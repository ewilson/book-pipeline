import mysql.connector
from collections import namedtuple

Section = namedtuple('Section', 'author title section_title section_text')


def save_all(sections):
    cnx = mysql.connector.connect(user='pipeline', password='password',
                                  host='127.0.0.1',
                                  database='books')

    cursor = cnx.cursor()

    insert = """
        INSERT INTO books.book_staging
        (author, title, section_title, section_text)
        VALUES (%(author)s, %(title)s, %(section_title)s, %(section_text)s)
    """

    cursor.executemany(insert, sections)
    cnx.commit()
    cursor.close()
    cnx.close()
