## InfrGit

InfraGit is a tool which implements git semantics on infrastructure.

Wrapping terraform under the hood, you can:

- [ ] checkout - copy/clone infrastructure
- [ ] commit - save infrastructure + data state
- [ ] revert - revert to a saved commit point
- [ ] hooks - allow pre/post checkout/commit hooks to run data migrations to enable complete clone

This is quite an ambitious project and it might be impossible to achieve. However, with limited scope it might be achievable. With compromises like - works only on top of GCP, implement hooks and let the user manage data migration and persistence, etc - this might be possible

The initial version will focus on GCP (which is what I am most familiar with) and will implement the hooks into the lifecycle

### Usage

```sh
# Prepare .igit folder for igit related state and files
igit init

# Initialize terraform modules and providers
igit terraform init

# Check status
igit status
"On 'webadd-prod' workspace
...
...
"

# Clone infrastructure
igit checkout -b add-labels-for-billing

# Add labels to resources

# Commit and applies infrastructure and data changes
igit commit -am "FEA: Add labels for infrastructure cost monitoring"

```
