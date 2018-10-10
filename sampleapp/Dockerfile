FROM python:3.7.0-alpine3.8

# Set the working directory to /
WORKDIR /
# Copy the directory contents into the container at /
COPY . /

ENV EH_CONN_STRING tbd1
ENV BLOB_ST_CONN_STRING tbd2
ENV BUILD_NAME tbd3

RUN pip install -r requirements.txt
RUN python hellotest.py

CMD ["python", "hello.py"]