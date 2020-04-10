from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route('/')
def menu():
  return render_template('menu.html')

@app.route('/cca_submit', methods=['GET', 'POST'])
def cca_submit():
  if request.method == 'GET':
    return render_template("cca_submit.html")
  else: # Post
    username = request.form.get('username')
    email = request.form.get('email')
    school_class = request.form.get('school_class')
    problem = request.form.get('problem')
    suggestion = request.form.get('suggestion')
    message = "Thank you for your suggestion."
    current_date = datetime.date.today()
    fout = open("INFO_CCA.txt", "a")
    fout.write(username + "\n" + email + "\n" + school_class + "\n" + problem + "\n" + suggestion + "\n" + str(current_date) + "\n")
    fout.close()
    fin = open("INFO_CCA.txt", "r")
    lines = fin.readlines()
    fin.close()
    
    return render_template('cca_submit.html', message=message, username=username, email=email, school_class=school_class, problem=problem, suggestion=suggestion, current_date=current_date, lines=lines)

@app.route('/cca_view', methods=['GET'])
def cca_view():
  fin = open("INFO_CCA.txt", "r")
  lines = fin.readlines()
  fin.close()
  x = 0
  submissions = {}
  if lines != None:
    for i in range(0, int(len(lines)/6)):
      sub1 = [lines[x][:-1], lines[x+1][:-1], lines[x+2][:-1], lines[x+3][:-1], lines[x+4][:-1], lines[x+5][:-1]]
      submissions[i] = sub1
      x += 6
  else:
    sub1 = []
    continue
  return render_template('cca_view.html', sub1=sub1, submissions=submissions,lines=lines)


@app.route('/class_submit', methods=['GET', 'POST'])
def class_submit():
  if request.method == 'GET':
    return render_template("class_submit.html")
  else: # Post
    username = request.form.get('username')
    email = request.form.get('email')
    school_class = request.form.get('school_class')
    problem = request.form.get('problem')
    suggestion = request.form.get('suggestion')
    message = "Thank you for your suggestion."
    current_date = datetime.date.today()
    fout = open("INFO_CLASS.txt", "a")
    fout.write(username + "\n" + email + "\n" + school_class + "\n" + problem + "\n" + suggestion + "\n" + str(current_date) + "\n")
    fout.close()
    fin = open("INFO_CLASS.txt", "r")
    lines = fin.readlines()
    fin.close()
    
    return render_template('class_submit.html', message=message, username=username, email=email, school_class=school_class, problem=problem, suggestion=suggestion, current_date=current_date, lines=lines)

@app.route('/class_view', methods=['GET'])
def class_view():
  fin = open("INFO_CLASS.txt", "r")
  lines = fin.readlines()
  fin.close()
  x = 0
  submissions = {}
  for i in range(0, int(len(lines)/6)):
    sub1 = [lines[x][:-1], lines[x+1][:-1], lines[x+2][:-1], lines[x+3][:-1], lines[x+4][:-1], lines[x+5][:-1]]
    submissions[i] = sub1
    x += 6
  return render_template('class_view.html', sub1=sub1, submissions=submissions,lines=lines)


@app.route('/facilities_submit', methods=['GET', 'POST'])
def facilities_submit():
  if request.method == 'GET':
    return render_template("facilities_submit.html")
  else: # Post
    username = request.form.get('username')
    email = request.form.get('email')
    school_class = request.form.get('school_class')
    problem = request.form.get('problem')
    suggestion = request.form.get('suggestion')
    message = "Thank you for your suggestion."
    current_date = datetime.date.today()
    fout = open("INFO_FACIL.txt", "a")
    fout.write(username + "\n" + email + "\n" + school_class + "\n" + problem + "\n" + suggestion + "\n" + str(current_date) + "\n")
    fout.close()
    fin = open("INFO_FACIL.txt", "r")
    lines = fin.readlines()
    fin.close()
    
    return render_template('facilities_submit.html', message=message, username=username, email=email, school_class=school_class, problem=problem, suggestion=suggestion, current_date=current_date, lines=lines)

@app.route('/facilities_view', methods=['GET'])
def facilities_view():
  fin = open("INFO_FACIL.txt", "r")
  lines = fin.readlines()
  fin.close()
  x = 0
  submissions = {}
  for i in range(0, int(len(lines)/6)):
    sub1 = [lines[x][:-1], lines[x+1][:-1], lines[x+2][:-1], lines[x+3][:-1], lines[x+4][:-1], lines[x+5][:-1]]
    submissions[i] = sub1
    x += 6
  return render_template('facilities_view.html', sub1=sub1, submissions=submissions,lines=lines)

@app.route('/others_submit', methods=['GET', 'POST'])
def others_submit():
  if request.method == 'GET':
    return render_template("others_submit.html")
  else: # Post
    username = request.form.get('username')
    email = request.form.get('email')
    school_class = request.form.get('school_class')
    problem = request.form.get('problem')
    suggestion = request.form.get('suggestion')
    message = "Thank you for your suggestion."
    current_date = datetime.date.today()
    fout = open("INFO_OTHERS.txt", "a")
    fout.write(username + "\n" + email + "\n" + school_class + "\n" + problem + "\n" + suggestion + "\n" + str(current_date) + "\n")
    fout.close()
    fin = open("INFO_OTHERS.txt", "r")
    lines = fin.readlines()
    fin.close()
    
    return render_template('others_submit.html', message=message, username=username, email=email, school_class=school_class, problem=problem, suggestion=suggestion, current_date=current_date, lines=lines)

@app.route('/others_view', methods=['GET'])
def others_view():
  fin = open("INFO_OTHERS.txt", "r")
  lines = fin.readlines()
  fin.close()
  x = 0
  submissions = {}
  for i in range(0, int(len(lines)/6)):
    sub1 = [lines[x][:-1], lines[x+1][:-1], lines[x+2][:-1], lines[x+3][:-1], lines[x+4][:-1], lines[x+5][:-1]]
    submissions[i] = sub1
    x += 6
  return render_template('others_view.html', sub1=sub1, submissions=submissions,lines=lines)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
