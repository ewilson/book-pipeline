import mysql.connector


def save_all(sections):
    cnx = mysql.connector.connect(user='pipeline', password='password',
                                  host='127.0.0.1',
                                  database='books')

    cursor = cnx.cursor()

    insert = """INSERT INTO books.book_staging
                (author, title, section_title, section_text)
                VALUES ('Owen','Mortification','1','KILL,KILL')"""

    cursor.execute(insert)
    print(cursor.lastrowid)
    cnx.commit()
    cursor.close()
    cnx.close()

if __name__ == '__main__':
    save_all(['asdf'])