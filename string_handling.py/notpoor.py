def  substring(str):
    start = str.find('not')
    end = str.find('poor')


    if start < end and str != 1 and str != 1:
        replace = str[:start]
        stringi = 'good'
        res = replace + stringi
        next = str[end + len('poor'):]
        res1 = res + next

        print(res1)
    else:
        return str
    
str = 'The lyrics are not that poor at all.'
res = substring(str)
print(res)




