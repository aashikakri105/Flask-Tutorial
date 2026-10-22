from flask import Flask
from uuid import UUID

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

#INTEGER CONVERTER
@app.route("/user/<int:id>")
def user(id):
    return f"User ID: {id}"

#FLOAT CONVERTER
@app.route("/price/<float:amount>")
def price(amount):
    return f"Price: {amount}"

#STRING CONVERTER
@app.route("/user/<string:name>")
def user_by_name(name):
    return f"User ID: {name}"

#PATH CONVERTER
@app.route("/files/<path:files_path>")
def files(files_path):
    return files_path

#UUID CONVERTER
@app.route("/student/<uuid:user_id>")
def student(user_id):
    return str (user_id)


if __name__ == "__main__":
    app.run(debug=True)
