from concurrent.futures import ThreadPoolExecutor, wait, as_completed, ALL_COMPLETED, FIRST_COMPLETED
import time


def task_func(id, sec):
    print("task {} begin".format(id))
    time.sleep(sec)
    print("task {} finished in {} s".format(id, sec))
    return sec


executor = ThreadPoolExecutor(max_workers=2)

# time_arr = [3, 2, 4]
time_arr = [2, 1, 3, 4]
all_tasks = [executor.submit(task_func, id, sleeptime) for id, sleeptime in enumerate(time_arr)]

# wait(all_tasks, return_when=FIRST_COMPLETED)
# wait(all_tasks, return_when=ALL_COMPLETED)
# print('main goes on')

try:
    for future in as_completed(all_tasks, timeout=3):
        print(future.result())
except Exception as e:
    print("as_completed timeout: {}".format(e))

for t in all_tasks:
    print(t.done())
