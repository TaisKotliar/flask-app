from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    if request.method == 'POST':
        name = request.form.get('name')
    return render_template('index.html', name=name)


@app.route('/about')
def about():
    return 'About Page'

@app.route('/contact')
def contact():
    return 'Contact Page'

if __name__ == '__main__':
    app.run(debug=True)