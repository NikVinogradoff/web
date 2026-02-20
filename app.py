from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("base.html", title="Заготовка")


@app.route("/index")
def index():
    return render_template("base.html", title="Заготовка")


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
                               title="Отбор астронавтов", f="static/images/robot.jpg")
    elif request.method == 'POST':
        f = request.files['file']
        if f.filename == '':
            return render_template("load_photo.html",
                                   title="Отбор астронавтов", f="static/images/robot.jpg")
        elif f:
            f.save(f"static/images/{f.filename}")
            return render_template("load_photo.html",
                                   title="Отбор астронавтов", f=f"static/images/{f.filename}")
        return render_template("load_photo.html",
                               title="Отбор астронавтов", f="static/images/robot.jpg")


if __name__ == "__main__":
    app.run("127.0.0.1", 8080)
