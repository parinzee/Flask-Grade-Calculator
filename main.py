from datetime import datetime, timedelta
from flask import Flask, render_template, make_response, flash, redirect, request
import os
from flask_sitemap import Sitemap

app = Flask(__name__)
ext = Sitemap(app=app)

app.config[
    "SECRET_KEY"
] = os.environ["SECRET_KEY"]


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


@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        language = request.form["lang"]
        print(language)
        res = make_response
        # Don't touch it please
        expire_date = datetime.now()
        expire_date += timedelta(days=360)

        res = make_response(render_template('home.html'), 200)

        # Set secure to true to deployment
        if language == "English":
            res.set_cookie("gc_lang", 'en', expires=expire_date, secure=False)
        else:
            res.set_cookie("gc_lang", 'th', expires=expire_date, secure=False)
        
        return res

    if not request.cookies.get('gc_lang'):
        flash("คุณต้องการใช้ภาษาไทยหรือไม่?/Do you want to use English?")
        return render_template("home.html")
    else:
        return render_template("home.html")

@ext.register_generator
def home_page():
    yield 'home_page', {}


@app.route("/standards", methods=["GET", "POST"])
def normal_page():
    if request.method == "POST":
        core1 = request.form["core1"]
        core2 = request.form["core2"]
        core3 = request.form["core3"]
        core4 = request.form["core4"]

        elect1 = request.form["elective1"]
        elect2 = request.form["elective2"]
        elect3 = request.form["elective3"]
        elect4 = request.form["elective4"]
        elect5 = request.form["elective5"]
        elect6 = request.form["elective6"]
        
        try:
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
        except:
            final_grade = "Please don't enter text, just numbers"
            return render_template("normal.html", title="Normal", final_grade=final_grade)


        final_core = (core1 + core2 + core3 + core4) * 0.5
        final_elect = (elect1 + elect2 + elect3 + elect4 + elect5 + elect6) * 0.25
        final_grade = (final_core + final_elect) / 3.5

        final_grade = round(final_grade, 2)

        return render_template("normal.html", title="Normal", final_grade=final_grade)

    else:
        return render_template("normal.html", title="Normal")

@ext.register_generator
def normal_page():
    yield 'normal_page', {}

@app.route("/honors", methods=["GET", "POST"])
def beta_page():
    if request.method == "POST":
        core1 = request.form["core1"]
        core2 = request.form["core2"]
        core3 = request.form["core3"]
        core4 = request.form["core4"]

        elect1 = request.form["elective1"]
        elect2 = request.form["elective2"]
        elect3 = request.form["elective3"]
        elect4 = request.form["elective4"]
        elect5 = request.form["elective5"]
        elect6 = request.form["elective6"]

        try:
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
        except:
            final_grade = "Please don't enter text, just numbers"
            return render_template("normal.html", title="Normal", final_grade=final_grade)

        final_core = (core1 + core2 + core3 + core4) * 0.5
        final_elect = (elect1 + elect2 + elect3 + elect4 + elect5 + elect6) * 0.25
        final_grade = (final_core + final_elect) / 3.5

        final_grade = round(final_grade, 2)

        return render_template("beta.html", title="Honors", final_grade=final_grade)

    else:

        return render_template("beta.html", title="Honors")

@ext.register_generator
def beta_page():
    yield 'beta_page', {}

@app.route("/elementary", methods=["POST", "GET"])
def elementary():

    if request.method == "POST":
        sub1 = int(request.form["sub1"])
        sub2 = int(request.form["sub2"])
        sub3 = int(request.form["sub3"])
        sub4 = int(request.form["sub4"])
        sub5 = int(request.form["sub5"])

        try:
            grade = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
        except:
            final_grade = "Please don't enter text, just numbers"
            return render_template("elementary.html", title="Elementary", final_grade=final_grade)

        if grade > 150:
            grade = "Are you trying to break me? Are you Int?"

        return render_template("elementary.html", title="Elementary", final_grade=grade)

    else:
        return render_template("elementary.html", title="Elementary")

@ext.register_generator
def elementary():
    yield 'elementary', {}

@app.route("/credits")
def credits():
    return render_template("credits.html", title="Credits!")

@ext.register_generator
def credits():
    yield 'credits', {}


@app.route("/help")
def help():
    return render_template("help.html", title="Help")

@ext.register_generator
def help():
    yield 'help', {}

@app.before_request
def before_request():
    if request.url == "https://python-grade-cal.herokuapp.com/sitemap.xml":
        url = request.url.replace("https://", "http://", 1)
        code = 301
        return redirect(url, code=code)
    
    elif request.url.startswith("http://") and request.url != "http://python-grade-cal.herokuapp.com/sitemap.xml":
        url = request.url.replace("http://", "https://", 1)
        code = 301
        return redirect(url, code=code)