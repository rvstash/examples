# Maven

This is a minimal Java library. Select a Ravenstash repository with Maven enabled, then deploy it through the `rvs` wrapper:

```bash
rvs art select acme/packages
rvs mvn verify
rvs mvn deploy
```

`rvs mvn` injects temporary repository settings and credentials for the selected target. The project therefore needs no Ravenstash URL in `pom.xml` and no token in a committed or user-level `settings.xml`.

Verify the exact version by resolving it through the same selected target:

```bash
rvs mvn dependency:get -Dartifact=com.acme:ravenstash-example:1.0.0
```

See [Publish Maven artifacts](https://docs.ravenstash.com/maven/publish/) and [Resolve Maven artifacts](https://docs.ravenstash.com/maven/install/).
