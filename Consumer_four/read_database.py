import pika
import pymongo
import sys

# Connect to MongoDB
client = pymongo.MongoClient('mongodb+srv://melvin:melvin123@cluster0.kmverd6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client["database"]
collection = db["inventory"]

# RabbitMQ setup
try:
    credentials = pika.PlainCredentials(username='guest', password='guest')
    parameters = pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=credentials)
    connection = pika.BlockingConnection(parameters=parameters)
    channel = connection.channel()
except pika.exceptions.AMQPConnectionError as e:
    print("Failed to connect to RabbitMQ: ", e)
    sys.exit(1)

# Declare the "read_database" queue
try:
    channel.queue_declare(
        queue='read_database',
        durable=True
    )

    channel.queue_declare(queue='send_database', durable=True)
    channel.queue_bind(exchange='microservices', queue='send_database', routing_key='send_database')
except pika.exceptions.ChannelClosedByBroker as e:
    print("Failed to declare queue or bind queue to exchange: ", e)
    sys.exit(1)

# Define the callback function to process incoming messages
def callback(ch, method, properties, body):
    # Retrieve all records from the database
    records = collection.find()
    print("Records retrieved from the database: ", records)
    # Send each record to the producer through RabbitMQ
    for record in records:
        channel.basic_publish(
            exchange='microservices',
            routing_key='send_database',
            body=str(record)
        )
    
    # Acknowledge that the message has been processed
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Consume messages from the "read_database" queue
try:
    channel.basic_consume(queue='read_database', on_message_callback=callback)
except pika.exceptions.ChannelClosedByBroker as e:
    print("Failed to consume messages: ", e)
    sys.exit(1)

# Start consuming messages
print('Waiting for messages...')
channel.start_consuming()