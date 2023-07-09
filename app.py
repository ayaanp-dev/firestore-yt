from flask import Flask, render_template
from db import read_posts, get_posts, create_post

app = Flask(__name__)

@app.route('/')
def index():
    read_posts()
    posts = get_posts()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)