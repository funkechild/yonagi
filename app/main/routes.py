from flask import render_template
from app.main import bp
from flask_babel import _


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@bp.route('/bootstrap_playground')
def bootstrap_playground():
    return render_template('bootstrap-playground.html', title=_('Bootstrap Playground'))