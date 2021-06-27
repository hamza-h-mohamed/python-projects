import sqlite3

db_name = "games.db"

def ask_for_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            break
        except ValueError:
            print("Enter a valid integer. Try again.") 
    return x
def ask_for_float(prompt):
    while True:
        try:
            y = float(input(prompt))
            break
        except ValueError:
            print("Enter a valid integer. Try again.")
    return y

def connect_to_db():
    db_conn = sqlite3.connect(db_name)
    db_cursor = db_conn.cursor()
    print("database opened")
   
    return db_conn, db_cursor

def create_table(db_cursor):
    sql = "CREATE TABLE game (title TEXT PRIMARY KEY, price FLOAT, creator TEXT, rating INTEGER, platform TEXT, genre TEXT)"
   
    db_cursor.execute(sql)
    
    print("Table Created")

def drop_table(db_cursor):
    sql = "DROP TABLE IF EXISTS game"
    
    db_cursor.execute(sql)
    
    print("Table Deleted")

def insert_row(db_cursor):
    sql = "INSERT INTO game (title, price, creator, rating, platform, genre) VALUES (?, ?, ?, ?, ?, ?)"
   
    title = input("Enter the title: ")
    price = ask_for_float("Enter the price: ")
    creator = input("Enter the creator: ")
    rating = ask_for_int("Enter the rating: ")
    platform = input("Enter the platform: ")
    genre = input("Enter the genre: ")

    tuple_values = (title, price, creator, rating, platform, genre)

    db_cursor.execute(sql, tuple_values)

def select_all(db_cursor):
    sql = "SELECT * from game"
   
    result_set = db_cursor.execute(sql)
   
    for row in result_set:
        print(row)

def select_row(db_cursor):
    sql = "SELECT * from game WHERE title = ?"
    
    t = input("enter the title: ")
    
    tuple_title = (t,)
    
    result_set = db_cursor.execute(sql, tuple_title)
   
    for row in result_set:
        print(row)

    print("Row Selected")

def update_row(db_cursor):

    title = input("enter the title: ")
    rating = ask_for_int("Enter the rating: ")
    price = ask_for_float("Enter the price: ")
    
    sql = "UPDATE game SET rating = ?, price = ? WHERE title = ?"

    tuple_values = (rating, price, title)
    
    db_cursor.execute(sql, tuple_values)
    
    print("Row Updated")

def delete_row(db_cursor):
    sql = "DELETE FROM game WHERE title = ?"
  
    t = input("Enter the title: ")
   
    tuple_title = (t,)
    
    db_cursor.execute(sql, tuple_title)

def display_menu(db_conn, db_cursor):


    while True:
        select_all(db_cursor)

        print("Main Menu")
        print("\nEnter S to get started & create/refresh the table")
        print("Enter C to create row")
        print("Enter R to retrieve data")
        print("Enter U to update row")
        print("Enter D to delete row")
        print("Enter D to quit program")

        choice = input("enter your choice: ").upper()

        if choice == 'S':
            drop_table(db_cursor)
            create_table(db_cursor)
        elif choice == 'C':
            insert_row(db_cursor)
        elif choice == 'R':
            select_row(db_cursor)
        elif choice == 'D':
            delete_row(db_cursor)
        elif choice == 'U':
            update_row(db_cursor)
        elif choice == 'Q':
            break 
        else:
            print("Invalid option. Try again.")
            continue 
      
        db_conn.commit()
      
def main():

    db_conn, db_cursor = connect_to_db()
    create_table()
    display_menu(db_conn, db_cursor)
    db_conn.close()

main()
