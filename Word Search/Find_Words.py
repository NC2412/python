import requests
import Edit_File
from bs4 import BeautifulSoup as bs

def find_words():

    word_list = []
    definitions = {}
    url = '''
            https://dictionary.com/browse/
          '''

    word_input = input('Please enter words to be defined, separated by commas, no spaces: ')
    word_list = word_input.split(',')
    print(word_list)

    for word in word_list:
        data = requests.get(url + word)
        soup = bs(data.text, 'html.parser')
        print('Now parsing for: ' + word)

    div = soup.find('div', {'value':'1'})
    for span in div.find_all('span'):
        definitions[word] = span.text

    Edit_File.add_to_file('Words', definitions)

if __name__ == '__main__':
    find_words()