from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.ibge.gov.br/estatisticas/economicas/industria/9294-pesquisa-industrial-mensal-producao-fisica-brasil.html?=&t=resultados'
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")
#print(soup.prettify()) 

data = {}
table = soup.find("div", attrs={"class": "table__scroll__container"})
#table_data = table.tbody.find_all("td")  
print (table)
headings = []
'''
for row in table.findAll('tr'):
    cells = row.findAll('td')


for td in table_data[0].find_all("td"):    
    headings.append(td.b.text.replace('\n', ' ').strip())
    
for table, heading in zip(table_data[1].find_all("table"), headings):
    t_headers = []
    for th in table.find_all("th"):
        t_headers.append(th.text.replace('\n', ' ').strip())
            
    table_data = []
    for tr in table.tbody.find_all("tr"):
        t_row = {}
        for td, th in zip(tr.find_all("td"), t_headers): 
            t_row[th] = td.text.replace('\n', '').strip()
        table_data.append(t_row)
    data[heading] = table_data
    
for topic, table in data.items():
    with open(f"{topic}.csv", 'w') as out_file:
        headers = [ 
            "planilha1",
            "planilha2",
            "planilha3",
            'planilha4'
        ] 
        writer = csv.DictWriter(out_file, headers)
        writer.writeheader()
        for row in table:
            if row:
                writer.writerow(row)
'''