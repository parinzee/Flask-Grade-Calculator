from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dc2ff804898bac95f18c1d4f13cb6d127bbb48a86b99632cbe06931e3ec46776'


def calculation(grade):
    grade = int(grade)
    grade = float(grade)

    if grade >= 93:
        calculation.grade = 4.0

    elif grade >= 90:
        calculation.grade = 3.7

    elif grade >= 87:
        calculation.grade = 3.3

    elif grade >= 83:
        calculation.grade = 3.0

    elif grade >= 80:
        calculation.grade = 2.7

    elif grade >= 77:
        calculation.grade = 2.3

    elif grade >= 73:
        calculation.grade = 2.0

    elif grade >= 70:
        calculation.grade = 1.7

    elif grade >= 67:
        calculation.grade = 1.3

    elif grade >= 63:
        calculation.grade = 1.0

    elif grade >= 60:
        calculation.grade = 0.7

    else:
        calculation.grade = 0


def calculation2(grade):
    grade = int(grade)
    grade = float(grade)

    if grade >= 93:
        calculation2.grade = 4.5

    elif grade >= 90:
        calculation2.grade = 4.2

    elif grade >= 87:
        calculation2.grade = 3.8

    elif grade >= 83:
        calculation2.grade = 3.5

    elif grade >= 80:
        calculation2.grade = 3.2

    elif grade >= 77:
        calculation2.grade = 2.8

    elif grade >= 73:
        calculation2.grade = 2.5

    elif grade >= 70:
        calculation2.grade = 2.2

    elif grade >= 67:
        calculation2.grade = 1.8

    elif grade >= 63:
        calculation2.grade = 1.5

    elif grade >= 60:
        calculation2.grade = 1.2

    else:
        calculation2.grade = 0


@app.route("/")
def home_page():
    return render_template('home.html')


@app.route("/normal", methods=['GET', 'POST'])
def normal_page():
    return render_template('normal.html', title='Normal')


@app.route('/send', methods=['POST'])
def send():
    core1 = request.form['core1']
    core2 = request.form['core2']
    core3 = request.form['core3']
    core4 = request.form['core4']

    elect1 = request.form['elective1']
    elect2 = request.form['elective2']
    elect3 = request.form['elective3']
    elect4 = request.form['elective4']
    elect5 = request.form['elective5']
    elect6 = request.form['elective6']

    calculation(core1)
    core1 = calculation.grade

    calculation(core2)
    core2 = calculation.grade

    calculation(core3)
    core3 = calculation.grade

    calculation(core4)
    core4 = calculation.grade

    calculation(elect1)
    elect1 = calculation.grade

    calculation(elect2)
    elect2 = calculation.grade

    calculation(elect3)
    elect3 = calculation.grade

    calculation(elect4)
    elect4 = calculation.grade

    calculation(elect5)
    elect5 = calculation.grade

    calculation(elect6)
    elect6 = calculation.grade

    final_core = (core1 + core2 + core3 + core4) * 0.5
    final_elect = (elect1 + elect2 + elect3 + elect4 + elect5 + elect6) * 0.25
    final_grade = (final_core + final_elect) / 3.5

    final_grade = round(final_grade, 2)

    return render_template('normal.html', title='Normal', final_grade=final_grade)


@app.route("/beta", methods=['GET', 'POST'])
def beta_page():
    return render_template('beta.html', title='Beta')


@app.route('/send2', methods=['POST'])
def send2():
    core1 = request.form['core1']
    core2 = request.form['core2']
    core3 = request.form['core3']
    core4 = request.form['core4']

    elect1 = request.form['elective1']
    elect2 = request.form['elective2']
    elect3 = request.form['elective3']
    elect4 = request.form['elective4']
    elect5 = request.form['elective5']
    elect6 = request.form['elective6']

    calculation2(core1)
    core1 = calculation2.grade

    calculation2(core2)
    core2 = calculation2.grade

    calculation2(core3)
    core3 = calculation2.grade

    calculation2(core4)
    core4 = calculation2.grade

    calculation(elect1)
    elect1 = calculation.grade

    calculation(elect2)
    elect2 = calculation.grade

    calculation(elect3)
    elect3 = calculation.grade

    calculation(elect4)
    elect4 = calculation.grade

    calculation(elect5)
    elect5 = calculation.grade

    calculation(elect6)
    elect6 = calculation.grade

    final_core = (core1 + core2 + core3 + core4) * 0.5
    final_elect = (elect1 + elect2 + elect3 + elect4 + elect5 + elect6) * 0.25
    final_grade = (final_core + final_elect) / 3.5

    final_grade = round(final_grade, 2)

    return render_template('beta.html', title='Beta', final_grade=final_grade)