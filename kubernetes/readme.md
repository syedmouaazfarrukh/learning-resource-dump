# Kubernetes

## Theoretical 

### Course Link
- [Getting Started with K8s with Nigel Poulton](https://app.pluralsight.com/ilx/video-courses/clips/374fcae1-fa4f-4bdc-8c3a-ef32cca2ac6a)
- [Course files and code](https://github.com/nigelpoulton/getting-started-k8s)

### Take Aways
- What is Kubernetes?
- Kubernetes Architecture
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


#### What is Kubernetes?
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
    - ![Control Plane Architecture](control-plane.png)




- Worker Nodes
- Pods
- Services
- Deployments
- The API and API Server
- Recap




