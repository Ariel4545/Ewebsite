from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint(__name__, 'views')


@views.route('/')
def home():
    return render_template('index.html', product_name='Egon')


@views.route('/<product>')
def product_page(product):
    """
    args = request.args
    name = args.get('name')
    """
    if product == 'EgonTE' or product == 'EgonCalc' or product == 'EgonDS':
        if product == 'EgonTE':
            product_type = 'Text editor'
        elif product == 'EgonCalc':
            product_type = 'Calculator(s)'
        elif product == 'EgonDS':
            product_type = 'Data science Gui(s)'
        return render_template('product_page.html', product_name=product, pt=product_type)
    else:
        return redirect(url_for('.home'))


@views.route('return-home')
def return_home():
    return redirect(url_for('.home'))
