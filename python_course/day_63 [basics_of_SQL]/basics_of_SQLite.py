import sqlite3

# creates a connection to a new database (if the database does not exist then it will be created
db = sqlite3.connect(database="books-collection.db")

# create a cursor which will control the database
cursor = db.cursor()

# create a table

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE,"
#                "author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# CREATE TABLE books --- creates a table and the table's name is books
# () --- the parts that come inside the parentheses are going to be fields in this table (like column headings in excel)
# id INTEGER PRIMARY KEY-- field is called id which is of data type integer and it will be the primary key for the table

# title varchar(250) NOT NULL UNIQUE -- field name is title accepts variable length string composed of characters, 250
# is the maximum length of text, NOT NULL means it cant be left empty and UNIQUE is no 2 records can have the same title

# rating FLOAT NOT NULL -- field name rating accepts float data type and cannot be left empty

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K.Rowling','9.3')")
db.commit()

# SQl queries are very sensitive to typos