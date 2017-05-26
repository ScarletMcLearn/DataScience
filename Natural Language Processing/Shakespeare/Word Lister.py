# file_name = input("Please enter the name of the file to listify: ")
#
# option = input("Do you want to: \n1) Read (r) \n2) Write (w) \n3) Append (a): ")
#
# # option = 'a'
#
# file = open(file_name, option)
#
# if (option == 'r'):
#     file = open(file_name, option)
#
# elif (option == 'r'):
#


print("Opened File")

file = open('test1.txt', 'r')

# words = file.read()

print("Reading And Cleaning File")

words = file.readlines()


words = [word.rstrip("\n") for word in words]

# print(words)

file.close()

print("Writing New File")

file = open('listied.txt', 'w')

file.write(str(words))

file.close()

print(words)

print("Done!")
