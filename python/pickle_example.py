import pickle

my_list = ["hello", "world", 123, True, 3.1415926]
pickleFile = open('pickle_store.pkl', 'wb')
pickle.dump(my_list, pickleFile)
pickleFile.close()

pickleFile2 = open('pickle_store.pkl', 'rb')

my_list2 = pickle.load(pickleFile2)
print(my_list2)
pickleFile2.close()