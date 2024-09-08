from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup as bs

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

i: int = 0

for i in range(0, 100, 10):
    url = f'https://ar.indeed.com/jobs?q=desarrollador&l=Argentina&sort=date&start={i}&vjk=aac382d01f8ed494'
    driver.get(url)
    soup = bs(driver.page_source, 'html.parser')
    elementos = soup.find('ul',class_="css-zu9cdh eu4oa1w0").find_all('li')
    print(elementos)
    with open('links.pdf', 'a', encoding='utf-8') as file:
        for i in elementos:
            try:
                if "backend" in i.text.lower() or "python" in i.text.lower():
                    file.write(f"Puesto: {i.find('a').text.strip()}\t|\tEmpresa: {i.find('span', class_= 'css-63koeb eu4oa1w0').text.strip()}\n")
                    file.write(f"Link: https://ar.indeed.com{i.find('a')['href']}\n\n")
            except Exception as e:
                print(e)