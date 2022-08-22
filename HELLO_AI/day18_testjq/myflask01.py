from flask import Flask
from flask.templating import render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/test01')
def test01():
    return render_template('test01.html')

@app.route('/test02')
def test02():
    return render_template('test02.html')

@app.route('/test03')
def test03():
    return render_template('test03.html')

@app.route('/test04')
def test04():
    return render_template('test04.html')

@app.route('/test05')
def test05():
    return render_template('test05.html')

@app.route('/test06')
def test06():
    return render_template('test06.html')

@app.route('/test07')
def test07():
    return render_template('test07.html')

@app.route('/test08')
def test08():
    return render_template('test08.html')

@app.route('/test09')
def test09():
    return render_template('test09.html')

@app.route('/test0a')
def test0a():
    return render_template('test0a.html')


if __name__ == '__main__':
    app.run()
