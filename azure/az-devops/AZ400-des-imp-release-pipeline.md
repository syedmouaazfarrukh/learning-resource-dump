#  AZ-400: Design and implement a release strategy

## Create a release pipeline 

- Pipelines capabilities
- build and release tasks
- multi-configuration/multi-agent

### Pipelines capabilities
- Pipeline as Code (YAML pipelines)
- UI-based release = classic release
- YAML Pipelines vs Classic Build/Release

### Explore release pipelines
- `Artifacts` as inputs
- Releases them through `stages` into production
- Components of release pipline:
    1. Artifacts can be from different sources
        - Most common source = package from build pipline
        - Another artifact source = source control
        - Explained below.

    2. Has a trigger mechanism
        - Manual (release by hand)
        - Scheduled (based on time)
        - Continuos deployment trigger (another event triggers a release)

    3. Stages/Environments
        - where the artifact will be eventually installed

    4. Approval
    5. Signing a Release
    6. Checking Quality (either manually/automatic)

    7. Tasks
        - Are within stages
        - Steps to install, configure, validate the artifact
    
#### Explore artifact sources
- Artifacts should 100% remain unchanged
- Most common is a build artifact
- Should be immutable
- Network sharing artifacts won't be a good choice in regulated env
- Container registries are somewhat similar to using a build artifact.
- Chosing the appropriate artifact source
    - In release pipeline, you need traceability
    - Should know the package origin
    - A proper mechanism to make sure you can provide the correct traceability and auditability is using `immutable packages`. 



#### Explore build and release tasks
#### Explore custom build and release tasks
#### Explore release jobs
#### Understand database deployment task
- Data separation
- Data preservation
- Idempotent operations
- Versioning and rollback
- Testing and validation
- Monitoring and alerting



### Configure Pipelines as Code with YAML
