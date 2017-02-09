# Learn DC/OS on ACS
Learn DC/OS on Azure Container Service.  This is intended to be a hands-on guide to learning the essentials for deploying containerized workloads on DC/OS in ACS.  Following the guides in this repo, you will:
- Gain a high-level understanding of the DC/OS Architecture in ACS
- Understand how to deploy workloads via: the Universe, the Marathon UI and the DC/OS CLI 
- Understand how to take advantage of marathon-lb to load balance and expose a public web app
- Understand how to take advantage of marathon-lb to load balance a private web api
- Understand the mechanics of service discovery with marathon-lb

## Prerequesites
- It is assumed that you have deployed an ACS cluster with DC/OS as the orchestrator
- The examples in these guides have 1 master, 3 private agents
- The examples assume that you are running on Windows 10 with Docker for Windows installed.  _You could certainly adapt the examples to Linux or OSX_
- The examples assume that you have established an SSH Tunnel to the master node

**The following video will show you how to Deploy an ACS Cluster with DC/OS and create an SSH Tunnel from Windows: [Installing ACS with DC/OS](http://www.deveducate.com/Module/1015)

## Index
[DC/OC Architecture Overview](https://github.com/RobBagby/dcos-primer/blob/master/dcos-architecture.md)<br/>
[Deployment Options](https://github.com/RobBagby/dcos-primer/blob/master/deployment-options.md)<br/>
[Deploy Your First Appp](https://github.com/RobBagby/dcos-primer/blob/master/deploy-first-app.md)<br/>
[Deploy a Load Balanced Web App](https://github.com/RobBagby/dcos-primer/blob/master/deploy-loadbalanced.md)<br/>
[Deploy a More Complex Topology](https://github.com/RobBagby/dcos-primer/blob/master/deploy-web-and-private-webapi.md)
