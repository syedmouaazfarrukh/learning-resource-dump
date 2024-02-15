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
    -   
- Worker Nodes
- Pods
- Services
- Deployments
- The API and API Server
- Recap




