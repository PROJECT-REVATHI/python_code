def length_extract(words):
    def length_extract(words):
        return len(words) > 5
    filtering = list(filter(length_extract,words))
    return filtering
    

words = ['revathi','sumaa','sridhar','srikanth','suma']

res = length_extract(words)
print(res)