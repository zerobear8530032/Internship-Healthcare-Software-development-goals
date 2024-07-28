import secrets
import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
from healthcareproject import app,db,bcrypt,mail
from flask import render_template,flash,redirect,url_for,request,abort
from healthcareproject.form import RegisterForm,LoginForm,RequestResetForm,ResetPasswordForm
from healthcareproject.models import Registertable
from flask_login import login_user,current_user,logout_user,login_required
from flask_mail import Message

@app.route("/register", methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        print("Form validation successful!")  # Add a print statement to check if form validation is successful
        hashed = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        userdata = Registertable(username=form.username.data, email=form.email.data, password=hashed)
        db.session.add(userdata)
        db.session.commit()
        flash("Your account is created and you can login now!", 'success')
        return redirect(url_for('login'))  
    else:
        print("Form validation failed!") 
    return render_template("Register.html", title="Register", form=form)

@app.route("/login",methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
         return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
            userdata=Registertable.query.filter_by(email=form.email.data).first()
            if(userdata and bcrypt.check_password_hash(userdata.password,form.password.data)):
                 login_user(userdata,remember=form.remember.data)
                 next_page=request.args.get('next')
                 return redirect(next_page) if next_page else  redirect(url_for("home"))
            else:     
                flash('check email and password',"danger")
    return render_template("Login.html",title="Login",form=form)


