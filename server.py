from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime
from dataclasses import dataclass


# rename db to users.db , reinstantiate the db and make a new fake user to see if it works when done

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profiles.db'
db = SQLAlchemy(app)


@dataclass
class User(db.Model):
    id: int
    firstname: str
    lastname: str
    birthday: date
    role: str
    about: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50), unique=False, nullable=False)
    lastname = db.Column(db.String(50), unique=False, nullable=True)
    birthday = db.Column(db.Date, unique=False, nullable=True)
    role = db.Column(db.String(100), unique=False, nullable=True)
    about = db.Column(db.String(500), unique=False, nullable=True)


# create test user for development purposes
#testuser = User(firstname='Vinzent', lastname='Croyy', birthday=date(1994, 7,8), role='Brother of Head Developer', about='He doesnt know')

# add testuser to db
# db.session.add(testuser)
# db.session.commit()


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', data=users)


# Add User to database

@app.route('/addUser', methods=['GET', 'POST'])
def createuser():
    try:
        body = request.get_json()
        print(body)
        firstname = body['firstname']
        lastname = body['lastname']
        birthday = body['birthday']
        role = body['role']
        about = body['about']

        print(birthday)
        new_user = User(firstname=firstname, lastname=lastname, birthday=datetime.strptime(
            birthday, '%d-%m-%Y'), role=role, about=about)

        db.session.add(new_user)
        db.session.commit()
        return render_template("index.html")
    except Exception as e:
        print(e)
        return render_template("index.html"), 400

    


@app.route('/deleteUser/<id>', methods=['DELETE'])
def deleteuser(id):
    user_to_delete = User.query.get_or_404(id)
    db.session.delete(user_to_delete)
    db.session.commit()
    return render_template("index.html")


db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
