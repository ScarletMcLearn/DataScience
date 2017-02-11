import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()

soup = bs.BeautifulSoup(sauce, "lxml")

# print(soup)

# print(soup.title)

# print(soup.title.name)

# print(soup.title.string)
# print(soup.title.text)


# print(soup.p)

# print(soup.find_all("p"))


# for paragraph in soup.find_all("p"):
#     print (paragraph.text)


# print(soup.get_text())



# for url in soup.find_all('a'):
#     # print(url)
#     # print(url.text)
#     print(url.get('href'))



nav = soup.nav

# print(nav.text)
# print(nav)


# for url in nav.find_all("a"):
#     print(url.get("href"))


body = soup.body

# for paragraph in body.find_all("p"):
#     print(paragraph.text)



# for div in soup.find_all("div"):
#     print(div.text)



# for div in soup.find_all("div", class_="body"):
#     print(div.text)



table = soup.table
table = soup.find('table')
# print(table)

table_rows = table.find_all('tr')

# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     print(row)



import pandas as pd
# import html5lib

# dfs = pd.read_html("https://pythonprogramming.net/parsememcparseface", header=0)
#
# for df in dfs:
#     print (df)




source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(source,'xml')

for url in soup.find_all('loc'):
    print(url.text)