import re
import string
from urllib.request import urlopen
from bs4 import BeautifulSoup


def load_urls_from_file(file_path: str):
    try:
        with open(file_path) as f:
            content = f.readlines()
            return content
    except FileNotFoundError:
        print("the file " + file_path + " could not be found")
        exit(2)

def load_page(url: str):
    response = urlopen(url)
    html = response.read().decode('utf-8')
    return html

def crawl_page(page_contents: str):
    # create an instance on BeautifulSoup to easily scrape webpage
    page_dom_object = BeautifulSoup(page_contents, "html5lib")
    print(page_dom_object.prettify())
    # remove the script and style tag components
    for script in page_dom_object(["script", "style"]):
        script.extract()

    text = page_dom_object.get_text()
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


def get_links_on_page(page_contents: str):
   links = []
   page_dom_object = BeautifulSoup(page_contents, "html5lib")
   
   for link in page_dom_object.find_all('a'):
      link.extend(links.get('href'))

   return links


def get_head(page_contents: str):
    page_dom_object = BeautifulSoup(page_contents, "html5lib")
    return page_dom_object.head
