from flask import Flask, render_template, request
from werkzeug.utils import redirect

from data.db_session import create_session
from data.jobs import Jobs
from data.user import User
from forms.jobs_form import JobsForm
from forms.login_form import LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user

from data import db_session

from os import listdir

from random import randint, choice
from datetime import datetime as dt

import json

from forms.register_form import RegisterForm

app = Flask(__name__)


app.config["SECRET_KEY"] = "password123"

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def user_loader(user_id):
    session = db_session.create_session()
    return session.get(User, user_id)


@app.route("/")
@app.route("/index")
def main():
    session = create_session()
    result = session.query(Jobs, User).join(
        User,
        Jobs.team_leader == User.id
    ).all()
    return render_template("index.html", title="Главная", result=result)


@app.route("/promotion")
def promotion():
    return ("<p>Человечество вырастает из детства.</p>"
            "<p>Человечеству мала одна планета.</p>"
            "<p>Мы сделаем обитаемыми безжизненные пока планеты.</p>"
            "<p>И начнем с Марса!</p>"
            "<p>Присоединяйся!</p>")


@app.route("/image_mars")
def image_mars():
    return render_template("image_mars.html")


@app.route("/promotion_image")
def promotion_image():
    return render_template("promotion_image.html")


@app.route("/choice/<planet_name>")
def choice(planet_name):
    return f"""<!DOCTYPE html>
               <html lang="ru">
               <head>
                   <meta charset="UTF-8">
                   <meta name="viewport" content="width=device-width, initial-scale=1">
                   <title>Варианты выбора</title>
                   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
                         integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
                   <style>
                       .custom-alert {{
                           font-weight: bold;
                           font-size: 25px;
                           padding-left: 0;
                           padding-bottom: 0;
                       }}
                   </style>
               </head>
               <body>
                   <h1>Моё предложение: {planet_name}</h1>
                   <h3>Эта планета близка к Земле;</h3>
                   <div class="alert alert-success custom-alert" role="alert">
                       На ней много необходимых ресурсов;
                   </div>
                   <div class="alert alert-secondary custom-alert" role="alert">
                       На ней есть вода и атмосфера;
                   </div>
                   <div class="alert alert-warning custom-alert" role="alert">
                       На ней есть небоьшое магнитное поле;
                   </div>
                   <div class="alert alert-danger custom-alert" role="alert">
                       Наконец, она просто красива!
                   </div>
               </body>
               </html>"""


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f"""<!DOCTYPE html>
                   <html lang="ru">
                   <head>
                       <meta charset="UTF-8">
                       <meta name="viewport" content="width=device-width, initial-scale=1">
                       <title>Варианты выбора</title>
                       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
                             integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
                       <style>
                           .custom-alert {{
                               font-weight: bold;
                               font-size: 25px;
                               padding-left: 0;
                               padding-bottom: 0;
                           }}
                       </style>
                   </head>
                   <body>
                       <h1>Результаты отбора</h1>
                       <h3>Претендента на участие в миссии {nickname}:</h3>
                       <div class="alert alert-success custom-alert" role="alert">
                           Поздравляем! Ваш рейтинг после {level} этапа отбора
                       </div>
                       <div class="alert alert-light custom-alert" role="alert">
                           составляет {rating}!
                       </div>
                       <div class="alert alert-warning custom-alert" role="alert">
                           Желаем удачи!
                       </div>
                   </body>
                   </html>"""


@app.route("/astronaut_selection")
def astronaut_selection():
    return render_template("astronaut_selection.html", title="Отбор астронавтов")


@app.route("/load_photo", methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return render_template("load_photo.html",
                               title="Отбор астронавтов", f="static/images/user.jpg")
    elif request.method == 'POST':
        f = request.files['file']
        if f and f.filename != '':
            f.save(f"static/images/user.jpg")
        return render_template("load_photo.html",
                               title="Отбор астронавтов", f="static/images/user.jpg")


@app.route("/carousel")
def carousel():
    return render_template("carousel.html",
                           img1="static/images/marsohod.jpg",
                           img2="static/images/mars_chocolate.jpg",
                           img3="static/images/mars_home.jpg")


@app.route("/training/<prof>")
def training(prof):
    return render_template("training.html", title="Тренировки в полёте", prof=prof)


@app.route("/list_prof/<sp>")
def list_prof(sp):
    return render_template("list_prof.html", title="Список профессий", sp=sp,
                           profs=["инженер", "космонавт", "учёный", "капитан", "кондитер"])


@app.route("/answer")
@app.route("/auto_answer")
def auto_answer():
    context = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": True
    }
    return render_template("auto_answer.html", **context)


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(
            User.email == login_form.email.data
        ).first()
        if user and user.check_password(login_form.password.data):
            login_user(user, login_form.remember_me)
            return redirect("/")
        return render_template("login.html", form=login_form, message="Пользователь не существует")
    return render_template("login.html", form=login_form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/distribution")
def distribution():
    members = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template("distribution.html", members=members)


@app.route("/table/<sex>/<int:age>")
def table(sex, age):
    return render_template("table.html", sex=sex, age=age)


@app.route("/gallery", methods=['POST', 'GET'])
def gallery():
    if request.method == "GET":
        return render_template("gallery.html",
                               files=[f'images/gallery/{filename}' for filename in listdir('static/images/gallery')])
    elif request.method == "POST":
        f = request.files['file']
        if f and f.filename != '':
            while True:
                filename = f"photo{randint(1, 1000000000)}.jpg"
                if filename not in listdir('static/images/gallery'):
                    f.save(f"static/images/gallery/{filename}")
                    break
        return render_template("gallery.html",
                               files=[f'images/gallery/{filename}' for filename in listdir('static/images/gallery')])


@app.route("/member")
def member():
    with open(f"templates/members.json", 'r') as f: # если бы в json-е были бы строки на русском, как в примере,
        # то при считывании файла python бы почему-то перевёл русский на марсианский ('Р\xa0РёРґР»Рё РЎРєРѕС‚С‚' и т.п.)
        file = json.load(f)
        print(file)
        marser = file[choice(file.keys())]
    return render_template("member.html", name=marser["name"], surname=marser["surname"],
                           photo=marser["photo"], professions=', '.join(sorted(marser["professions"])))


@app.route("/addjob", methods=['GET', 'POST'])
@login_required
def addjob():
    jobs_form = JobsForm()
    if jobs_form.validate_on_submit():
        session = db_session.create_session()

        modules_request = Jobs(
            team_leader=jobs_form.team_leader.data,
            job=jobs_form.job.data,
            work_size=jobs_form.work_size.data,
            collaborators=jobs_form.collaborators.data,
            start_date=dt.now(),
            is_finished=jobs_form.is_finished.data
        )
        session.add(modules_request)
        session.commit()
    return render_template("addjob.html", form=jobs_form, title="Добавление работы")


@app.route("/register", methods=['GET', 'POST'])
def register():
    reg_form = RegisterForm()
    if reg_form.validate_on_submit():
        session = db_session.create_session()

        guy = User(
            surname=reg_form.surname.data,
            name=reg_form.name.data,
            age=reg_form.age.data,
            position=reg_form.position.data,
            speciality=reg_form.speciality.data,
            address=reg_form.address.data,
            email=reg_form.email.data,
        )
        guy.hash_password(reg_form.password.data)
        session.add(guy)
        session.commit()
        return redirect("/login")
    return render_template("register.html", form=reg_form, title="Регистрация")


if __name__ == "__main__":
    db_session.global_init("db/mars_explorer.db")
    app.run("127.0.0.1", 8080)
