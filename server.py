from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Route for index page
@app.route('/')
def index():
    return render_template('index.html')

# Redirect all other routes to index
@app.route('/<path:subpath>')
def catch_all(subpath):
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False)
