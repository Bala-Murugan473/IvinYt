from flask import Blueprint,render_template, request, flash,redirect,url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .Execute import * 
from Ivinyt import db
from flask_login import login_user,login_required,logout_user


auth = Blueprint('auth',__name__)


@auth.route('/admin',methods=['GET','POST'])
@login_required
def admin():
    if request.method=='POST':
        mobile=request.form.get('mobile')
        password =request.form.get('password')

        if mobile=='1234512345' and password=='captain':
            flash('Logged in as Admin !', category='success')
            # return redirect(url_for('views.admin'))
            date,time,price = Execute.MatchDetails()
            return render_template("adminuser.html",df=Execute.ClassicRegistration(),match_time=time,match_date=date,price=price)
            
        else:
            flash('Invalid Admin Credentials !', category='error')
            return render_template("admin.html")
    return render_template("admin.html")

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        mobile=request.form.get('mobile')
        password =request.form.get('password')
        
        user = User.query.filter_by(mobile=mobile).first()
        if user:
            if check_password_hash(user.password,password):
                 flash('Logged In successfully',category='success')
                #  login_user(user,remember=True)
                 login_user(user)
                 #  return redirect(url_for('views.home'))
                 return redirect(url_for('views.classic'))
            else:
                flash('Incorrect password, try again !', category='error')
        else:
            flash('Mobile number not registered, please register to log in !', category='error')

    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        name1  = request.form.get('name')
        mobileNmr  = request.form.get('mobile')
        password  = request.form.get('password')
        user = User.query.filter_by(mobile=mobileNmr).first()
        logout()
        if user:
            flash('Mobile number already registered !',category='error')
        elif len(name1)<3:
            flash('Name must be contains minimum three characters',category='error')
        elif len(password)<6:
            flash('Password must be contains minimum 6 characters',category='error')
        else:
            new_user =User(name=name1,mobile=int(mobileNmr),password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            # login_user(user,remeber=True)
            flash('Signed In successfully !',category='success')
            flash('Signed In successfully',category='success')
            return redirect(url_for('auth.classic'))
        return render_template("sign_up.html")
    return render_template("sign_up.html")

@auth.route('/classicReg',methods=['POST'])
def classicReg():  
    player1 = request.form.get("player1")
    player2 = request.form.get("player2")
    player3 = request.form.get("player3")
    player4 = request.form.get("player4")
    player5 = request.form.get("player5")
    gpay = request.form.get("gpay_no")
    # if(Execute.VerifyGpayExists(gpay)==False):
    #     flash('Signed In successfully',category='success')
    #     return redirect("classic.html",remaining_slot=Execute.RemainingSlots())

    slotNo=Execute.Register(["",player1,player2,player3,player4,player5,gpay,""])
    return render_template("classicReg.html",slot_no=slotNo)

@auth.route('/classic',methods=['GET','POST'])
@login_required
def classic():
    date,time,price = Execute.MatchDetails()
    return render_template("classic.html",remaining_slot=Execute.RemainingSlots(),match_time=time,match_date=date)

# @auth.route('/matchdetails',method=['GET','POST'])
# def change_match_details():
#     nw_date = request.form.get("date")
#     nw_time = request.form.get("time")
#     nw_price = request.form.get("price")
#     Execute.ChangeMatchDetails(nw_date,nw_time,nw_price)
#     date,time,price = Execute.MatchDetails()
#     flash('Match Details changed successfully',category='success')
#     return render_template("classic.html",remaining_slot=Execute.RemainingSlots(),match_time=time,match_date=date)

