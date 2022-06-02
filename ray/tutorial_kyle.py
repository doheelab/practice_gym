import ray
import datetime
import time

print(ray.__version__)
# 1.0.1.post1


def print_current_datetime():
    time.sleep(0.3)
    current_datetime = datetime.datetime.now()
    print(current_datetime)
    return current_datetime


ray.init()

# Ray Task
@ray.remote
def print_current_datetime():
    time.sleep(0.3)
    current_datetime = datetime.datetime.now()
    print(current_datetime)
    return current_datetime


# print_current_datetime()
print_current_datetime.remote()

ray.get(print_current_datetime.remote())
futures = [print_current_datetime.remote() for i in range(4)]

ray.get(futures)
