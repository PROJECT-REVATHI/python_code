def array_index_bound(arr,input):
    try:
        access =  arr[input]
        print("index element %s" %(access))
    except IndexError:
        print("index error")
    finally:
        print("finally block is executed")


    
arr = [1,2,3,4]
input = int(input("index the number"))
array_index_bound(arr,input)