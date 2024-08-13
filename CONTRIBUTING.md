# Contributing to this repo

This repo contains evaluation apps for Torizon.

## Repo structure

Each directory contains one or more docker-compose files that will install and run an individual evaluation app on a Torizon OS system. Each directory must also contain a JSON file named `app.json` that governs what Uptane targets will be created for the Evaluation Apps package source in Torizon cloud. The structure of `app.json` is as follows:

```
{
    "packages": # An array of packages to be created. You can specify multiple packages here.
    [
        {
            "filename": "docker-compose.yml", # The filename of the docker-compose file, in the same directory
            "name": "Node-RED", # The name of the package to be created
            "icon": "icon.png", # (optional) An icon to display in Torizon cloud
            "version": "3.1.3", # The version of the package to be created
            "description": "README.md" # A markdown file describing the package, to display in Torizon Cloud
        }
    ]
}
```

## Delegation generation and signing

At present, the creation and signing of the Uptane metadata happens in a different pipeline, in a private repo.
