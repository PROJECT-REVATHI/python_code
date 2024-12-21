def substring_extracting(strings,substring):
    def containing_substring(strings):
        return substring in strings
    

    filtering = list(filter(containing_substring,strings))

    return filtering
    

strings = ['revathi','suma','srinu','mumma','mat']
substring = 'm'
res = substring_extracting(strings,substring)
print(res)