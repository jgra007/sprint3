from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = "mysecretkey"


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/superadmin", methods=["GET","POST"])
def superadmin():
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




