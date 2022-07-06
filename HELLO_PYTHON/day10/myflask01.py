from flask import Flask
from flask.globals import request
from flask.templating import render_template
from day10.daoemp import DaoEmp

app = Flask(__name__)


@app.route('/')
@app.route('/emp_list')
def emp_list():
    de = DaoEmp()
    list = de.selects()
    return render_template('emp_list.html', list=list)


@app.route('/emp_detail')
def emp_detail():
    de = DaoEmp()
    e_id = request.args.get('e_id')
    
    list = de.select(e_id)
    return render_template('emp_detail.html', list=list)


@app.route('/emp_add')
def emp_add():
    return render_template('emp_add.html')


@app.route('/emp_add_act', methods=['GET', 'POST'])
def emp_add_act():
    de = DaoEmp()
    
    e_name = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    
    cnt = de.insert(e_name, sex, addr)
    
    return render_template('emp_add_act.html', cnt=cnt)

@app.route('/emp_del')
def emp_del():
    de = DaoEmp()
    e_id = request.args.get('e_id')
    
    list = de.select(e_id)
    
    return render_template('emp_del.html', list=list)

@app.route('/emp_del_act')
def emp_del_act():
    de = DaoEmp()
    e_id = request.args.get('e_id')
    cnt = de.delete(e_id)
    
    return render_template('emp_del_act.html', cnt=cnt)


@app.route('/emp_mod')
def emp_mod():
    de = DaoEmp()
    e_id = request.args.get('e_id')
    
    list = de.select(e_id)
    return render_template('emp_mod.html', list=list)

@app.route('/emp_mod_act', methods=['GET', 'POST'])
def emp_mod_act():
    de = DaoEmp()
    
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    
    cnt = de.update(e_id, e_name, sex, addr)
    
    return render_template('emp_mod_act.html', cnt=cnt)


if __name__ == '__main__':
    app.run(debug=True)
