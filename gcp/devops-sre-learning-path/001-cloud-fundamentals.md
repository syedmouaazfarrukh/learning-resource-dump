# Cloud Fundamentals Core Infrastructure

Major Services
- Compute
- Storage
- BigData
- Machine Learning
- Application services

For
- Solution developer
- SysOps professional
- System architecture
- Business decision makers

Key Objects
- Understand gcp services
- how infrastructure is org
- how to create an infrastructure
- select and use storage options
- understand GKE
- Understand serverless gcp services

Cloud Computing overview
IaaS, PaaS and SaaS
GCP Network
Environmental Impact
Security
- Hardware infrastructure security (Own Servers/chips etc)
- Service layer security (encrypted inter-service communication)
- Identity layer
- Storage security (encryption at REST)
- Internet communication layer (GFE, DoS protection)
- Operational Security (intrusion, insider risk, U2F, software dev practices)
Open-Source Ecosystems
Pricing and Billings

Resources/Access in Cloud
- IAM
- Service accounts
- Cloud Identity
- Interacting with google cloud

- VMs/Networks in Cloud
    - VPC Networking (Types of Peering (Direct, Carrier, Dedicated, Partner, Cross-Cloud))
    - Compute Engine
    - Scaling Virtual machines
    - Cloud Load Balancing
    - Cloud DNS and CDN (8.8.8.8 - available)
    - `Lab - Getting stated with VPC networking and google compute` 

- Storage in GCP
    - Diff types of storage (5)
        - storage
            - objects (binary form of actual data)
            - in bucket and is managed
            - for web, direct archiving, BLOB
            - security (IAM, ACLs(scope,permission) RBAC) - encryption at server
            - classes (standard, nearline, coldine, archive) - `autoclass` feature
        
        - Sql
            - Relational (mysql,postgre,sql)

        - spanner
            - relational
            - Fully managed
            - HA and consistency

        - Firestore
            - NoSQL database
            - data - document - collection
            - retreival of ind and collection of documents
            - Can do CRUD operations
            - price for read,write and delete and storage used


        - bigtable
            - NoSQL (semi-structured ) for BigData
            - Massive workloads and great read latency
            - Mostly for time-based data
            - Data can streamed/Batched in and out by 3rd party clients


    - Comparison
        - ![alt text](/gcp/src/image.png)



- Containers in the Cloud
    - Containers (isolated and lightweight OS environments)
    - Kuberenetes (Container orchestration)
        - FOR MORE INFO: [DETAILED INFO ON KUBERNETES](/kubernetes/readme.md)
        - GKE
            - Multiple compute engine instances
            - Cluster customization
            - Deploy/manage apps
            - For administration etc
            - Allows for cluster management

- Applications in Cloud
    - Cloud Run
        - Service to run containers
        - Serverless
        - Built on Knative
        - Price as you go
        - Three steps
            - Write your code
            - build and pckg your code in container
            - Image is run by cloud run

        - container-based workflow
            - deploys container images

        - source-based workflow
            - deploy source instead of a container
            - using buildpacks

    - Cloud Function



- Prompt Engineering Guide
    - What is genAI
    - what is LLM
    - What is promt eng
    - Best prac for prompt eng