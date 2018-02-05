from bs4 import BeautifulSoup
html_sample=''
soup=BeautifulSoup(html_sample,'html.parser')
print(soup.text)