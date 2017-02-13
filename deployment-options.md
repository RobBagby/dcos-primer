# Deployment Options Services
You have a multitude of options when it comes to deploying services to a DC/OS Cluster.  Some (but not all) of these include:
- The DC/OS Universe
- The Marathon UI
- The DC/OS CLI
- The Marathon REST API<br/>
## DC/OS Universe
The DC/OS universe is intended to be an app store experience for deploying open source and partner offerings into your cluster.  Remember that the UI is only exposed via a local HTTP endpoint and requires you to open an SSH Tunnel.  For more information review [dcos architecture](https://github.com/RobBagby/dcos-primer/blob/master/dcos-architecture.md).

![DC/OS Universe](https://github.com/robbagby/dcos-primer/raw/master/images/dcos-universe.jpg)

The above image shows the Universe UI exposed in the DC/OS UI (http://localhost:8080/#/universe/packages/). 	As you can see, you simply search for the offering you are interested in and choose 'Install Package'.  You can then choose to deploy with default settings ('Install Package' again) or perform an 'Advanced Installation'.  _You can  deploy packages from the universe via the following methods, as well._
## Marathon UI
Marathon provides a web UI where you can manage applications: (http://localhost:8080/marathon/ui).  _As before, this requires an SSH tunnel to be opened._

![DC/OS Universe](https://github.com/robbagby/dcos-primer/raw/master/images/marathon-create-application.jpg)

When you click on 'Create Application', you are presented with a UI that allows you to add a new application.  You can choose between the default tabbed UI or JSON mode.  I would highly urge you to use JSON mode as not everything can be managed via the non-JSON UI.

<img src="https://github.com/robbagby/dcos-primer/raw/master/images/marathon-new-app-nonjson.jpg" alt="New Application" style="width: 400px;height: 300px"/>
<img src="https://github.com/robbagby/dcos-primer/raw/master/images/marathon-new-app-json.jpg" alt="New Application - JSON" style="width: 400px;height: 300px"/>

## DC/OS CLI
As with most operations activities, UIs are helpful, but a good percentage of the work is done in code.  From the [DC/OS CLI documentation](https://dcos.io/docs/1.8/usage/cli/): 
>You can use the DC/OS command-line interface (CLI) to manage your cluster nodes, install DC/OS packages, inspect the cluster state, and administer the DC/OS service subcommands. 

You can install the CLI from the DC/OS UI.  See below:
![Install DC/OS CLI](https://github.com/robbagby/dcos-primer/raw/master/images/install-dcos-cli.jpg)

As mentioned above, you can manage a variety of aspects of your cluster with the CLI.  Here, I will briefly introduce 3 commands:

### dcos auth login
This command allows you to authenticate to a dc/os cluster.  Once you have an SSH tunnel established to a master node, you simply run the dcos auth login command and you will be authenticated.

    dcos auth login

### dcos marathon app add
This command allows you to deploy an application to DC/OS.

    dcos marathon app add [<app-resource>]

### dcos package 
This command allows you to install and manage software packages from the a DC/OS package repository.

    dcos package install [--cli | [--app --app-id=<app-id>]]
                                 [--package-version=<package-version>]
                                 [--options=<file>]
                                 [--yes]
                                 <package-name>                         
## Marathon REST API
Marathon is one of the frameworks available for DC/OS.  It exposes a REST API for starting, stopping and scaling applications. As with the other options, the marathon REST API is exposed via http://localhost:local-port.  For example, if you are tunneling on port 8080, Marathon endpoints begin with  <http://localhost:8080/marathon/v2/>.

We won't be using the REST API in this primer, but I did want to introduce it.  
                         
                         