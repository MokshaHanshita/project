import os 
file1="A:\python_W\Swapping-file\sample1.txt"
file2="A:\python_W\Swapping-file\sample2.txt"
def swapFileData():


    with open (file1, 'r') as a:
        data_a = a.read()
    with open (file2, 'r') as b:
        data_b = b.read()
    with open(file1,'w') as a:
        a.write(data_b)

    with open(file2,'w') as b:
        b.write(data_a)
         
    print("Task completed")

swapFileData()
