from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Flask App!"
 
@app.route("/templates")
def hello(yogesh):
    return render_template(
        'Html.html',name=yogesh)
if __name__ == "__main__":
    app.run()

