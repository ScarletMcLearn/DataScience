# # # # updater.py
# # # # import time
# # # # from datetime import datetime
# # # # from shared import shared_variable

# # # # def update_variable():
# # # #     global shared_variable  # Add this line to access the global variable
# # # #     while True:
# # # #         # Update the shared variable
# # # #         shared_variable = datetime.now().strftime("%Y-%m-%d %I:%M %p")
# # # #         time.sleep(120)  # Sleep for 1 second before updating again

# # # # # Start updating the variable
# # # # update_variable()


# # # import time
# # # from datetime import datetime
# # # from shared import shared_variable

# # # def update_variable():
# # #     while True:
# # #         # Update the shared variable
# # #         with shared_variable.get_lock():
# # #             shared_variable.value = datetime.now().strftime("%Y-%m-%d %I:%M %p") #time.time()
# # #         time.sleep(60)  # Sleep for 1 second before updating again

# # # # Start updating the variable
# # # update_variable()


# # # updater.py
# # import time
# # from datetime import datetime
# # from multiprocessing import Manager

# # def update_variable(shared_dict):
# #     while True:
# #         # Update the shared variable
# #         shared_dict['shared_variable'] = datetime.now().strftime("%Y-%m-%d %I:%M %p")
# #         time.sleep(1)  # Sleep for 1 second before updating again

# # # Create a shared namespace using Manager
# # manager = Manager()
# # shared_dict = manager.dict()

# # # Start updating the variable
# # update_variable(shared_dict)

# # updater.py
# import time
# from datetime import datetime
# from shared import shared_dict, shared_lock

# def update_variable():
#     while True:
#         # Update the shared variable
#         shared_lock.acquire()
#         try:
#             shared_dict['shared_variable'] = datetime.now().strftime("%Y-%m-%d %I:%M %p")
#         finally:
#             shared_lock.release()
#         time.sleep(1)  # Sleep for 1 second before updating again

# # Start updating the variable
# update_variable()


# updater.py
import time
from datetime import datetime
from multiprocessing import Queue

def update_variable(queue):
    while True:
        # Update the shared variable
        shared_variable = datetime.now().strftime("%Y-%m-%d %I:%M %p")
        queue.put(shared_variable)
        time.sleep(1)  # Sleep for 1 second before updating again

# Create a queue for interprocess communication
queue = Queue()

# Start updating the variable
update_variable(queue)
