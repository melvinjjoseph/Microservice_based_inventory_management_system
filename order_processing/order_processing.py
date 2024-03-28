import pika

def callback(ch, method, properties, body):
    print("Received message:", body)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='order_processing_queue')
channel.basic_consume(queue='order_processing_queue', on_message_callback=callback, auto_ack=True)

print("Waiting for order processing messages. To exit press CTRL+C")
channel.start_consuming()
