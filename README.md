# 250_264_265_294_Microservices_communication_using_RabbitMQ 

Mini Project for the Cloud Computing - UE21CS351 course.

## Batch Number 13
### Team Members
1. [L Sai Tejas - PES2UG21CS250](https://github.com/saiii009)
2. [Madduri Sai Sriya Samhitha - PES2UG21CS264](https://github.com/sriyasamhitha)
3. [Madhava Bhat Bhave - PES2UG21CS265](https://github.com/madhavabhave)
4. [Melvin Jojee Joseph - PES2UG21CS294](https://github.com/melvinjjoseph)
   
## Problem Statement
Build an inventory management system. The inventory management system aims to efficiently manage inventory
items, track stock levels, and handle orders through a microservices architecture. The system will utilize RabbitMQ
for inter-service communication and Docker for containerisation, ensuring scalability, modularity, and ease of
deployment.

## Getting Started
1. Clone the repository
```{bash}
git clone https://github.com/melvinjjoseph/250_264_265_294_Microservices_communication_using_RabbitMQ.git 
```
2. Change the directory
```{bash}
cd 250_264_265_294_Microservices_communication_using_RabbitMQ
```
3. Add your mongodb connection string in `read_database.py` , `app.py` , `deletion.py` , `order.py` and `insertion.py`
4. Run the following command to start the services
```{bash}
docker-compose up --build
```
5. The services will be up and running and you can view them using the simple frontend at `http://127.0.0.1:5000/`
