# Container image

Select a Ravenstash repository with OCI enabled, then build, push, and pull the example through the `rvs` Docker wrapper:

```bash
rvs art select acme/runtime-images
rvs docker build -t acme/example:1.0.0 .
rvs docker push acme/example:1.0.0
rvs docker pull acme/example:1.0.0
```

The wrapper expands the short image name inside the selected repository and provides temporary registry access without changing your persistent Docker credentials. It prints the full local image reference retained by a pull.

Dockerfiles and Buildx output tags are not shorthand-aware. Use the full Ravenstash reference for those cases, for example:

```text
oci.rvsta.sh/acme/runtime-images/acme/example:1.0.0
```

See [Push and pull container images](https://docs.ravenstash.com/container/push-and-pull/).
