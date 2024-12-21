try:
    pro = int(input("enter no:"))
    print("input %s" %(pro))
except KeyboardInterrupt:
    print("keyboard error")
finally:
    
    print("this is final block")
