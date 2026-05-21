from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    links = [
        {"name": "Google", "url": "https://www.google.com"},
        {"name": "GitHub", "url": "https://github.com"},
        {"name": "Python", "url": "https://www.python.org"},
    ]
    return render_template('index.html', page_title='My Links', links=links)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
