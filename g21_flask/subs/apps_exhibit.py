from flask import Flask, render_template, request, session
from classes.exhibit import Exhibit

prev_option = ""

def apps_exhibit():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Exhibit.current()
            Exhibit.remove(obj.id)
            if not Exhibit.previous():
                Exhibit.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Exhibit.get_id(0))
            strobj = strobj + ';' + request.form["creation_date"] + ';' + \
            request.form["title"] + ';' + request.form["category"]
            obj = Exhibit.from_string(strobj)
            Exhibit.insert(obj.id)
            Exhibit.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Exhibit.current()
            obj.creation_date = request.form["creation_date"]
            obj.title = request.form["title"]
            obj.category = float(request.form["category"])
            Exhibit.update(obj.id)
        elif option == "first":
            Exhibit.first()
        elif option == "previous":
            Exhibit.previous()
        elif option == "next":
            Exhibit.nextrec()
        elif option == "last":
            Exhibit.last()
        elif option == 'exit':
            return render_template("layout.html", ulogin=session.get("user"))
        prev_option = option
        obj = Exhibit.current()
        if option == 'insert' or len(Exhibit.lst) == 0:
            id = 0
            id = Exhibit.get_id(id)
            creation_date = title = category = ""
        else:
            id = obj.id
            creation_date = obj.creation_date
            title = obj.title
            category = obj.category
        return render_template("exhibit.html", butshow=butshow, butedit=butedit, 
                        id=id,creation_date = creation_date,title=title,category=category, 
                        ulogin=session.get("user"))
    else:
        return render_template("layout.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

