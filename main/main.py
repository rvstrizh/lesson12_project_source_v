from flask import Blueprint, render_template, request
from functions import load_posts

main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.route('/')
def main():
    return render_template('index.html')


@main_blueprint.route('/search')
def search():
    search_by = request.args['s']
    posts = [x for x in load_posts() if search_by.lower() in x['content'].lower()]
    return render_template('post_list.html', search_by=search, posts=posts)
