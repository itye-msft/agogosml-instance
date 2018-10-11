# agogosml_instance
An instance for Agogosml generator

## Creating Build Pipeline

### Assumptions

    -You have created a [Service Connection](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=vsts) in Azure Devops for the Resource Group containing your ACR
    -All relevant helm files are in a subdirectory with the same name as the application folder (e.g. sampleapp/sampleapp/)
    -The application and test harness each have their own subdirectory

### Variables

- appImageName: The name of the container image of the application itself
- testImageName: The name of the container image of the test harness
- registryName: The name of the ACR instance (contoso.azurecr.io)
- SubscriptionEndpointName: the name of the Service Endpoint in Azure Devops
- appDirectory: The name of the folder containing app code and Dockerfile (whithout a trailing slash)
- testDirectory: The name of the folder containing test code and Dockerfile (whithout a trailing slash)

### Steps

#### Docker Build

The first 2 steps build the docker images for the application and the test harness containers. Each directory has a Dockerfile at their top levels

#### Helm Install

Currently set to version 2.9.1. This installs Helm

#### Lint Helm

Calls the ```helm lint``` command on the application directory

#### Docker Login

Logs into the ACR container

#### Docker Push

Pushes the container to the registry

#### Publish

Publishes the helm directory to 'drop'