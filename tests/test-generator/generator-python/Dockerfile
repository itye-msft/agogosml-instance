
FROM python:3.7-slim-stretch 
#as base
#FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY . .
#RUN pip install --install-option="--prefix=/install" -r /requirements.txt
RUN pip install -r requirements.txt
#FROM base
#COPY --from=builder /install /usr/local
COPY . /app

WORKDIR /app

ENV OUTPUT_FORMATTER=[changeme]\
EVENT_HUB_NAMESPACE=[changeme]\
EVENT_HUB_NAME=[changeme]\
EVENT_HUB_SAS_POLICY=[changeme]\
EVENT_HUB_SAS_KEY=[changeme]\
KAFKA_HOST_IP=[changeme]\
KAFKA_HOST_PORT=[changeme]\
KAFKA_TOPIC=[changeme]

ENTRYPOINT ["python", "main.py"]
