from flask import Flask, jsonify

students = [
        {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
        {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
        {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
        {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
        {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
        {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
        {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
        {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
        {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
        {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
    ]

app = Flask(__name__)

# "http://127.0.0.1:5000/students"
# Return student greater than 20 years old. 
@app.route('/old_students', methods = ['GET'])
def old_students():
  temp = []
  for stud in students:
    if stud['age'] > 20:
      temp.append(stud)
  return jsonify(temp)

# "http://127.0.0.1:5000/students"
# Return student less than 21 years old. 
@app.route('/young_students', methods = ['GET'])
def young_students():
  temp = []
  for stud in students:
    if stud['age'] < 21:
      temp.append(stud)
  return jsonify(temp)

# Return student less than 21 years old and grade equal to A.
@app.route('/advance_students', methods = ['GET'])
def advance_students():
  temp = []
  for stud in students:
    if stud['age'] < 21 and stud['grade'] == 'A':
      temp.append(stud)
  return jsonify(temp)

# Return student first and last name.
@app.route('/student_names', methods = ['GET'])
def student_names():
  temp = []
  for stud in students:
    temp.append({
      'first_name': stud['first_name'],
      'last_name': stud['last_name']   
      })
  return jsonify(temp)

# Return student first and last name and age.
@app.route('/student_ages', methods = ['GET'])
def student_ages():
  temp = []
  for stud in students:
    temp.append({
      'student_name': f"{stud['first_name']} {stud['last_name']}",
      'age': stud['age']  
      })
  return jsonify(temp) 

# Return all students.
@app.route('/all_students', methods = ['GET'])
def all_students():
  return jsonify(students)

app.run(debug=True)