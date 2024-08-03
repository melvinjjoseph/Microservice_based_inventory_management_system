# Microservice based Inventory Management System
   
## 📎 About
The inventory management system aims to efficiently manage inventory
items, track stock levels, and handle orders through a microservices architecture. The system will utilize RabbitMQ
for inter-service communication and Docker for containerisation, ensuring scalability, modularity, and ease of
deployment.

## 🛠️ Stack Used
<div>
  <a href="https://www.python.org/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;</a>
  <a href="https://www.mongodb.com/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original-wordmark.svg" title="MongoDB" alt="MongoDB" width="40" height="40"/>&nbsp;</a>
  <a href="https://www.docker.com/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original-wordmark.svg" title="Docker" **alt="Docker" width="40" height="40"/></a>
  <a href="https://www.rabbitmq.com/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rabbitmq/rabbitmq-original.svg" title="RabbitMQ" alt="RabbitMQ" width="40" height="40"/>&nbsp;</a>
  <a href="https://flask.palletsprojects.com"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original-wordmark.svg" title="Flask" alt="Flask" width="40" height="40"/>&nbsp;</a>
</div>

## 🚀 Getting Started
1. Clone the repository
```{bash}
git clone https://github.com/melvinjjoseph/Microservice_based_inventory_management_system.git 
```
2. Change the directory
```{bash}
cd Microservice_based_inventory_management_system
```
3. Add your mongodb connection string in `read_database.py` , `app.py` , `deletion.py` , `order.py` and `insertion.py`
4. Run the following command to start the services
```{bash}
docker-compose up --build
```
5. The services will be up and running and you can view them using the frontend at `http://127.0.0.1:5000/`
