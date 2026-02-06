from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
            'index.html',
            breadcrumb=['Inicio']
        )
    
@app.route('/sistema-ambiental')
def sistema_ambiental():
    return render_template(
        'sistema.html',
        breadcrumb=['Inicio', 'Sistema de Gestion Ambiental']
    )
    
@app.route('/futuro')
def futuro():
    return render_template(
        'futuro.html',
        breadcrumb=['Inicio', 'Futuras Generaciones']
    )
        
@app.route('/tres-r')
def tres_r():
    return render_template(
        'tres_r.html',
        breadcrumb=['Inicio', 'Principio de las 3R...']
    )
        
if __name__ == '__main__':
    app.run(debug=True)