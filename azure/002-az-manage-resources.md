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

- Apply policies to enforce standards in your Azure environments.
- Use resource locks to protect critical Azure resources from accidental deletion.