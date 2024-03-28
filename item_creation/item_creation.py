import pika

def callback(ch, method, properties, body):
    print("Received message:", body)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='item_creation_queue')
channel.basic_consume(queue='item_creation_queue', on_message_callback=callback, auto_ack=True)

print("Waiting for item creation messages. To exit press CTRL+C")
channel.start_consuming()
