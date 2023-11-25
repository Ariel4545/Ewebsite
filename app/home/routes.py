from flask import Blueprint, render_template, redirect, url_for

from app.home import blueprint

home = Blueprint('home', __name__)


@blueprint.route('/')
def home():
    return render_template('home/index.html', product_name='Egon')


@blueprint.route('return-home')
def return_home():
    return redirect(url_for('.home'))
