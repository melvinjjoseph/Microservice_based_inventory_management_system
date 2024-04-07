from flask import Flask, request, render_template, jsonify
import pymongo
import pika
import json
import sys


app = Flask(
    __name__,
    template_folder='templates'
)

# Connect to MongoDB
client = pymongo.MongoClient('add your mongodb connection string here')
db = client["database"]
collection = db["inventory"]


# RabbitMQ setup
try:
    credentials = pika.PlainCredentials(username='guest', password='guest')
    parameters = pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
except pika.exceptions.AMQPConnectionError as e:
    print("Failed to connect to RabbitMQ: ", e)
    sys.exit(1)

# Declare exchange
try:
    channel.exchange_declare(
        exchange='microservices', 
        exchange_type='direct',
        durable=True
    )
except pika.exceptions.ChannelClosedByBroker as e:
    print("Failed to declare exchange: ", e)
    sys.exit(1)

# Declare queues
try:
    channel.queue_declare(queue='health_check', durable=True)
    channel.queue_declare(queue='insert_record', durable=True)
    channel.queue_declare(queue='delete_record', durable=True)
    channel.queue_declare(queue='read_database', durable=True)
    channel.queue_declare(queue='send_database', durable=True)
    print("Queues declared successfully")
except pika.exceptions.ChannelClosedByBroker as e:
    print("Failed to declare queue: ", e)
    sys.exit(1)

# Bind queues to exchange with routing keys
try:
    channel.queue_bind(exchange='microservices', queue='health_check', routing_key='health_check')
    channel.queue_bind(exchange='microservices', queue='insert_record', routing_key='insert_record')
    channel.queue_bind(exchange='microservices', queue='delete_record', routing_key='delete_record')
except pika.exceptions.ChannelClosedByBroker as e:
    print("Failed to bind queue to exchange: ", e)
    sys.exit(1)


@app.route('/')
def index():
    return render_template('index.html')

# Health check endpoint
@app.route('/health_check', methods=['GET'])
def health_check():
    #check if the service is up
    if connection.is_open:
        return 'Service is up!'
    else:
        return 'Service is down!'

    # try:
    #     channel.basic_publish(exchange='microservices', routing_key='health_check', body=message)
    # except pika.exceptions.UnroutableError as e:
    #     print("Failed to publish message: ", e)
    #     return 'Failed to send Health Check message!'
    # return 'Health Check message sent!'

# # Insert record endpoint
@app.route('/insert_record', methods=['GET', 'POST'])
def insert_record():
    if request.method == 'POST':
        product_name = request.form['product_name']
        product_id = request.form['product_id']
        units = request.form['units']
        message = json.dumps({'product_name': product_name, 'product_id': product_id, 'units': units})
        try:
            channel.basic_publish(exchange='microservices', routing_key='insert_record', body=message)
            print("Message sent: ", message)
            return render_template('insert.html', message='Record Inserted Successfully!')
        except pika.exceptions.UnroutableError as e:
            print("Failed to publish message: ", e)
            return render_template('insert.html', message='Failed to insert record!')
    else:  # GET request
        return render_template('insert.html', message='Add a new record!')

# Delete record endpoint
@app.route('/delete_record', methods=['GET', 'POST'])
def delete_record():
    if request.method == 'POST':
        product_id = request.form['product_id']
        message = product_id
        try:
            channel.basic_publish(exchange='microservices', routing_key='delete_record', body=message)
        except pika.exceptions.UnroutableError as e:
            print("Failed to publish message: ", e)
            return render_template('delete.html', message='Failed to delete record!')
        return render_template('delete.html', message='Record Deleted Successfully!')
    else:  # GET request
        return render_template('delete.html', message='Enter the product ID to delete the record!')

@app.route('/read_database', methods=['GET'])
def read_database():
    try:
        method_frame, header_frame, body  = channel.basic_get(queue='send_database')
        if method_frame:
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            records = body.decode()
        else:
            records = list(collection.find())
    except pika.exceptions.ChannelClosedByBroker as e:
        print("Failed to get message: ", e)
        return jsonify({"error": "Failed to read database!"})
    return render_template('read.html', message='Records retrieved from the database: ', records=records)


if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print("Failed to run application: ", e)
