from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime


#rename db to users.db , reinstantiate the db and make a new fake user to see if it works when done
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
    firstname = db.Column(db.String(50),unique=False, nullable=False)
    lastname = db.Column(db.String(50),unique=False, nullable=False)
    birthday = db.Column(db.Date,unique=False, nullable=False)
    role = db.Column(db.String(100),unique=False,nullable=False)
    about = db.Column(db.String(500),unique=False,nullable=False)
    #add picture as well when you've got time (SQLAlchemy-ImageAttach)

    def __repr__(self):
        return  'name: ' + str(self.firstname) + ' ' + str(self.lastname) + ', ' + 'birthday: ' + str(self.birthday)  + ', ' + 'role :' + str(self.role)  + ', ' + 'about :' + str(self.about)


#uncomment to create database if not already in directory
#db.create_all()

#create test user for development purposes
testuser = User(firstname='Vinzent', lastname='Croyy', birthday=date(1994, 7,8), role='Brother of Head Developer', about='He doesnt know')

#add testuser to db
db.session.add(testuser)
db.session.commit()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showall', methods=['GET', 'POST'])
def showallusers():
    allusers = User.query.all()
    return jsonify(allusers)




# if __name__ == "__main__":
#     app.run(debug=True)


