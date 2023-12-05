import mysql.connector as mysql_connector

# mycursor = mydb.cursor()

#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("John", "Highway 21")
#mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

class TestLibrary:
    def __init__(self):
        self.books = ["harry potter1", "harry potter2", "harry potter3"]
        self.no_of_books = len(self.books)
        self.db_connection = self.get_db_connect()
        print("-------welcome to library--------")

    def get_db_connect(self):
        print("getting db connection...")
        connection = mysql_connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="library"
        )
        print(connection, "connection established")
        return connection

    def deposit_book(self,book_id):
        mycursor = self.db_connection.cursor()
        sql3 = f"select status from library_book where book_id = {book_id};"

        res = mycursor.execute(sql3)
        res = mycursor.fetchall()
        print(res)
        if res[0][0] == "a":

            sql1 = f"UPDATE library_book SET status = 'p' WHERE book_id = {book_id};"
            sql2 = f"UPDATE library_book SET d_o_deposit =  '2023-12-6'  WHERE book_id = {book_id};"
            mycursor.execute(sql1)
            mycursor.execute(sql2)

            self.db_connection.commit()
            self.show_books()
            print("book is deposited")
        else:
            print("book is already depositted")

    def show_books(self):
        print("showing all the books from library...")
        mycursor = self.db_connection.cursor()
        mycursor.execute("SELECT * FROM library_book")
        all_books = mycursor.fetchall()

        for book in all_books:
            print(f"Book Name: {book[1]}, Status: {book[2]}")
        # print(f"This Library has: {self.no_of_books} books.The books are:")
        # for book in self.books:
        #     print(book)


    def borrow_book(self, book_id):
        mycursor = self.db_connection.cursor()
        #id = input("enter book id :")
        sql3 = f"select status from library_book where book_id = {book_id};"

        res = mycursor.execute(sql3)
        res = mycursor.fetchall()
        print(res)

        if res[0][0] == "p":
           sql1 = f"UPDATE library_book SET status = 'a' WHERE book_id = {book_id};"
           sql2 = f"UPDATE library_book SET d_o_borrow =  '2023-12-4'  WHERE book_id = {book_id};"

           mycursor.execute(sql1)
           mycursor.execute(sql2)
           self.db_connection.commit()
           print("you have borrowed a book")
           self.show_books()

        else:
            print("sorry this book is not available in library")


     #   sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'
    def update_books_in_library(self,book_id1,book_name1):
        mycursor = self.db_connection.cursor()
        password = "pooja"
        p = input("please enter password")
        if p != password:
            print("access denied")
        else:
            option = input("enter a if for adding a new book: \n enter d to delet a book:")
            if option == "a":
                sql1 = f"INSERT INTO library_book (book_id, book_name,status) VALUES ({book_id1},'{book_name1}','p')"

                mycursor.execute(sql1)

                self.db_connection.commit()
                print("you have added a book")
                self.show_books()
            elif option == "d":
                sql1 = f"delete from library_book where book_id = {book_id1};"

                mycursor.execute(sql1)

                self.db_connection.commit()
                print("you have deleted a book")
                self.show_books()








l1 = TestLibrary()
#l1.show_books()
#l1.borrow_book(2)
#l1.deposit_book(3)

while True:
    a = input("enter \n b: if you want to borrow a book \n d: if  you want to deposit a book \n s: to have  a look of library status \n u:if you want to update library \n q: to exit:")
    if a == "s":
       l1.show_books()

    elif a == "d":
       dep_book =  input("enter id of book you want to deposit:")
       l1.deposit_book(dep_book)


    elif a == "b":
       bor_book = input("enter id of book you want to borrow:")
       l1.borrow_book(bor_book)

    elif a == "u":
        b1 = input("enter book_id")
        b2 = input("enter book_name")
        l1.update_books_in_library(b1,b2)


    elif a == "q":
        break

    else:
        print("please enter correct choice")






