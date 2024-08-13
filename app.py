from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'  # Cambia esto por una clave secreta segura
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecopledge.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registro exitoso. ¡Ahora puedes iniciar sesión!')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            flash('Has iniciado sesión correctamente')
            return redirect(url_for('index'))
        else:
            flash('Inicio de sesión fallido. Revisa tus credenciales.')

    return render_template('login.html')

if __name__ == '__main__':
    # Crear las tablas aquí antes de iniciar la aplicación
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
