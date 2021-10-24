from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "mysecretkey"


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/sessionsuperadmin", methods=["GET", "POST"])
def sessionsuperadmin():
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]

        if not user:
            error = "Debes Ingresar El Usuario"
            flash(error)
            return redirect(url_for("login"))

        if not password:
            error = "Debes Ingresar La Contraseña"
            flash(error)
            return redirect(url_for("login"))

        if user == "Prueba" and password == "Prueba123":
            return render_template("superadmin.html")
        elif user == "Usuario" and password == "Usuario123":
             return redirect(url_for("user"))
        else:
            flash("Usuario y Contraseña No Validos ")

            return redirect(url_for("login"))

    return render_template("superadmin.html")


@app.route("/manageuser", methods=["GET", "POST"])
def manageuser():
    return render_template("gestionar.html")


@app.route("/adduser", methods=["GET", "POST"])
def adduser():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        id = request.form["id"]
        fnacimiento = request.form["fnacimiento"]
        cargo = request.form["cargo"]
        tcontrato = request.form["tcontrato"]
        fingreso = request.form["fingreso"]
        email = request.form["email"]
        fterminacion = request.form["fterminacion"]
        dependencia = request.form["dependencia"]
        salario = request.form["salario"]
        rol = request.form["rol"]

        if not id:
            error = "Debes Ingresar El ID"
            flash(error)
            return redirect(url_for("adduser"))

        if not fname:
            error = "Debes Ingresar El Nombre"
            flash(error)
            return redirect(url_for("adduser"))

        if not lname:
            error = "Debes Ingresar El Apellido"
            flash(error)
            return redirect(url_for("adduser"))

        if not fnacimiento:
            error = "Debes Ingresar Fecha de Nacimiento"
            flash(error)
            return redirect(url_for("adduser"))

        if not cargo:
            error = "Debes Ingresar El Cargo"
            flash(error)
            return redirect(url_for("adduser"))

        if not tcontrato:
            error = "Debes Ingresar Tipo de Contrato"
            flash(error)
            return redirect(url_for("adduser"))

        if not fingreso:
            error = "Debes Ingresar Fecha de Ingreso"
            flash(error)
            return redirect(url_for("adduser"))

        if not email:
            error = "Debes Ingresar Email"
            flash(error)
            return redirect(url_for("adduser"))

        if not fterminacion:
            error = "Debes Ingresar Fecha de Terminacion"
            flash(error)
            return redirect(url_for("adduser"))

        if not dependencia:
            error = "Debes Ingresar Dependencia"
            flash(error)
            return redirect(url_for("adduser"))

        if not salario:
            error = "Debes Ingresar Salario"
            flash(error)
            return redirect(url_for("adduser"))

        if not rol:
            error = "Debes Ingresar Rol"
            flash(error)
            return redirect(url_for("adduser"))

        flash("Usuario Creado Exitosamente")
        return redirect(url_for("adduser"))

    return render_template("empleados.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")


@app.route("/pruebas")
def pruebas():
    return render_template("pruebas.html")


@app.route("/registeruser", methods=["GET", "POST"])
def registeruser():
    return render_template("empleados.html")


@app.route("/evaluationuser", methods=["GET", "POST"])
def evaluationuser():
    return render_template("evaluacion.html")


@app.route("/infouser", methods=["GET", "POST"])
def infouser():
    usuario = [
        "001",
        "Camilo",
        "Noguera",
        "18",
        "Tecnico",
        "100000",
        "Departamento de Sistemas",
        "12-02-2003",
        "Indefinido",
        "correo@gmail.com"
        
        
    ]
    return render_template("infousuario.html", data=usuario)


@app.route("/editarusuario", methods=["GET", "POST"])
def edituser():
    if request.method == "POST":
        return "Usuario Actualizado Correctamente"
    
    return render_template("editarusuario.html")

@app.route("/calificacion",  methods=["GET", "POST"])
def calificacion():
    return render_template("calificacion.html")

@app.route("/user",  methods=["GET", "POST"])
def user():
    return render_template("user.html")

@app.route("/deleteuser", methods=["GET", "POST"])
def deleteuser():
    return "Usuario Eliminado Correctamente"

@app.route("/vercomentario", methods=["GET", "POST"])
def vercomentario():
    return render_template("vercomentario.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)    