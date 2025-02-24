from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def profession(prof):
    return render_template('prof.html', profe=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
