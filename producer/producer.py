import pika

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queues for different microservices
health_check_queue = 'health_check_queue'
item_creation_queue = 'item_creation_queue'
stock_management_queue = 'stock_management_queue'
order_processing_queue = 'order_processing_queue'

# Publish messages to the queues
channel.queue_declare(queue=health_check_queue)
channel.queue_declare(queue=item_creation_queue)
channel.queue_declare(queue=stock_management_queue)
channel.queue_declare(queue=order_processing_queue)

# Example messages
health_check_message = "Health check message"
item_creation_message = "Item creation message"
stock_management_message = "Stock management message"
order_processing_message = "Order processing message"

# Send messages to respective queues
channel.basic_publish(exchange='', routing_key=health_check_queue, body=health_check_message)
channel.basic_publish(exchange='', routing_key=item_creation_queue, body=item_creation_message)
channel.basic_publish(exchange='', routing_key=stock_management_queue, body=stock_management_message)
channel.basic_publish(exchange='', routing_key=order_processing_queue, body=order_processing_message)

print("Messages sent to RabbitMQ")

# Close the connection
connection.close()
