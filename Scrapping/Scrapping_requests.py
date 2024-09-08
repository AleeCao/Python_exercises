import requests as rs
from bs4 import BeautifulSoup as bs
jobs = ['python', 'backend', 'developer', 'programmer', 'programador', 'desarrollador', 'nodejs', 'node.js', 'node', 'django', 'flask', 'fastapi', 'api', 'rest', 'restful']

for job in jobs:
    ok = True
    print(f"Buscando {job}...\n")
    while ok:
        try:
            url = f'https://es.linkedin.com/jobs/desarrollo-web-empleos?keywords=Desarrollo%20Web&location=Espa%C3%B1a&geoId=105646813&f_TPR=r604800&f_E=1%2C2&position=1&pageNum=0'
            head = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
            res = rs.get(url, headers=head)
            soup = bs(res.text, 'html.parser')
            elementos = soup.find('ul', class_= "jobs-search__results-list").find_all('li')
            with open('links.pdf', 'a', encoding='utf-8') as file:
                for i in elementos:
                    if "backend" in i.text.lower() or job in i.text.lower():
                        file.write(f"Puesto: {i.find('a').text.strip()}\t|\tEmpresa: {i.find('h4').text.strip()}\n")
                        file.write(f"Link: {i.find('a')['href']}\n\n")
            ok = False
        except Exception as e:
            pass