# First Deployment
Here we will perform our first deployment on DC/OS.  We will be starting with the traditional "Hello ~~World~~ Marathon".  This will be a simple service that simply prints 'Hello Marathon' to stdout and sleeps for 5 seconds, in an infinite loop.  (The code was sourced from <https://dcos.io/docs/1.8/usage/marathon/application-basics/>)

## Application Definition
    {
        "id": "hello-marathon", 
        "cmd": "while [ true ] ; do echo 'Hello Marathon' ; sleep 5 ; done",
        "cpus": 0.1,
        "mem": 10.0,
        "instances": 1
    }
## Prerequisites
You should have performed the following steps:
- Deployed an ACS cluster with DC/OS as the orchestrator
- Created an SSH Tunnel into the master node
- Installed the DC/OS CLI

You can follow the instructions here for steps 1 & 2: [Installing ACS with DCOS](http://www.deveducate.com/Module/1015).  For step 3, the CLI can be installed via the DC/OS UI.

## Deploy via Marathon UI
Perform the following steps to deploy Hello Marathon via the Marathon UI<br/>
1. Open a browser to <http://localhost:8080/#/services/>.  This is the DC/OS UI.  You should see 'No Services Deployed' like below:
![No Services Deployed](https://raw.githubusercontent.com/robbagby/dcos-primer/master/images/dcos-no-services.jpg)
2. Open a browser to <http://localhost:8080/marathon><br/>
3. Click on 'Create Application'
![Create Application](https://raw.githubusercontent.com/robbagby/dcos-primer/master/images/marathon-create-application.jpg)
4. Click on JSON Mode in the upper right corner and paste in the hello-marathon application definition above.
![Create Hello Marathon](https://raw.githubusercontent.com/robbagby/dcos-primer/master/images/marathon-new-hello-marathon.jpg)
5. Click 'Create Application'  
6. You should see the app initially listed as 'Deploying' then 'Running'

## View the logs
In order to see the output of our Hello Marathon, complete the following steps:<br/>
1. Open a browser to <http://localhost:8080/#/services/><br/>
2. Click on the 'hello-marathon' service
![Create Hello Marathon](https://raw.githubusercontent.com/robbagby/dcos-primer/master/images/dcos-list-hello-marathon.jpg)
3. Click on the 'Tasks' tab and the specific task 
![Click on Task](https://raw.githubusercontent.com/robbagby/dcos-primer/master/images/dcos-hello-task.jpg)
4. Click on the 'Logs' tab.  You should see the following:
![Logs](https://raw.githubusercontent.com/robbagby/dcos-primer/master/images/dcos-hello-marathon-logs.jpg)

## Destroy the app
We have deployed the app via the Marathon UI.  Let's destroy it so we can deploy it via the DC/OS CLI.<br/>
1. Open a browser to <http://localhost:8080/#/services/><br/>
2. Click on the up arrow next to the hello-world service and choose 'Destroy'
![Destroy Service](https://raw.githubusercontent.com/robbagby/dcos-primer/master/images/dcos-destroy-hello.jpg)
3. Click on the 'Destroy Service' button.

## Deploy via DC/OS CLI
_It is likely important to note that you must have opened an SSH tunnel to the master node, as well as installed the DC/OS CLI._

In order to deploy the Hello Marathon service via the DC/OS CLI, perform the following steps:<br/>
1. Either create a new file named 'hello-marathon.json' and paste in the hello-marathon application definition or, if you have cloned this repo, find the location of this file: dcos-primer\marathon\ <br/>
2. Open a cmd prompt<br/>
3. Navigate to the directory containing 'hello-marathon.json'.  On my machine it is: C:\Development\Technologies\DCOS\dcos-primer\marathon    

```cd C:\Development\Technologies\DCOS\dcos-primer\marathon```<br/><br/>
4. Type the following to login

```dcos auth login```<br/><br/>
You should see a 'Login successful!' message<br/><br/>
5. Type the following to deploy the app

```dcos marathon app add hello-marathon.json```<br/><br/>
You should see a message that states: 'Created deployment someguid'<br/><br/>
6. Validate that the service is running like above
