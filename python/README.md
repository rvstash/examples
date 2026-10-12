# Python / PyPI

This is a minimal Python package built with Hatchling. Select a Ravenstash repository with PyPI enabled, build the distributions, and publish through the `rvs` uv wrapper:

```bash
rvs art select acme/packages
rvs uv build
rvs uv publish
```

`rvs uv publish` discovers the upload endpoint, supplies a temporary credential, and asks you to confirm the destination and files. It does not write a token or Ravenstash index URL into `pyproject.toml`.

Verify the exact version from a clean environment:

```bash
rvs pip install ravenstash-example==1.0.0
python -c 'from ravenstash_example import registry_greeting; print(registry_greeting())'
```

You can also publish the built files with Twine:

```bash
rvs twine upload dist/*
```

See [Publish Python packages](https://docs.ravenstash.com/pypi/publish/) and [Install Python packages](https://docs.ravenstash.com/pypi/install/).
