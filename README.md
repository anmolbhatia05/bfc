## Purpose
The aim of this repository is:
- to familiarise myself with [bfc (bridging function chain)](https://github.com/epi-project/Netsoft2023)
- to prepare bfc for [brane](https://github.com/epi-project/brane) integration

The bfc is built on top of a socksx proxy implemented [here](https://github.com/epi-project/socksx)

### Network functions
These functions are docker containers that have a unique network purpose, for example - to act as a proxy, to encrypt traffic, to decrypt traffic, to act as a firewall. Location - `functions` folder

### Kubernetes files
These functions are deployed into a K8s cluster. The kube files (deployment and service) can be found in the `kube` folder.
