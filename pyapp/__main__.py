from operator import contains
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import time
import random
from kubernetes import client, config

registry = CollectorRegistry()
config.load_incluster_config()



ti_1080 = Gauge('dsmlp_gpu', 'Number of GPUS in use',['hostname','type','status'],registry=registry)
def process_request():
    """A dummy function that takes some time."""
    v1 = client.CoreV1Api()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        if i.spec.containers[0].resources.requests is None:
            continue
        if 'cpu' in i.spec.containers[0].resources.requests:
            ti_1080.labels(i.metadata.name,"1080_ti",'reserve').set(i.spec.containers[0].resources.requests['cpu'].replace('m',''))

import time
if __name__ == '__main__':
    while True:
        process_request()
        #push_to_gateway('127.0.0.1:9091', job='GPUS', registry=registry)
        time.sleep(5)
