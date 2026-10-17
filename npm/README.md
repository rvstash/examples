# npm

This is a minimal scoped npm package. Select a Ravenstash repository with npm enabled, test and inspect the package, then publish through the `rvs` wrapper:

```bash
rvs art select acme/packages
rvs npm test
rvs npm pack --dry-run
rvs npm publish
```

The selected target determines the upload registry. `rvs` supplies a temporary credential and asks you to confirm the destination and package; no Ravenstash URL or token is stored in `package.json` or `.npmrc`.

pnpm works the same way through `rvs pnpm`:

```bash
rvs pnpm test
rvs pnpm publish --no-git-checks
```

Verify the exact version in a clean project:

```bash
rvs npm install @acme/ravenstash-example@1.0.0
rvs pnpm add @acme/ravenstash-example@1.0.0
```

pnpm 11 and later skip versions published less than a day ago when they resolve a range, so install a version you just published by its exact version.

See [Publish npm packages](https://docs.ravenstash.com/npm/publish/) and [Install npm packages](https://docs.ravenstash.com/npm/install/).
