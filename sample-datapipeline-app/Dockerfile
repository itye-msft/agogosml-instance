FROM python:3.7-slim-stretch

# Set the working directory to /
WORKDIR /
# Copy the directory contents into the container at /
COPY . /

RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt
RUN python tests.py

ENTRYPOINT ["python", "ehreceiver.py"]