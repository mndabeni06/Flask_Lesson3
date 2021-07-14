from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template('homepage.html', name=name)

@app.route('/looping/<int:number>')
def looping(number):
    return render_template('loopy.html', number=number)

@app.route('/times/<int:number>')
def times(number):
    return render_template('timestable.html', numbers=number)

if __name__ =='__main__':
    app.debug = True
    app.run()

