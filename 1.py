from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index/')
def html_index():
    return render_template('index.html')

@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    return render_template('clothes.html', **context)

@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)

@app.route('/hats/')
def hats():
    context = {'title': 'Шляпы'}
    return render_template('hats.html', **context)

@app.route('/heavy_weapons/')
def heavy_weapons():
    context = {'title': 'Тяжелое вооружение'}
    return render_template('heavy_weapons.html', **context)

@app.route('/mg/')
def mg():
    context = {'title': 'Пулеметы'}
    return render_template('mg.html', **context)


if __name__ == '__main__':
    app.run(debug=True)