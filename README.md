Kubernetes 3-Node Cluster with Docker
This repository contains a project that demonstrates the setup and deployment of a containerized application using Docker and Kubernetes on a 3-node cluster. The setup includes one master node and two worker nodes, configured using VirtualBox on Ubuntu servers.

Table of Contents
1.Introduction
2.Project Structure
3.Prerequisites
4.Setup Instructions
5.Deployment
6.Monitoring and Auto-Healing
7.Usage
8.Contributing


1.Introduction
This project demonstrates a Kubernetes setup with a 3-node cluster consisting of one master node and two worker nodes. The master node runs client code that uses a round-robin algorithm to communicate with the servers running on the worker nodes. The servers respond to the client's 'hello' message with 'hii'. The client then waits for 1 second before sending the next message to another server.

2.Project Structure
Dockerfiles/: Contains Dockerfiles for building the client and server applications.
k8s-manifests/: Kubernetes YAML files for deploying the client and server applications.
scripts/: Setup and configuration scripts for automating the deployment process.
README.md: Project documentation.

3.Prerequisites
Before you begin, ensure you have the following installed:

VirtualBox: For creating virtual machines.
Ubuntu Server: Installed on the VMs.
Docker: To containerize the applications.
Kubernetes (MicroK8s): To manage the cluster.
kubectl: Kubernetes command-line tool.

4.Setup Instructions
Create Virtual Machines:

Set up three VMs using VirtualBox (1 master node, 2 worker nodes).
Install Ubuntu Server on all VMs.
Install Docker:

Install Docker on all nodes to containerize the applications.
Docker Installation Guide
Install Kubernetes (MicroK8s):

Install MicroK8s on all nodes.
Initialize the Kubernetes cluster and join worker nodes to the master.
MicroK8s Installation Guide
Configure Network:

Ensure all nodes can communicate over the network.
Install a Container Network Interface (CNI) plugin if not already installed.


5.Deployment
Build Docker Images:

Navigate to the Dockerfiles directory and build the images for the client and server applications.
bash
Copy code
docker build -t client-app:latest Dockerfiles/client/
docker build -t server-app:latest Dockerfiles/server/
Push Images to Docker Registry:

Push the Docker images to your preferred Docker registry.
Deploy to Kubernetes Cluster:

Apply the Kubernetes manifests to deploy the applications.
bash
Copy code
kubectl apply -f k8s-manifests/
Verify Deployment:

Check the status of your pods and services to ensure they are running correctly.
bash
Copy code
kubectl get pods
kubectl get services


6.Monitoring and Auto-Healing
Prometheus and Grafana: For monitoring the cluster and application metrics.
Kubernetes Health Checks: Configured in the deployment manifests to automatically restart failed pods.
Auto-Healing Scripts: Located in the scripts directory to automate node recovery and scaling.
Usage
Client Application: Runs on the master node and communicates with the servers on the worker nodes.
Server Application: Deployed on worker nodes, responds to client messages.
To see the logs of the client application:

bash
Copy code
kubectl logs <client-pod-name>


7.Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
