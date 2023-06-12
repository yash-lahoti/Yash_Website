from flask import render_template, request, Flask
from photography import photography_blueprint

application = Flask(__name__, static_url_path='/static')
application.register_blueprint(photography_blueprint, url_prefix='')
print(application.url_map)


@application.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        data = dict()
        data['name'] = request.form['Name']
        data['email'] = request.form['Email']
        data['message'] = request.form['Message']
    return render_template('index.html')

@application.route("/aboutme.html/")
def aboutme():
    return render_template('aboutme.html')

@application.route("/projects.html/")
def projects():
    return render_template('projects.html')

@application.route("/research.html/")
def research():
    return render_template('research.html')

# run the application
if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0', port=5000)
