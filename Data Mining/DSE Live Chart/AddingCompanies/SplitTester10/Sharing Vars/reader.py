# # # # # # reader.py
# # # # # from shared import shared_variable

# # # # # # Access the shared variable
# # # # # print(shared_variable)

# # # # from shared import shared_variable
# # # # import time

# # # # # Access the shared variable
# # # # while True:
# # # #     with shared_variable.get_lock():
# # # #         value = shared_variable.value
# # # #     print(value)
# # # #     time.sleep(1)  # Sleep for 1 second before reading again


# # # # reader.py
# # # from shared import shared_dict
# # # import time

# # # # Access the shared variable
# # # while True:
# # #     shared_variable = shared_dict.get('shared_variable')
# # #     print(shared_variable)
# # #     time.sleep(1)  # Sleep for 1 second before reading again


# # # reader.py
# # from shared import shared_dict, shared_lock
# # import time

# # # Access the shared variable
# # while True:
# #     shared_lock.acquire()
# #     try:
# #         shared_variable = shared_dict.get('shared_variable')
# #         print(shared_variable)
# #     finally:
# #         shared_lock.release()
# #     time.sleep(1)  # Sleep for 1 second before reading again


# # reader.py
# from multiprocessing import Queue

# # Access the shared variable
# while True:
#     shared_variable = Queue.get()
#     print(shared_variable)
#     time.sleep(1)  # Sleep for 1 second before reading again

# reader.py
from multiprocessing import Queue

# Create a queue for interprocess communication
queue = Queue()

# Access the shared variable
while True:
    shared_variable = queue.get()
    print(shared_variable)
    time.sleep(1)  # Sleep for 1 second before reading again
