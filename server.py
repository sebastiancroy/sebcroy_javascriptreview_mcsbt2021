from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profiles.db'
db = SQLAlchemy(app)


class User(db.Model):
    id: int
    firstname: str
    lastname: str
    birthday: date
    role: str
    about: str
    #add picture as well when you've got time (SQLAlchemy-ImageAttach)

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), unique=True, nullable=False)
    lastname = db.Column(db.String(50), unique=True, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    role = db.Column(db.String(100), unique=True, nullable=False)
    about = db.Column(db.String(500), unique=True, nullable=False)
    #add picture as well when you've got time (SQLAlchemy-ImageAttach)

    def __repr__(self):
        return  'Name: ' + str(self.firstname) + ' ' + str(self.firstname) + '.' + 'Birthday: ' + date(self.birthday) + '.' +'Role: ' + str(self.role) + '.' + 'Info: ' + str(self.about)



#uncomment to create database if not already in directory
#db.create_all()

#create test user for development purposes
#testuser = User(firstname='Sebastian', lastname='Croy', birthday=date(1995, 2, 19), role='Head Developer', about='I cannot deliver assignements on time')

#add testuser to db
#db.session.add(testuser)
#db.session.commit()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)