from flask import Flask, render_template, request, session
from classes.patient import Patient

prev_option = ""

def apps_patient():
    global prev_option
    ulogin=session.get("user")
    
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        
        elif option == "delete":
            obj = Patient.current()
            Patient.remove(obj.id)
            if not Patient.previous():
                Patient.first()
       
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        
        elif option == 'cancel':
            pass
        
        elif prev_option == 'insert' and option == 'save':
            obj = Patient(Patient.get_id(0),
                          request.form["name"],
                          request.form["age"],
                          request.form["diagnosis"],
                          request.form["condition"],
                          request.form["ward_id"],
                          ulogin)
            Patient.insert(obj.id)
            Patient.last()
        
        elif prev_option == 'edit' and option == 'save':
            obj = Patient.current()
            obj.patient_name = request.form["name"]
            obj.age = request.form["age"]
            obj.condition = request.form["condition"]
            obj.diagnosis = request.form["diagnosis"]
            obj.ward_id = request.form["ward_id"]
            Patient.update(obj.id)
        
        elif option == "first":
            Patient.first()
        
        elif option == "previous":
            Patient.previous()
        
        elif option == "next":
            Patient.nextrec()
        
        elif option == "last":
            Patient.last()
        
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Patient.current()
        
        if option == 'insert' or len(Patient.lst) == 0:
            id = Patient.get_id(0)
            name = age = condition = diagnosis = ward_id = ""
        
        else:
            id = obj.id
            name = obj.patient_name
            age = obj.age
            condition = obj.condition
            diagnosis = obj.diagnosis
            ward_id = obj.ward_id
        return render_template("patient.html", butshow=butshow, butedit=butedit, 
                        id=id,name = name,age = age,condition = condition, diagnosis = diagnosis, ward_id = ward_id,
                        ulogin=session.get("user"))
    
    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

