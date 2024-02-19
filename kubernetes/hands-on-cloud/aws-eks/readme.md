# Amazon Elastic Kubernetes Service (EKS)

## Theoretically 
- Managed K8s cluster on AWS
- Similar to ECS, ECS is not opensource
- Two launch modes
    - EC2 Mode
    - Fargate (serverless containers)
- To expose cluster to web, public/private load balancers are setup
- EKS NodeTypes
    - Managed Node Groups
        - Creates/manages EC2 instances
        - Nodes are part of AutoScalling Group
        - Supports on-Demand or Spot instances
    - Self-Managed Nodes
        - You create/register nodes to EKS cluster
        - Can use EKS AMI's or custom AMI
        - Supports on-Demand or Spot instances
    - AWS Fargate
        - No nodes are managed
        - Containers are run on top of EKS

- EKS Data Volumes
    - Must specify StorageClass manifest on EKS cluster
    - Leverages a container-storage-interface (CSI) complaint driver
    - Support for
        - Amazon EBS
        - Amazon EFS (works with Fargate)

- Diagram
    - EKS pods are similar to ECS tasks
![alt text](image-1.png)

## Hands-On-Practice
- Not available in free tier
- To create a cluster, create a `Cluster service Role`
    - Create a role in IAM
        - Select service and then EKS as use case
        - Need to have a VPC, Subnets, and Security
        - Publicly accessible
    