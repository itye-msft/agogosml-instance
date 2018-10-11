# How to run

## Option 1 - Locally using Python

### Requirements

- Python3
- Install everything in requirements.txt

### Run

1. Ensure that you have a .env file with appropriate environment variables as listed in the env-template.
2. Run `python ehreceiver.py`
3. Run `python ehsender.py`

## Option 2 - Using Kubernetes

### Requirements

- Kubernetes cluster

### Run

Use 'Helm install' command.
Example:

Navigate to the chart's directory and run:

```bash
helm install .\
--set env.EVENT_HUB_CONSUMER_GROUP="[value]"\
--set env.AZURE_STORAGE_ACCOUNT="[value]"\
--set env.AZURE_STORAGE_ACCESS_KEY="[Base64 value]"\
--set env.AZURE_STORAGE_CONTAINER="[value]"\
--set env.EVENT_HUB_NAMESPACE="[value]"\
--set env.EVENT_HUB_NAME="[value]"\
--set env.EVENT_HUB_STORAGE_ACCOUNT="[value]"\
--set env.EVENT_HUB_STORAGE_CONTAINER="[value]"\
--set env.EVENT_HUB_SAS_POLICY="[value]"\
--set env.EVENT_HUB_SAS_KEY="[Base64 value]"
```

Notice that the secrets are Base64 encoded values