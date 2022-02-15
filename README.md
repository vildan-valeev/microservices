#  microservices in docker - test project
Небольшой тест работы запросов между контейнерами в докере
## To start
`docker-compose up`

Generate pb2.py files
````
python -m grpc_tools.protoc -I pb --python_out=pb --grpc_python_out=pb pb/main.proto


````