# Delay ray.get()

import time


def do_some_work(x):
    time.sleep(1)  # Replace this with work you need to do.
    return x


start = time.time()
results = [do_some_work(x) for x in range(4)]
print("duration =", time.time() - start, "\nresults = ", results)

# Now, let’s parallelize the above program with Ray.

import time
import ray

ray.init(num_cpus=4)  # Specify this system has 4 CPUs.


@ray.remote
def do_some_work(x):
    time.sleep(1)  # Replace this is with work you need to do.
    return x


# We measure only the time it takes to invoke the tasks, not their running times, and we get the IDs pf the results corresponding to the four tasks.
start = time.time()
results = [do_some_work.remote(x) for x in range(4)]
print("duration =", time.time() - start, "\nresults = ", results)

# no speedup!
# start = time.time()
# results = [ray.get(do_some_work.remote(x)) for x in range(4)]
# print("duration =", time.time() - start, "\nresults = ", results)

# To enable parallelism, we need to call ray.get() after invoking all tasks.
start = time.time()
results = ray.get([do_some_work.remote(x) for x in range(4)])
print("duration =", time.time() - start, "\nresults = ", results)
