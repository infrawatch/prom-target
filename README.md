# prom-target

Simple script to generate fake prometheus metrics

## Usage

```
$ ./prom-target.py &
[1] 3475808
Listening on port 8000 to serve 10000 total metrics

$ curl http://localhost:8000
127.0.0.1 - - [07/Dec/2022 17:47:11] "GET / HTTP/1.1" 200 -
#Mock Prometheus metrics
mock_metric_0{labelA="0",labelB="0"} 1
mock_metric_0{labelA="1",labelB="0"} 2
[...]

$ kill %%
[1]+  Terminated              ./prom-target.py -m 1000 -l 10
```

## Container

```
$ podman build -t prom-target .
[...]

$ podman run --name target1 -d -p 8000:8000 prom-target -m 100 -l 5
6bfe29b1fb6e720d0a72cf64a931101d65286825f8e2eceef2419b2f1646135c

$ curl localhost:8000                                                               
#Mock Prometheus metrics                                                                                                  
mock_metric_0{labelA="0",labelB="0"} 1                                  
mock_metric_0{labelA="1",labelB="0"} 2          
[...]

$ podman rm -f target1
6bfe29b1fb6e720d0a72cf64a931101d65286825f8e2eceef2419b2f1646135c
```
