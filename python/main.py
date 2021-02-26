import threading
import time
import locking_stack
import stack


def thread_function(tmp_stack, index):
    for i in range(1000000):
        tmp_stack.push(index)
        tmp_stack.pop()


if __name__ == "__main__":
    tmp_stack = stack.Stack()
    threads_x = list()
    for index in range(5):
        x = threading.Thread(target=thread_function, args=(tmp_stack, index))
        threads_x.append(x)
        x.start()
    for thread in threads_x:
        thread.join()
    print(tmp_stack.items)

    tmp_locking_stack = locking_stack.LockingStack()
    threads_y = list()
    for index in range(5):
        y = threading.Thread(target=thread_function(tmp_locking_stack, index))
        threads_y.append(y)
        y.start()
    for thread in threads_y:
        thread.join()
    print(tmp_locking_stack.items)
# from datetime import time
#
# from tornado import concurrent
# import time
#
# class FakeDatabase:
#     def __init__(self):
#         self.value = 0
#
#     def update(self):
#         local_copy = self.value
#         local_copy += 1
#         time.sleep(0.1)
#         self.value = local_copy
#
#
# if __name__ == "__main__":
#     database = FakeDatabase()
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         for index in range(2):
#             executor.submit(database.update)
#     print(database.value)
