from flask import Flask, render_template, request, session
from datafile import filename
from classes.patient import Patient
from classes.doctor import Doctor
from classes.ward import Ward
from classes.appointment import Appointment
from classes.userlogin import Userlogin
from subs.apps_patient import apps_patient
from subs.apps_gform import apps_gform 
from subs.apps_subform import apps_subform 
from subs.apps_userlogin import apps_userlogin
from subs.apps_plot import apps_plot
import subs.subs_patientFoto as patientfsub
import os 

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD'] = UPLOAD_FOLDER

Patient.read(filename + 'Patient.db')
Doctor.read(filename + 'Patient.db')
Ward.read(filename + 'Patient.db')
Appointment.read(filename + 'Patient.db')
Userlogin.read(filename + 'Patient.db')
app.secret_key = 'BAD_SECRET_KEY'

@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/login")
def login():
    return render_template("login.html", user= "", password="", ulogin=session.get("user"),resul = "")

@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname):
    return apps_gform(cname)

@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname):
    return apps_subform(cname)

@app.route("/patient", methods=["post", "get"])
def patient():
    return apps_patient(app)

@app.route("/patient_foto", methods=["post", "get"])
def patient_foto():
    return patientfsub.patientFotoform(app, 'Patient')

@app.route("/plot", methods=["post", "get"])
def plot():
    return apps_plot()

@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    return apps_userlogin()
if __name__ == '__main__':
    app.run()