
from flask import Flask, render_template, request 
                                         

app = Flask(__name__)  


@app.route('/')  
def home():      
    return render_template("home.html") 

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route('/cursos')
def cursos():
    return render_template("cursos.html")

@app.route('/detalle')
def detalle():
    id = request.args.get('id')
    return render_template('detallecursos.html', id=id)


if __name__ == '__main__':
    app.run(debug=True)   