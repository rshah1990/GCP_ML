## What is Containers

- Historically to deploy solution we use to have dedicated servers which means waste of resources, scaling was difficult, not portable. For ex: database will be deployed on one VM, when queries are not running or partially used the resources are wasted
- **Virtualization**: run multiple virtual serves on same physical computer. Hypervisor is software layer which breaks dependencies OS with hardware so that multiple virtual machine to share same hardware. Disadvantages of the historic system has been removed but still application is tightly coupled with application and its dependencies
- To resolve issue of dependency problem is to abstract at user space level which is nothing but containers. **Containers are isolated user spaces to run application code**
