# Technical decisions

Record at least 5 decisions. Include assumptions and limits.

## Decision
- Choice:
- Why:
- Alternative:
- Trade-off:
- Evidence / commit:
- Production improvement:

Cover your base image, health checks, networks, timeouts/retries, restart/resource settings,
storage and any other meaningful choices.

## Decision 01:
- Choice: Changed The USER parameter in Dockerfile to be non-root user
- Why: because, if the container compormised the attacker will have a low privlage so, he will not be able to execute dangerous commands
- Alternative: keeping the USER as Root
- Trade-off: the easiest is to leave the contianer with it's default root value but, this will lead to a big security flaw so, we make some effort creating another non-root user and make it executing the command
- Evidence / commit: 88a65a3449f3032066fd3fb13f15118450e2b92e
- Production improvement: This is used in production


## Decision 02:
- Choice: Made a Network Segmentation in frontend and backend networks (frontend (NGINX + app-01, app-02) and backend (apps + postgres + redis))
- Why: Isolates postgres and Redis from the outside world and blocks nginx from accessing them directly 
- Alternative: one default network for all the services
- Trade-off: if we used one default network for all the services it will be easy for a hacker to manipulate requests and deceive nginx to retrive sensitive data from Database services (which known as SSRF vulnerability)
- Evidence / commit: cfef474c5251455b1a504fd13d1faafa5227fa8e
- Production improvement: Use cloud network VPCs and apply firewall policies

## Decision 03:
- Choice: changed the /healthz path to the right one which is /health in docker-compose file services healthchecks
- Why: because, this is the wrong path which results in error 404
- Alternative: NONE
- Trade-off: NONE
- Evidence / commit: 89d8a6bd29e5921a19ffbfe90a82b9c7bb65f8c6
- Production improvement: Use HTTP/TCP liveness and readiness probes without container process forks

## Decision 04
- Choice: Used a named volume postgres-data and redis-data
- Why: Because, it guarantees database data survives when containers are destroyed or crashed 
- Alternative: Make bind-mounts
- Trade-off: Bind mounts suffer from cross-platform permission problems but, Docker managed named volumes manage permissions natively
- Evidence / commit: e0780beb2d8bd87d6c6dabb62fd7a5f15ee83ae0 , d33060e593ef1843951155164018cce8a5f59ddc
- Production improvement: Use a managed database services like AWS RDS with automated point-in-time recovery

## Decision 05
- Choice: Configured restart policy in docker compose to always on services.
- Why: Allows services to automatically recover from chrashed or OOM situations
- Alternative: make it restart: "no"
- Trade-off: If a bug causes crashing on startup, always can restart the containers and increase the service avaliability but, with no it still crashed until it is manually fixed
- Evidence / commit: ed4bd8e01b71f9951ef3ffe0ac7404afe5c77c57
- Production improvement: Kubernetes Deployments with ReplicaSets and Pod Autoscaling