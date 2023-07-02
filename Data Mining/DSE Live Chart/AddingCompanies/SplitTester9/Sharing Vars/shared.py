# # # # shared.py
# # # shared_variable = None

# # from multiprocessing import Value

# # shared_variable = Value('d', 0.0)  # 'd' denotes the data type (double)

# # shared.py
# from multiprocessing import Manager

# # Create a shared namespace using Manager
# manager = Manager()
# shared_dict = manager.dict()


# shared.py
from multiprocessing import Manager

# Create a shared namespace using Manager
manager = Manager()
shared_dict = manager.dict()
shared_lock = manager.Lock()
