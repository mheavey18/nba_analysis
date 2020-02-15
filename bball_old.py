from bs4 import BeautifulSoup
import re

f = open('fte.txt', 'r')
content = f.read()

soup = BeautifulSoup(content, 'html.parser')

lst = soup.find_all("table", class_=re.compile("^post game"))

for i in range(len(lst)):
    game_lst = []
    game = lst[i]
    table_rows = game.find_all('tr')
    for j in range(len(table_rows)):
        if j == 2 or j == 3:
            tr = table_rows[j]
            td = tr.find_all('td')
            row = [td[k].text for k in range(
                len(td)) if k != 0 and k != 1 and k != 6]
            game_lst.append(row)
    print(game_lst)
