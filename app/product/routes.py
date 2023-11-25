from flask import Blueprint, render_template, redirect, url_for

from app.product import blueprint

product = Blueprint('product', __name__)


@blueprint.route('/<product>')
def product_page(product):
    """
    args = request.args
    name = args.get('name')
    """
    base_link = 'https://github.com/Ariel4545/'
    product = product.capitalize()
    if product == 'Egonte' or product == 'Egoncalc' or product == 'Egonds':
        if product == 'Egonte':
            product, product_type = 'EgonTE', 'Text editor'
            content = open('data/product_content/ete.text', 'r')
            link = f'{base_link}text_editor'
        elif product == 'Egoncalc':
            product, product_type = 'EgonCalc', 'Calculator(s)'
            content = open('data/product_content/ecalc.text', 'r')
            link = f'{base_link}calculators'
        elif product == 'Egonds':
            product, product_type = 'EgonDS', 'Data science Gui(s)'
            content = open('data/product_content/edata_science.text', 'r')
            link = f'{base_link}Edata_science'

        content = content.readlines()
        return render_template('product/product_page.html', product_name=product, pt=product_type, c=content, link=link)
    else:
        return redirect(url_for('home_blueprint.home'))
