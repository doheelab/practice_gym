import time


def tiny_work(x):
    time.sleep(0.0001)  # Replace this with work you need to do.
    return x


start = time.time()
results = [tiny_work(x) for x in range(100000)]
# 13.36 secs
print("duration =", time.time() - start)

# make every invocation of do_some_work() remote
import time
import ray

ray.init(num_cpus=4)


@ray.remote
def tiny_work(x):
    time.sleep(0.0001)  # Replace this is with work you need to do.
    return x


start = time.time()
result_ids = [tiny_work.remote(x) for x in range(100000)]
results = ray.get(result_ids)
# 27 secs
print("duration =", time.time() - start)


# make the remote tasks larger in order to amortize the invocation overhead
# we aggregate 1000 tiny_work() function calls in a single bigger remote function, mega_work()

import time
import ray

ray.init(num_cpus=4)


def tiny_work(x):
    time.sleep(0.0001)  # replace this is with work you need to do
    return x


@ray.remote
def mega_work(start, end):
    return [tiny_work(x) for x in range(start, end)]


start = time.time()
result_ids = []
[result_ids.append(mega_work.remote(x * 1000, (x + 1) * 1000)) for x in range(100)]
results = ray.get(result_ids)
print("duration =", time.time() - start)
