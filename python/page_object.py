import re
import string
from urllib.request import urlopen
from bs4 import BeautifulSoup


class PageObject():
    def __init__(self, url):
        html_handler =  urlopen(url)
        html =  html_handler.read().decode('utf-8')
        self.html_dom =  BeautifulSoup(html, 'html5lib')

    def get_content(self):
        return self.html_dom.get_text()

    def get_all_links(self):
        links = [] 
        for link in self.html_dom.find_all('a'):
            if 'http' in link.get('href'):
                print (link.get('href'))
                links.append(link.get('href'))

        return links

    def get_head(self):
        return self.html_dom.head
 
    def get_title(self):
        return self.html_dom.title

    def get_body(self):
        return self.html_dom.body

    def get_words(self):
        for script in self.html_dom(["script", "style"]):
            script.extract()

        text = self.html_dom.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

        text = ' '.join(chunk for chunk in chunks if chunk)
        plain_text = ''.join(filter(lambda x: x in string.printable, text))

        clean_words = []

        # traverse the entire words
        words = plain_text.split(" ")
        for word in words:
            clean = True

            # no punctuations allowed
            for punc in string.punctuation:
                if punc in word:
                    clean = False

                # no numbers allowed
                if any(char.isdigit() for char in word):
                    clean = False

                # at least two characters but no more than 10
                if len(word) < 2 or len(word) > 10:
                    clean = False

                # should match regex word
                if not re.match(r'^\w+$', word):
                    clean = False

                if clean:
                    try:
                        clean_words.append(word.lower())
                    except UnicodeEncodeError:
                        print(".")
        return clean_words
   

if __name__ == "__main__":
   web_obj = PageObject('https://www.crummy.com/software/BeautifulSoup/bs4/doc')
   for l in web_obj.get_all_links(): print (l)
