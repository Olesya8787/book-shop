import sqlite3

from models import*
from UI import*

def save_data(conn, curs, elem):       
    curs.execute("""
        INSERT INTO books VALUES(?,?,?,?)  
    """, elem )
    conn.commit()

def get_inputs_data(conn, curs, inputs):
    books = []  
    for input_item in inputs:
       book = input_item['data'].to_int(    
       )if input_item['key'] == "book_id" or input_item['key'] == "is_bestseller" else input_item['data'].get_data()
       books.append(book)
     
    save_data(conn, curs, books)

def select_all_data(conn,book):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM books""")
    books = cur.fetchall()
    for book in books:
        print(book)

def delete_data(conn):
    cur = conn.cursor()
    cur.execute("""DELETE FROM books WHERE book_id=7  """)
    conn.commit()
    
def main():
    connection = sqlite3.connect("book_shop.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(book_id INT PRIMARY KEY, title TEXT,  author TEXT, is_bestseller INT)
        """ )
    connection.commit()
 

    book_schema = Book(1,"The Green Mile", "Stephen King", True )
    book_fields = list(book_schema.__dict__.keys())
    screen = UI("Book shop", 550, 450)
    inputs = []
    dict_screen = screen.__dict__
 

    for filed in book_fields:
        tk_input = Input()
        inputs.append(
            {
                "key": filed,
                "data": tk_input
            }
        )
        tk_label = Label(filed)
        
        screen.pack(tk_input.get_input_component())
        screen.pack(tk_label.get_label_component())

    btn_submit = Button("Add to DB", "purple",
                        "black", lambda: get_inputs_data(connection, cursor, inputs)).get_button_component()
    

    btn_submit_select= Button("Show books", "purple",
                        "black", lambda: select_all_data(connection,inputs)).get_button_component() 

    btn_submit_delete= Button("Delete books", "purple",
                        "black", lambda: delete_data(connection)).get_button_component()    
    screen.pack(btn_submit)
    screen.pack(btn_submit_select)
    screen.pack(btn_submit_delete)

    UI.loop(dict_screen)

if __name__ == "__main__":
    main()