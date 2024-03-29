from bs4 import BeautifulSoup
import requests

def formatter(word):
    new_word = word.replace(' ', '_')
    new_word = new_word.replace(':', '')
    new_word = new_word.replace('__', '_')
    return new_word
name = input("Enter the movie name : ")
name = formatter(name)
link = f"https://www.rottentomatoes.com/m/{name}"
source = requests.get(link).text
soup = BeautifulSoup(source, 'lxml')
title = soup.find('h1').text
print()
print("Movie name : ", title)
score_board = soup.find('score-board-deprecated')
print("Tomatometer : ", score_board['tomatometerscore'])
print("Rating : ", score_board['rating'])
print(score_board.find('p').text)

