from flask import Flask, render_template, request, session
from classes.specialty import Specialty

prev_option = ""

def apps_specialty():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Specialty.current()
            Specialty.remove(obj.id)
            if not Specialty.previous():
                Specialty.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Specialty.get_id(0))
            strobj = strobj + ';' + request.form["specialty_name"] 
            obj = Specialty.from_string(strobj)
            Specialty.insert(obj.id)
            Specialty.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Specialty.current()
            obj.name = request.form["specialty_name"]
            Specialty.update(obj.id)
        elif option == "first":
            Specialty.first()
        elif option == "previous":
            Specialty.previous()
        elif option == "next":
            Specialty.nextrec()
        elif option == "last":
            Specialty.last()
        elif option == 'exit':
            return render_template("layout.html", ulogin=session.get("user"))
        prev_option = option
        obj = Specialty.current()
        if option == 'insert' or len(Specialty.lst) == 0:
            id = 0
            id = Specialty.get_id(id)
            name = ""
        else:
            id = obj.id
            name = obj.name
        return render_template("Specialty.html", butshow=butshow, butedit=butedit, 
                        id=id,name = name,
                        ulogin=session.get("user"))
    else:
        return render_template("layout.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

