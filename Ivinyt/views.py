from flask import Blueprint, render_template
from flask_login import login_required,current_user
from .Execute import Execute

views = Blueprint('views',__name__)

# @views.route('/')
# @login_required
# def home():
#     return render_template("home.html")

@views.route('/')
@login_required
def classic():
    return render_template("classic.html",remaining_slot=Execute.RemainingSlots())


# @views.route('/admin')
# @login_required
# def admin():
#     return render_template("adminuser.html",df=Execute.ClassicRegistration())