from flask import Flask, render_template, request, session
from classes.museum import Museum

prev_option = ""

def apps_museum():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Museum.current()
            Museum.remove(obj.id)
            if not Museum.previous():
                Museum.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Museum.get_id(0))
            strobj = strobj + ';' + request.form["name"] 
            obj = Museum.from_string(strobj)
            Museum.insert(obj.id)
            Museum.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Museum.current()
            obj.name = request.form["name"]
            Museum.update(obj.id)
        elif option == "first":
            Museum.first()
        elif option == "previous":
            Museum.previous()
        elif option == "next":
            Museum.nextrec()
        elif option == "last":
            Museum.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Museum.current()
        if option == 'insert' or len(Museum.lst) == 0:
            id = 0
            id = Museum.get_id(id)
            name = ""
        else:
            id = obj.id
            name = obj.name
        return render_template("museum.html", butshow=butshow, butedit=butedit, 
                        id=id,name = name, 
                        ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

