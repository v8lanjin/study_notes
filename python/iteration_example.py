#iteration_example.py
string = "hello"
itr = iter(string)
print(next(itr))

# if go to the end of iter, it will throw StopIteration exception
# __iter__ __next__