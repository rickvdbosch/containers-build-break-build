# Container Lab Guide
Welcome to the container lab! In this exercise, you will run a containerized application in three different environments: locally, Azure Container Instance (ACI), and Azure Container Apps (ACA). Each environment will return a unique letter, and by the end, you’ll have all the letters needed for the final answer.

Each user will work in their own Azure environment, using their own container registry and services.

# Prerequisites
Azure Subscription: Ensure you have access to an Azure subscription.
Docker Installed: Make sure Docker is installed on your local machine.
Azure CLI Installed: You’ll need the Azure CLI to interact with Azure services.
Azure Container Registry (ACR): You’ll use your own ACR to store container images for ACI and ACA.

## Steps
## 1. Clone the Repository
First, clone the repository to your local workstation:

bash
Copy code
git clone https://github.com/yourusername/your-repo.git
cd your-repo
## 2. Set Up Your Azure Container Registry (ACR)
Create a Resource Group (if you don’t have one):

bash
Copy code
az group create --name <your-resource-group> --location <region>
Create an Azure Container Registry:

bash
Copy code
az acr create --resource-group <your-resource-group> --name <your-registry-name> --sku Basic --location <region>
Log in to ACR:

bash
Copy code
az acr login --name <your-registry-name>
Replace <your-resource-group>, <your-registry-name>, and <region> with your specific values.

## 3. Run the Container Locally
In this step, you will use Dockerfile.local to build and run the container locally.

Build the Docker Image:

bash
Copy code
docker build -t letter-local -f Dockerfile.local .
Run the Docker Container:

bash
Copy code
docker run letter-local
Check the Output:
You should see a letter for the local environment displayed in the console.

## 4. Deploy to Azure Container Instance (ACI)
In this step, you’ll build and push the image to ACR, then deploy it to Azure Container Instance.

Build the Docker Image for ACI:

bash
Copy code
docker build -t <your-registry-name>.azurecr.io/letter-aci -f Dockerfile.aci .
Push the Image to ACR:

bash
Copy code
docker push <your-registry-name>.azurecr.io/letter-aci
Deploy to Azure Container Instance:

Run the following command to deploy the container, setting ENVIRONMENT=aci as an environment variable:

bash
Copy code
az container create \
  --resource-group <your-resource-group> \
  --name letter-aci \
  --image <your-registry-name>.azurecr.io/letter-aci \
  --registry-login-server <your-registry-name>.azurecr.io \
  --registry-username <your-registry-name> \
  --registry-password <your-acr-password> \
  --environment-variables ENVIRONMENT=aci \
  --dns-name-label <unique-dns-label> \
  --ports 5000
Replace <unique-dns-label> with a unique DNS name for your container.
Replace <your-acr-password> with the password for your Azure Container Registry (you can retrieve it from the ACR’s Access keys section in the Azure Portal).
View the Output in Logs: Go to the Azure Portal > Container Instances > letter-aci > Logs to view the letter output for aci.

## 5. Deploy to Azure Container Apps (ACA)
This step involves deploying the container to Azure Container Apps.

Create a Container Apps Environment (if not already created):

bash
Copy code
az containerapp env create --name <your-containerapps-env> --resource-group <your-resource-group> --location <region>
Build and Push the Docker Image for ACA:

bash
Copy code
docker build -t <your-registry-name>.azurecr.io/letter-containerapps -f Dockerfile.containerapps .
docker push <your-registry-name>.azurecr.io/letter-containerapps
Deploy to Azure Container Apps:

Run the following command to deploy to Azure Container Apps, ensuring ENVIRONMENT=containerapps is set:

bash
Copy code
az containerapp create \
  --name letter-containerapps \
  --resource-group <your-resource-group> \
  --environment <your-containerapps-env> \
  --image <your-registry-name>.azurecr.io/letter-containerapps \
  --registry-server <your-registry-name>.azurecr.io \
  --registry-username <your-registry-name> \
  --registry-password <your-acr-password> \
  --env-vars ENVIRONMENT=containerapps \
  --ingress external --target-port 5000
View the Output in Logs: In the Azure Portal > Container Apps > letter-containerapps > Logs, you should see the letter for containerapps.