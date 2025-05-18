
from flask import Flask, render_template, request, session
from classes.userlogin import Userlogin

prev_option = ""

def apps_userlogin():
    global prev_option
    ulogin = session.get("user")
    user_id = Userlogin.get_user_id(ulogin)
    if ulogin is not None:
        group = Userlogin.obj[user_id].usergroup if user_id in Userlogin.obj else ''
        if group != "admin":
            Userlogin.current(user_id)
        
        # Controle dos botões: vazio = ativo, "disabled" = desativado
        butshow = ""
        butedit = "disabled"

        option = request.args.get("option")
        msg = ""

        if option == "edit":
            butshow = "disabled"
            butedit = ""
        elif option == "delete":
            obj = Userlogin.current()
            Userlogin.remove(obj.id)
            if not Userlogin.previous():
                Userlogin.first()
        elif option == "insert":
            butshow = "disabled"
            butedit = ""
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            obj = Userlogin(0, request.form["user"], request.form["usergroup"],
                            Userlogin.set_password(request.form["password"]))
            Userlogin.insert(obj.id)
            Userlogin.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Userlogin.current()
            if group == "admin":
                obj.usergroup = request.form["usergroup"]
            if request.form["password"] != "":
                obj.password = Userlogin.set_password(request.form["password"])
            Userlogin.update(obj.id)
        elif option == "first":
            Userlogin.first()
        elif option == "previous":
            Userlogin.previous()
        elif option == "next":
            Userlogin.nextrec()
        elif option == "last":
            Userlogin.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=ulogin)

        prev_option = option
        obj = Userlogin.current()

        if option == 'insert' or len(Userlogin.lst) == 0:
            id_val = ""
            user = ""
            usergroup = ""
            password = ""
        else:
            id_val = obj.id
            user = obj.user
            usergroup = obj.usergroup
            password = ""

        return render_template("userlogin.html",
                               butshow=butshow,
                               butedit=butedit,
                               id=id_val,
                               user=user,
                               usergroup=usergroup,
                               password=password,
                               ulogin=ulogin,
                               group=group,
                               msg=msg)
    else:
        return render_template("index.html", ulogin=ulogin)


