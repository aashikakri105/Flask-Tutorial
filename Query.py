from flask import Flask, request

app = Flask(__name__)

#READ QUERY PARAMETERS WITH DEFAULT VALUE
@app.route("/search")
def search():
    name = request.args.get("name","Guest")                         #MULTIPLE QUERY PARAMETERS
    course = request.args.get("course","UnKnown")
    return f"{name} is learning {course}"

if __name__ == "__main__":
    app.run(debug=True)