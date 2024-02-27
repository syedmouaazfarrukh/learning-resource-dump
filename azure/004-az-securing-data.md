# Azure Securing your Data

## Top 5 security items to consider before pushing to production

- Use Microsoft Defender for Cloud.
    - Can monitor both Cloud and On-premises services

- Verify your application's inputs and outputs.
    - Inputs:
        - Security weakness of current applications is a failure to correctly validate input data
        - Don't use inline SQL
        - Use Procedures instead of inline SQL
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