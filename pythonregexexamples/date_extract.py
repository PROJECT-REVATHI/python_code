import re

pattern = re.compile(r'/(\d{4})/(\d{2})/(\d{2})/')  # Fixed regex
url = 'https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/'
match = re.findall(pattern, url)

print(match)
