mydict ={
    'ke1' : 10,
    'ke32':20
}


mydict2 = {
    'k41':"revathi",
    'k32':"suma"
}

mydict3 = {
    'k341':"ssss",
    'k872':"hhhh"
}

dic3 = {}


for dic in (mydict,mydict2,mydict3):
    dic3.update(dic)


print(dic3)