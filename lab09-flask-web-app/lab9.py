from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask('name')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    author = db.Column(db.String(30))

@app.route('/', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        book = Book(name=name, author=author)
        db.session.add(book)
        db.session.commit()
        return redirect('/')

    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/clear', methods=['POST'])
def clear():
    Book.query.delete()
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
