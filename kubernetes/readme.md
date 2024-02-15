# Kubernetes

## Theoretical 

### Course Link
- [Getting Started with K8s with Nigel Poulton](https://app.pluralsight.com/ilx/video-courses/clips/374fcae1-fa4f-4bdc-8c3a-ef32cca2ac6a)
- [Course files and code](https://github.com/nigelpoulton/getting-started-k8s)

### Take Aways
- What is Kubernetes?
- Kubernetes Architecture
- Declarative Model and Desired State
- Getting Kubernetes
- Working with Pods
- Working with Services
- Working with Deployments
- What Next


#### What is Kubernetes?
- History
    - Means Helmsman (Greek)
    - Google with CNCF Project
    - github.com/kubernetes/kubernetes
    - written in `GO`
    - OpenSource
    - Related with Borg (Proprietary) and Omega (Proprietary) systems

- What it does
    - Container Orchestration
    - Similar to the role of OS
    - Communicates with the hardware to allocate resources
    - Sort of an abstraction layer
        - Packs apps in container
        - Describe them in Manifest
        - Done
    - Jargons
        - Monoliths vs Microservices (Containers)
- Why need it
    - Container Orchestration
        - Orchestration is like all players on a feild have a specific role along with a `COACH`. Coach manages the in-game strategy, replace players incase of injury. Change of strategy as per the requirements. Coach is the K8s.
    - Granular AutoScalling
    - Self healing


#### Kubernetes Architecture
- Big Picture
    - App in a package using a container and container is in a pod and the pod is in a deployment and all this is described in the K8's YAML file.
    - Place in a K8 Cluster (Feed the YAML)
    - Control Plane is the brain
    - Worker runs the user apps/services

- Control Plane Nodes or Masters
    - Should always be available
    - Use odd no of H/A Control planes (3 is magic, 5 is sweet)
    - Should be in different data centers
    - `1 is better than 2`
        - Split brain/Dealock
        - In case of network breakdown, each side will go int read-only mode because it won't have the majority
    - Follows an active/passive model
        - One is leader/Others are followers
        - For own clusters, linux machines for Control planes
    - Control plane features
    - In Hosted K8s, Cloud Manages control planes
    - Control Plane node not for userapps

    - Kuber-apiserver
        - front-end to control plane
        - everything to the control plane comes through this
        - EXPOSES the API(REST)
        - Consumes the YAML   
    - Cluster Store
        - Persists cluster state/configs
        - Based on `etcd`
        - Performance bottlenecks occur here
        - Have recovery plans
    - Kube-controller-manager
        - Controller
            - Node Controller
            - Deployments controller
            - Endpoints controller
        - Watch loops
        - Reconciles state
    - Kube-scheduler
        - Watches API server for work
        - Assigns tasks to worker
            - Affinity/Anti-affinity
            - Constraints
            - Taints
            - Resources

    - Commands is via `kubectl`
    ![Control Plane Architecture](control-plane.png)

- Worker Nodes
    - kubelet
        - Main K8s agent
        - Registers node with cluster
        - Work is in the form of Pods
            - Pods is one or more containers deployed
        - Watches API server for work
        - Executes Pods
        - Reports back to control plane
    - Container-runtime
        - Previously it was Docker
        - Pluggable CRI
        - Container-d (High usage)
        - gVisor
        - Katacontainers
    - kube-proxy
        - Node Networking
        - Pod IP addresses (One IP/POD)
        - For multi-container pods (all containers will share the same IP)
    - `A service is a way of hiding multiple pods behind a single IP like a load balancer`
    - Come cloud provide Nodeless Kubernetes - `Virtual Kubelet`


- Pods
    - Atmoic units of k8s
    - Containers run inside a pod
    - Shared execution env for an app to run
        - One IP address and Ports
        - Memory
        - Containers within a pod share resources
        - Scaling in K8s happen at Pod level (Scale-up by adding Pod and Scale-down by removing Pod )
        - Service Mesh
            -  A pod in which there is a mesh container that helps the main app container for enhanced services
        - Pod Deployment is atomic operation
        - All containers in a pod are scehduled with the same cluster node
    - Annotations, Labels, Policies, Resources and Co-scheduling

- Services
    - Stable abstraction point for multiple pods
    - Stable IP and DNS
    - Acts as a basic load balancing
    - Labels (Ties the services with the ones containing the labels)
    - send traffic to only healthy pods
    - Can do session Affinity - ?
    - Can send traffic outside of cluster
    - Can do TCP and UDP


- Deployments
    - Deployments are controllers that control pods
        - Stateless apps
        - Statefull apps
        - Daemon sets (One pod per node)
        - Time-based short-lived jobs
    - Watches API server for new deployments
    - Implements them and keeps a watch to maintain desire state
    - Deployment Types
        - ReplicaSet
        - 


- The API and API Server
    - All above objects are resource in K8s API
    - K8s API contains definition and feature set of each resource
    - API server exposes the resource API - HTTPS/REST(methods)


- Recap


#### Declarative Model and Desired State
- K8s prefers with Declarative model
    - Using manifest files
    - key-value pairs
    - Desired State vs Observed State



