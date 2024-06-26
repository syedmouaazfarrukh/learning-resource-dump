# Learning objectives

## Align requirements with cloud types and service models in Azure
- Compare each cloud computing deployment model: public, private, and hybrid.
    - Why Public Cloud
        - Service consumption through on-demand or subscription model
        - No up-front investment in hardware:
        - Automation
        - Geographic dispersion
        - Reduced hardware maintenance
    - Why Private Cloud
        - Pre-existing environment
        - Legacy applications
        - Data sovereignty and security
        - Regulatory compliance / certification
    - Why Hybrid Cloud
        - Existing hardware investment
        - Regulatory requirements
        - Unique operating environment
        - Migration


## Azure PowerShell
- Azure PowerShell
    - Three administration tools (Azure):
        - Azure portal
        - Azure CLI
            - Inside a browser via the Azure Cloud Shell
            - Local installation (Linux/Windows)
        - Azure PowerShell
            - Added to a Shell
            - PowerShell cmdlets
                - (pronounced "command-let")
                - To imply "small command."
            - PowerShell module
                - Cmdlets are shipped in modules
                - Is a dynamic-link library (DLL)
                - Includes the code to process each available cmdlet
            - PowerShell Script
                - A text file containing commands and control constructs


## Resource Group 
- Organize your resources
- Is a logical container for resources
- Resources can be a member of single resource group
- Resource groups can't be nested

- Logical resource grouping
    - Placing resource of similar usage, type, or location into resource groups
- Lifecycle
    - Delete a resource group, all resources contained within the group are also deleted
- Authorization
    - Apply role-based access control (RBAC) permissions

- Tags to organize resources.
    - name/value pairs of text data
    - resource has the following properties
        - department (like finance, marketing, and more)
        - environment (prod, test, dev)
        - cost center
        - lifecycle and automation
    - Limit is 50 Tags
    - Uses:
        - use tags to group your billing data
        - retrieve all the resources in your subscription that have a specific tag name or value
        - help in monitoring to track down impacted resources.
        - common for tags to be used in automation:
            - *EG:* If you want to automate the shutdown and startup of virtual machines in development environments during off-hours to save costs, you can use tags to support automation. Add a shutdown:6PM and startup:7AM tag to the virtual machines, then create an automation job that looks for these tags and shuts down or starts resources based on their tag value. There are several solutions in the Azure Automation Runbooks Gallery that use tags in a similar manner to accomplish this result.

- Policies for Resource Groups.
    - Azure Policy is a service you can use to create, assign, and manage policies
    - apply and enforce rules that your resources need to follow
        - *EG*: Policies can enforce rules such as only allowing specific types of resources to be created or only allowing resources in specific Azure regions. You can enforce naming conventions across your Azure environment. You can also enforce that specific tags are applied to resources. Let's take a look at how policies work.
    - Create a policy Definition
        - Definition location should be same subs as for resource group
        - Make it tag compulsory for resources in resource group
        - Go and create a resource within that resource group without tag, it won't be created
        - Now create the same after adding tag, resource will be created.
    - Create a policy assignment


- Secure resources with role-based access control.
    - Allow one user to manage VMs in a subscription and another user to manage virtual networks.
    - Allow a database administrator (DBA) group to manage SQL databases in a subscription.
    - Allow a user to manage all resources in a resource group, such as VMs, websites, and virtual subnets.
    - Allow an application to access all resources in a resource group.
    - Best Practices for RBAC
        - grant users only the amount of access that they need to perform their jobs.
        - grant users the lowest privilege level that they need to do their work
        - Use Resource Locks to ensure critical resources aren't modified or deleted

- Resouce locks and how to use them
    - A setting that you can apply to any resource to block modification or deletion
    - In a recent conversation, your manager mentioned that there had been instances where critical Azure resources were mistakenly deleted. Because there was disorganization across their Azure environment, good intentions of cleaning up unnecessary resources resulted in accidental deletions of resources critical to other systems. You've heard of resource locks on Azure. You mention to your manager that you think you can help prevent this type of incident from happening in the future
    - Delete or Read-only
    - Create a lock in the resource group


- Move Resources to another Resource Group
    - Identify whether you can move resources.
        - Your organization has a resource group that contains both production resources and development resources. You're going to move the development resources out of that group and into their own resource group, which is dedicated to development.
    
    - Identify all resources in the production resource group.
    - Check the limitations of resources and whether they can be moved to a new resource group.
    - Run a test validation to verify that resources can move successfully.
    - Create a new resource group to hold the development resources by using the Azure portal.
    - Move resources from the production resource group to the new resource group.
    - Confirm that the resources are in the new group.