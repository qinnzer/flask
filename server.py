from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def none():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def prom():
    return '''
    Человечество вырастает из детства.
</br>Человечеству мала одна планета.
</br>Мы сделаем обитаемыми безжизненные пока планеты.
</br>И начнем с Марса!
</br>Присоединяйся!
    '''


@app.route('/image_mars')
def image():
    return f'''<h1>Жди нас, марс!</h1>
    <img src="{url_for('static', filename='img/mars.png')}" 
               alt="здесь должна была быть картинка, но не нашлась">
    </br>Вот она какая, красная планета.'''


@app.route('/promotion_image')
def prom_image():
    return f'''
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
                         rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" 
                         crossorigin="anonymous">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
                         rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" 
                         crossorigin="anonymous">
                        
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <div class="container-fluid">
                            <h1>Жди нас, марс!</h1>
                            <img src="{url_for('static', filename='img/mars.png')}" 
                            alt="здесь должна была быть картинка, но не нашлась">
                        <!doctype html>
                            <h3 class="custom-bggrey"></br>Человечества вырастет из детства.</h3>
                            <h3 class="custom-bggreen"></br>Человечеству мала одна планета.</h3>
                            <h3 class="custom-bggrey"></br>Мы сделаем обитаемыми безжизненные пока планеты.</h3>
                            <h3 class="custom-bgyellow"></br>И начнём с Марса!</h3>
                            <h3 class="custom-bgred"></br>Присоединяйся!</h3>
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
