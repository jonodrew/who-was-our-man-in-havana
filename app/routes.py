from flask import render_template
from app import app
from app.models import Diplomat, Post


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Diplowho, Diplowhen, Diplowhat?')


@app.route('/diplomat', methods=['POST'])
def diplomat():
    diplomat = Diplomat().random()
    print(diplomat.name)
    return render_template('diplomat.html', title='Diplowho, Diplowhen, Diplowhat?', diplomat=diplomat)


@app.route('/post')
def post():
    post = Post().random()
    return render_template('post.html', title='RandoPost', post=post)