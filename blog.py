from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register.html')
def try_exit():
    return render_template('register.html')


@app.route('/user/<string:name>/<int:user_id>')
def hello_user(name, user_id):
    return 'Hello ' + name + ' your id is ' + str(user_id)


@app.route('/template-flask_demo_project')
def template_tets():
    return render_template('flask_demo_project.html')

if __name__ == '__main__':
    app.run(debug=True)
