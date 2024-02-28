# Azure Securing your Data

## Top 5 security items to consider before pushing to production

- Use Microsoft Defender for Cloud.
    - Can monitor both Cloud and On-premises services

- Verify your application's inputs and outputs.
    - Inputs:
        - Security weakness of current applications is a failure to correctly validate input data
        - Don't use inline SQL
        - Use Procedures instead o`f inline SQL
    - Outputs:
        - Screen outputs are encoded, not to be interpreted as code

- Store your secrets into Key Vault.
    - Service - `Azure Key Vault`
        - centralized cloud service for storing application secrets
        - Secrets are stored in individual vaults, own configuration and security policies to control access.
        - Can get data through a REST API or client SDK's
    - Why use Key Vault
        - Credential theft
        - Manual key rotation
        - Certificate renewal.

- Ensure you're using the latest version of your framework, and its security features.
    - Use new modern frameworks
    - Built in security in .NET
        - Authentication - Identity Management
        - Authorization
        - Data Protection
        - Secure Configuration
        - Security Extensibility APIs

- Validate that your program dependencies and libraries are safe to use.
    - OWASP top 10 list of worst web application vulnerabilities
    - Track known security vulnerabilities 
        - `Mitre` maintain *Common Vulnerabilities and Exposures list*
            - If you find a library or component in the CVE database, it has known vulnerabilities
    - Vulnerabilities in your third-party compo
        - Run these tools against your codebase, or better yet, add them to your CI/CD pipeline
            - OWASP Dependency Check, which has a Jenkins plugin
            - Snyk, which is free for open-source repositories in GitHub
            - Black Duck which is used by many enterprises
            - Retire.js


## Configure security policies to manage data

- Learn how to classify your data.
    - rest
        - Apply disk encryption to help safeguard your data.
        - Use encryption to help mitigate risks related to unauthorized data access.
    - in-process
    - transit
        - Secure access from multiple workstations located on-premises to an Azure virtual network - Use site-to-site VPN.
        - Secure access from an individual workstation located on-premises to an Azure virtual network - Use point-to-site VPN.
        - Move large data sets over a dedicated high-speed wide-area network (WAN) link - Use Azure ExpressRoute
        - Interact with Azure Storage through the Azure portal.

- Configure your data retention requirements.
- Explore data ownership and sovereignty.

- SQL Information Protection (SQL IP)
    - Azure SQL Auditing
    - Data Discovery & Classification
    - Dynamic data masking etc

- Classify your SQL DB
- Paired Regions
    - Cross-region activities number key
    - EG: ![paired-region](paired-region.png) 


## Secure your Azure Storage account

- 