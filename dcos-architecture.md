# Default Architecture
Before going into deployment specifics, it is important to understand the default DC/OS architecture in Azure - at least at a high level.  Below is a visual of the default architecture:

![Default DC/OS Architecture](https://raw.githubusercontent.com/robbagby/dcos-primer/master/images/dcos-reference-architecture.jpg)

The first thing to notice is that there are 3 subnets in the same private vnet.  Each of these subnets has it's own responsibility and the way you communicate with each differs.  The following are high-level details of each.
## Master subnet
The master subnet contains the master VMs that you communicate with to deploy and manage workloads to both the public and private agents.  In DC/OS, the masters expose HTTP endpoints locally.  For this reason, you have to create an SSH tunnel to the master.  For more details on how to SSH into the master, see: [Installing ACS with DCOS](http://www.deveducate.com/Module/1015).

The master subnet does have a load balancer sitting in front of the master VM(s).  The LB, however, does not have any Load Balancing Rules.  It does have inbound NAT rules that allow you to create the SSH tunnel to port 22 on each Master.  A Network Security Group that is associated with the NIC for each Master VM enforces that only the SSH ports are reachable.

The net-net is that in order to manage the DC/OS cluster, you will have to open an SSH tunnel into a master node.  Once that tunnel is created, you can then manage the  DC/OS cluster from your local system.  For example, you can access the DC/OS web interface via <http://localhost:8080> and the Marathon web interface via <http://localhost:8080/marathon>.
## Public agent subnet
The public agent subnet contains a VM ScaleSet of publicly accessible nodes.  There is a load balancer sitting in front of the VMSS with load balancing rules set up ofr ports 80, 443 and 8080, by default.  There is also a Network Security Group associated with this subnet that opens up access to these ports.

 It is important to note that there are no inbound NAT rules defined.  As such, you cannot SSH into the public agent nodes directly.  In order to SSH into these nodes, you can SSH into the master and from there SSH into the agent nodes.  Again, for more information on how to do this see  [Installing ACS with DCOS](http://www.deveducate.com/Module/1015).

Only applications deployed to the public agent pool are publicly accessible  However, you should **not** deploy most workloads to the public agents.  The intended pattern is to deploy load balancers such as HAProxy or Marathon-lb (which sits on top of HAProxy) in this pool and they expose services running in the internal agent pool.
## Private agent subnet
The private agent subnet contains a VM ScaleSet of internally accessible nodes.  As noted above, most workloads should be deployed in the private agent pool.  They can be exposed to the outside world or other services via LBs such as Marathon-lb.

There is no Load Balancer in this subnet.  The Network Security Group associated with this subnet only allows traffic from other nodes within the virtual network (through the default rules).

## Summary
In order to deploy workloads into a DC/OS cluster (unless you open it up), you will first need to create an SSH tunnel into the master node.  Once that tunnel is established, you can deploy your workloads (more about this next) to either the public agent pool or the private agent pool.  The suggested pattern is to deploy most workloads into the private agent pool.  If any services need to be publicly accessible, a load balancer such as HAProxy or Marathon-lb can be deployed into the public pool and expose those services.