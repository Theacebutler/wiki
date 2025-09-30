import wikipediaapi
from sys import argv

try:
    q = argv[1] 
except IndexError as e:
    q = 'wikipedia'

cli = wikipediaapi.Wikipedia('codeMaster', extract_format=wikipediaapi.ExtractFormat.HTML)

response = cli.page(q)

page = response.text if response.exists() else 'Page dons not exists'

with open(f'responses/{q}.html', 'w', encoding='utf-8') as file:
    file.write(str(page))