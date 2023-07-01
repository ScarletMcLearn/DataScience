import time
# from datetime import datetime
from Utils.Utilities import generate_shared_data
import datetime
# import pickle
# import json



# Define the interval (in seconds) for updating the data
update_interval = 180  # Update every 3 minutes


# fname = 'temp ' + datetime.datetime.now().date().isoformat()  + ' shared_data.json'
c = 0

print('Running Data Generation')

while True:
    c = c + 1
    now = datetime.datetime.now()
    formatted_datetime = now.strftime("%y-%m-%d %I:%M:%S %p")
    print('Iteration number: ', str(c), '- Time: ', formatted_datetime)
    all_tr = generate_shared_data()
    # # Store the data in a shared location, such as a file or a database
    # # For simplicity, let's assume a file named 'shared_data.txt'
    # with open(fname, 'w') as file:
    #     file.write(str(all_tr))

    # serialized_data = pickle.dumps(all_tr)
    # Store the serialized data in a shared location, such as a file or a database
    # For simplicity, let's assume a file named 'shared_data.pkl'
    # with open(fname, 'wb') as file:
    #     pickle.dump(all_tr, file)
    # Convert the data to a JSON string
    # json_data = json.dumps(all_tr, default=str)

    # # Store the JSON string in a shared location, such as a file or a database
    # with open(fname, 'w') as file:
    #     file.write(json_data)

    time.sleep(update_interval)




# Define the interval (in seconds) for updating the data
# update_interval = 180  # Update every 3 minutes

# shared_data = None

# def update_shared_data():
#     global shared_data
#     shared_data = get_all_data()

# while True:
#     update_shared_data()
#     time.sleep(update_interval)