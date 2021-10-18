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
    return "Información del Usuario"


@app.route("/edituser", methods=["GET", "POST"])
def edituser():
    return "Usuario Editado Correctamente"


@app.route("/deleteuser", methods=["GET", "POST"])
def deleteuser():
    return "Usuario Eliminado Correctamente"
