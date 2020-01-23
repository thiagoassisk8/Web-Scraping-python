import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

try:
    site_url = requests.get('https://www.ibge.gov.br/estatisticas/economicas/industria/9294-pesquisa-industrial-mensal-producao-fisica-brasil.html?=&t=resultados').text
except HTTPError as e:
    print(e)
except URLError as e:
    print("o Servidor não foi encontrado!")
        
soup = BeautifulSoup(site_url,'lxml')
print(soup.prettify())

minha_tabela = soup.find('table',{'class':'pvtTable'})
print(minha_tabela)





#indices_mensais = []
#links = minha minha_tabela.findall('div')
