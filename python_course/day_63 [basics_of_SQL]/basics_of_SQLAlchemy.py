from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    author = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return "(id:%s | title:%s | author:%s | rating:%s)"%(self.id, self.title, self.author, self.rating)

# db.create_all()
# book1 = Books(title='Give and Take', author='ADAM graham', rating='9.5')
#
# db.session.add(book1)
# db.session.commit()

# read
all_books = db.session.query(Books).all()      # use Books.query.all()
print(repr(all_books))

# read a particular record by query
book = Books.query.filter_by(title="Give and Take").first()
print(book)

# update a particular record by query
# book_to_update = Books.query.filter_by(title='Harry potter and the goblet of fire').first()
# book_to_update.title = 'Harry Potter'
# db.session.commit()

# update a record by primary key
# book_id = 1
# book_to_update = Books.query.get(book_id)
# book_to_update.title = '  '
# db.session.commit()

# delete a particular record by primary key
# book_id = 1
# book_to_delete = Books.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()