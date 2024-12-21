import re
def match_string(string):
    pattern = ('(\d{4})/(\d{2})/(\d{2})')
    match = re.findall(pattern,string)
    return match

print(match_string('https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/'))

