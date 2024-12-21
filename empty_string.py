def filter_empty_string(strings):

    def non_empty_str(strings):
        return strings.strip() != ""
    
    filtering = list(filter(non_empty_str,strings))

    return filtering
    
strings = ['revathi','suma','sridhar'," ",'','']
res = filter_empty_string(strings)
print(res)
