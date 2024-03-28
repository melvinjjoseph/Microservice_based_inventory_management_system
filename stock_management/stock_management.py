import pika

def callback(ch, method, properties, body):
    print("Received message:", body)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='stock_management_queue')
channel.basic_consume(queue='stock_management_queue', on_message_callback=callback, auto_ack=True)

print("Waiting for stock management messages. To exit press CTRL+C")
channel.start_consuming()
