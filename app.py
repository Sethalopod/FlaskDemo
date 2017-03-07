from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@localhost/swe'

db = SQLAlchemy(app)

class Students(db.Model):
	__tablename__ = 'students'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String)
	grader_id = db.Column(db.Integer, db.ForeignKey('graders.id'))
	grader = db.relationship('Graders', back_populates="students")

class Graders(db.Model):
	__tablename__ = 'graders'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String)
	students = db.relationship('Students', back_populates="grader")

@app.route('/')
def index():
	return "hello world"

@app.route('/static')
def template():
	return render_template("static.html")

@app.route('/students')
def students():
	return render_template("students.html", students=Students.query.all(), graders=Graders.query.all())

if __name__ == "__main__":
	"""
	db.create_all()				# Only want to do this once, this is just here for demonstration
	
	grader = Graders()
	grader.name = "Cindy"
	# alernative way
	# grader = Graders(name="Seth)

	student = Students()
	student.name = "Susy"
	student.grader = grader

	db.session.add(grader)
	db.session.add(student)
	db.session.commit()
	"""
	app.run()