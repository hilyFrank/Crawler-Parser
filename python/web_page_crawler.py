import os
import argparse
import url_utilities

def main(database: str, url_list_file: str):
    print("Db " + database)
    print("Preparing to crawl" + url_list_file)
    urls = url_utilities.load_urls_from_file(url_list_file)
    word_list = []
    for url in urls:
        print("reading " + url)
        page_content = url_utilities.load_page(url=url)
        words = url_utilities.crawl_page(page_contents=page_content)
        word_list.extend(words)

       
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file =  args.input
    main(database=database_file, url_list_file=input_file)

