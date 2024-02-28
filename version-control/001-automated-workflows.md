# Automated Workflows

## GitHub Actions:

**1. GitHub Actions Overview:**
   - GitHub Actions is a CI/CD and automation service provided by GitHub.
   - It allows you to define custom workflows using YAML syntax directly within your repository.

**2. Key Concepts:**
   - **Workflow:** A configurable automated process made up of one or more jobs.
   - **Job:** A set of steps that run on the same runner.
   - **Step:** A single task within a job. Steps can include running commands, checking out code, or using an action.

**3. Example Workflow:**
   ```yaml
   name: CI/CD Pipeline

   on:
     push:
       branches:
         - main

   jobs:
     build:
       runs-on: ubuntu-latest

       steps:
         - name: Checkout Repository
           uses: actions/checkout@v2

         - name: Build
           run: |
             # Your build commands here

         - name: Test
           run: |
             # Your test commands here

         - name: Deploy
           run: |
             # Your deployment commands here
   ```

**4. GitHub Actions Marketplace:**
   - GitHub Actions has a marketplace where you can find and use existing actions for various tasks.



## GitLab CI:

**1. GitLab CI Overview:**
   - GitLab CI/CD is the built-in CI/CD service provided by GitLab.

**2. Key Concepts:**
   - **.gitlab-ci.yml:** A configuration file where you define your CI/CD pipelines.
   - **Pipeline:** A series of jobs defined in `.gitlab-ci.yml` that run sequentially or in parallel.

**3. Example `.gitlab-ci.yml`:**
   ```yaml
   stages:
     - build
     - test
     - deploy

   build:
     stage: build
     script:
       - echo "Building..."

   test:
     stage: test
     script:
       - echo "Testing..."

   deploy:
     stage: deploy
     script:
       - echo "Deploying..."
   ```

**4. Runners and Executors:**
   - GitLab Runners execute the CI/CD jobs. They can be shared or specific to a project.



## Bitbucket Pipelines:

**1. Bitbucket Pipelines Overview:**
   - Bitbucket Pipelines is a CI/CD service integrated directly into Bitbucket repositories.

**2. Key Concepts:**
   - **bitbucket-pipelines.yml:** Configuration file for defining pipelines.
   - **Pipeline:** A series of steps defined in `bitbucket-pipelines.yml` that run when triggered.

**3. Example `bitbucket-pipelines.yml`:**
   ```yaml
   image: node:14

   pipelines:
     default:
       - step:
           name: Build and Test
           script:
             - npm install
             - npm test
       - step:
           name: Deploy
           deployment: production
           script:
             - echo "Deploying to production..."
   ```

**4. Integrations:**
   - Bitbucket Pipelines seamlessly integrates with Bitbucket repositories, making it easy to set up CI/CD for your projects.


## Common CI/CD Concepts:

**1. Triggers:** Events that initiate a CI/CD pipeline, such as code pushes, pull requests, or scheduled builds.
**2. Artifacts:** Files generated during the CI/CD process that can be reused or deployed.
**3. Environments:** Target environments where the code is deployed after passing CI/CD stages.
**4. Notifications:** Receive notifications or status updates based on CI/CD pipeline results.
**5. Parallelism:** Running multiple jobs or steps concurrently to speed up the CI/CD process.
**6. Deployment Strategies:** Blue/Green deployments, canary releases, etc., to control the rollout of changes to production.

