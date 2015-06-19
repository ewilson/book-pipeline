import baxter.sections as sections
import baxter.book_dao as book_dao

DELIM = '__________________________________________________________________'


def main():
    filename = '../baxter.txt'
    file = open(filename)
    text = file.read()
    chunks = [ s.strip() for s in text.split(DELIM)]
    parsed_sections = sections.extract_headers(chunks)
    book_dao.save_all(parsed_sections)

if __name__ == '__main__':
    main()