# Azure Devops for Beginners

- Introducction
    - Set of practices
    - Highly pushses for collaboration

- Setup and Overview
    - Where to access
        - Web portal
        - CLI
        - Visual Studio
    - Payments Plan
    - Microsoft servers
    - You own servers for policy/security
    - Create an Azure DevOps project
    - Azure Devops demo generator (In your Azure accounts)
    - Add users to organizations and devops teams
        - Add users in Organization settings
        - From `Azure Active Directory`
        - From `Project settings` in Azure DevOps

- Azure Boards
- Azure Repos
- Azure Pipelines
    - Automate app build and deploy phase
    - CI - process of automating/testing
        - Build Pipeline
            - Merge code
            - Test code
            - workflow  (commit,merge,build,test)
    - CD - process of automating delivery
        - Release pipeline
            - Web app deployed on Azure App Service
            - Microservices, web front, database updates
            - Blue-Green Pattern
            - Feature Flag Pattern
            - EG: Windows 10 OS CI is done via Ring series
    - Types of automation
        - Automated Builds - Automated Release
        - Automated Builds - Manual Release
        - Manul Build - Automate Relase


    - Pipeline Parts
        - Multiple Stages run Jobs
            - Each stage has multiple scripts/tasks
            - Each script/tasks executes a job
            - Agent in stages run jobs
        - Manual runing of piplines or
        - Trigger
            - Repo Triggers
            - PR Triggers
            - Schedule Triggers
            - Pipeline Triggers
        - Collection of steps
            - Step is task/script
            - Script runs code using cli, bash etc
            - Tasks is package script or procedure using parameters
                - Categories: Build, Utility, test, package, deploy, tool
                - Eg: 
                    - Build: run MSBuild etc
                    - Utility: delete files, file transform
                    - Package: npm, NuGet Restore etc

        - Example Web Project
            - Deploy app in App service

        - Service Connection to Azure Resource Manager
        - Explore pipeline Templates
        - *Add a build pipleline*
        - Manually run and troubleshoot a pipeline
        - *Update the repo to trigger the build*
        - *Add a release pipeline*
        - Use custom variables in the pipeline
        