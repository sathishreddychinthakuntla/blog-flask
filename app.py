from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('projects.json') as f:
        projects = json.load(f)
    return render_template('index.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        with open('messages.txt', 'a') as f:
            f.write(f"{name}: {message}\n")
        return "Thanks for contacting!"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
