## To Build Docker Container

docker build -t pytestharness:[version_number] .

## To Run Docker Container

Supply values for the ENV variables like this:

docker run -it -e OUTPUT_FORMATTER=EVENTHUB -e EVENT_HUB_NAMESPACE=golive -e EVENT_HUB_NAME=asbhub -e EVENT_HUB_SAS_POLICY=RootManageSharedAccessKey -e EVENT_HUB_SAS_KEY=ZhLwp6lrVWQt5UFgnogJXFbNnD8RDuHWfY0J9RN1ctE= -e KAFKA_HOST_IP=104.40.3.144 -e KAFKA_HOST_PORT=9092 -e KAFKA_TOPIC=asbtopic pytestharness:7
