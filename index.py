from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/portafolio')
def portafolio(): 
    return render_template('portafolio.html')

@app.route('/contactos')
def contactos(): 
    return render_template('contactos.html')


@app.route ('/mensaje', methods=['POST'])
def mensaje():
    if request.method == 'POST': 
        nombre = str(request.form['nombre'])
        telefono = str(request.form['telefono'])
        correo = str(request.form['correo'])
        telefono2 = str(request.form['telefono2'])
        asunto = str(request.form['asunto']) 
    return render_template('mensaje.html', tes=nombre, op=correo, tes2=telefono, tes3=telefono2)
    
if __name__ == '__main__':
    app.run() 