
#https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc
#https://www.guru99.com/create-drop-table-postgresql.html
#    https://realpython.com/flask-by-example-part-1-project-setup/








import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object("config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    published = db.Column(db.String())

    def __init__(self, name, author, published):
        self.name = name
        self.author = author
        self.published = published

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'author': self.author,
            'published':self.published
        }

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add")
def add_book():
    name=request.args.get('name')
    author=request.args.get('author')
    published=request.args.get('published')
    try:
        book=Book(
            name=name,
            author=author,
            published=published
        )
        db.session.add(book)
        db.session.commit()
        return "Book added. book id={}".format(book.id)
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        books=Book.query.all()
        return  jsonify([e.serialize() for e in books])
    except Exception as e:
	    return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        book=Book.query.filter_by(id=id_).first()
        return jsonify(book.serialize())
    except Exception as e:
	    return(str(e))

@app.route("/add/form",methods=['GET', 'POST'])
def add_book_form():
    if request.method == 'POST':
        name=request.form.get('name')
        author=request.form.get('author')
        published=request.form.get('published')
        try:
            book=Book(
                name=name,
                author=author,
                published=published
            )
            db.session.add(book)
            db.session.commit()
            return "Book added. book id={}".format(book.id)
        except Exception as e:
            return(str(e))
    return render_template("getdata.html")

if __name__ == '__main__':
    app.run()



# import os
# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# app.config.from_object("config.DevelopmentConfig")
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# #from models import Book
# class Book(db.Model):
#     __tablename__ = 'books'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     author = db.Column(db.String())
#     published = db.Column(db.String())
 
#     def __init__(self, name, author, published):
#         self.name = name
#         self.author = author
#         self.published = published

#     def __repr__(self):
#         return '<id {}>'.format(self.id)
    
#     def serialize(self):
#         return {
#             'id': self.id, 
#             'name': self.name,
#             'author': self.author,
#             'published':self.published
#         }


# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route("/add")
# def add_book():
#     name=request.args.get('name')
#     author=request.args.get('author')
#     published=request.args.get('published')
#     try:
#         book=Book(
#             name=name,
#             author=author,
#             published=published
#         )
#         db.session.add(book)
#         db.session.commit()
#         return "Book added. book id={}".format(book.id)
#     except Exception as e:
# 	    return(str(e))

# @app.route("/getall")
# def get_all():
#     try:
#         books=Book.query.all()
#         return  jsonify([e.serialize() for e in books])
#     except Exception as e:
# 	    return(str(e))

# @app.route("/get/<id_>")
# def get_by_id(id_):
#     try:
#         book=Book.query.filter_by(id=id_).first()
#         return jsonify(book.serialize())
#     except Exception as e:
# 	    return(str(e))

# if __name__ == '__main__':
#     app.run()

# @app.route("/name/<name>")
# def get_book_name(name):
#     return "name : {}".format(name)

# @app.route("/details")
# def get_book_details():
#     author=request.args.get('author')
#     published=request.args.get('published')
#     return "Author : {}, Published: {}".format(author,published)

# if __name__ == '__main__':
#     app.run()
