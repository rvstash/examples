# Helm OCI chart

Ravenstash stores Helm charts as OCI artifacts. Select a repository with OCI enabled, then lint, package, and push the example through the `rvs` Helm wrapper:

```bash
rvs art select acme/deployment-charts
rvs helm lint .
rvs helm package .
rvs helm push ravenstash-example-1.0.0.tgz charts
```

Helm appends the chart name and version, producing this reference:

```text
oci://oci.rvsta.sh/acme/deployment-charts/charts/ravenstash-example:1.0.0
```

Inspect or install the exact version through the same target:

```bash
rvs helm show chart charts/ravenstash-example --version 1.0.0
rvs helm upgrade --install example charts/ravenstash-example --version 1.0.0
```

The wrapper provides temporary registry access. Ravenstash does not expose a classic `index.yaml` chart repository.

See [Publish and install Helm OCI charts](https://docs.ravenstash.com/helm/publish-and-install/).
