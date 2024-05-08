# my_tuple = (i ** 2 for i in range(1, 10))
#
# for i in my_tuple:
#     print(i)

def my_generator():
    yield 1
    yield 2
    yield 3


arr1 = ['one', 'two', 'three']
arr2 = [1, 2, 3]

my_gen = {key: value for key, value in zip(arr1, arr2)}
print(my_gen)
