from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Current memory address and the length in elements of the buffer: "+str(array_num.buffer_info()))
print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))
