from flask import Flask, render_template, request




app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['name']
    fix = request.form['fix']
    char = request.form['char']
    return render_template('pass.html', n=name, f=fix, c=char)



if __name__ == '__main__':
    app.run(debug=True)
