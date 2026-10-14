# Ravenstash examples

Copyable projects and CI configurations for Ravenstash. The examples use [`rvs`](https://docs.ravenstash.com/cli/overview/) to run standard package and OCI clients with temporary credentials; they do not store registry tokens in project files.

| Workflow | Example |
| --- | --- |
| Python / PyPI | [`python/`](python/) |
| npm | [`npm/`](npm/) |
| Maven | [`maven/`](maven/) |
| Container images | [`container/`](container/) |
| Helm OCI charts | [`helm/`](helm/) |
| GitHub Actions | [`ci/github-actions/`](ci/github-actions/) |
| GitLab CI/CD | [`ci/gitlab/`](ci/gitlab/) |

## Before you start

Install `rvs` and the native tool used by the example:

```bash
curl -fsSL https://ravenstash.com/install.sh | bash
rvs --version
```

For interactive work, sign in, choose the account that owns the repository, and select the exact `namespace/repository` target:

```bash
rvs auth login
rvs account switch AcmeHQ
rvs art repo list
rvs art select acme/packages
rvs status
```

The selected repository must have the format required by the example: PyPI, npm, Maven, or OCI. Container images and Helm charts share one OCI format.

## Try the examples

Run commands from the corresponding example directory:

```bash
# Python
rvs uv build
rvs uv publish
rvs pip install ravenstash-example==1.0.0

# npm
rvs npm test
rvs npm pack --dry-run
rvs npm publish

# Maven
rvs mvn deploy
rvs mvn dependency:get -Dartifact=com.acme:ravenstash-example:1.0.0

# Container
rvs docker build -t acme/example:1.0.0 .
rvs docker push acme/example:1.0.0

# Helm OCI
rvs helm lint .
rvs helm package .
rvs helm push ravenstash-example-1.0.0.tgz charts
```

Publishing commands display the account, target, and content before asking for confirmation. Use `--rvs-yes` only in a guarded automation job.

## CI authentication

Create a narrowly scoped automation token owned by the same account or organization as the target repository. Store it as the masked CI secret `RVS_TOKEN`; never commit or log its value. The examples select the target and let `rvs` exchange that token for a short-lived package credential.

Replace `acme/packages` in the CI files with the exact target shown in Ravenstash. See the [GitHub Actions](https://docs.ravenstash.com/ci/github-actions/) and [GitLab CI/CD](https://docs.ravenstash.com/ci/gitlab-ci/) guides.

CI jobs install an exact `rvs` version so a new CLI release cannot change a pipeline unannounced. The CLI is pre-1.0 and can change commands between minor releases; raise the version deliberately after reading the [changelog](https://github.com/rvstash/ravenstash-cli/blob/main/CHANGELOG.md). GitHub Actions use [`rvstash/setup-ravenstash`](https://github.com/rvstash/setup-ravenstash), pinned to a full commit SHA. GitLab jobs use the portable installer with `RVS_INSTALL_VERSION`.

## Generated endpoints

You normally do not need to copy a URL: `rvs` discovers the endpoint for the selected target. The Ravenstash repository view shows generated endpoints when you need to configure a client that does not have an `rvs` wrapper.

Generated package endpoints use immutable namespace and repository references, for example:

```text
https://pypi.rvsta.sh/in/ar_23456789/simple/
https://npm.rvsta.sh/in/ar_23456789/
https://maven.rvsta.sh/in/ar_23456789/
```

OCI references use readable names and are refreshed by `rvs` after a rename:

```text
oci.rvsta.sh/acme/runtime-images/acme/example:1.0.0
```

Download and upload hosts remain separate for PyPI, npm, and Maven. OCI uses `oci.rvsta.sh` for both pulls and pushes.

## Documentation

- [Ravenstash quickstart](https://docs.ravenstash.com/getting-started/overview/)
- [Run native package tools through rvs](https://docs.ravenstash.com/cli/native-package-tools/)
- [PyPI quickstart](https://docs.ravenstash.com/pypi/quickstart/)
- [npm quickstart](https://docs.ravenstash.com/npm/quickstart/)
- [Maven quickstart](https://docs.ravenstash.com/maven/quickstart/)
- [Container quickstart](https://docs.ravenstash.com/container/quickstart/)
- [Helm OCI quickstart](https://docs.ravenstash.com/helm/quickstart/)

## License

The examples are available under the [MIT License](LICENSE).
