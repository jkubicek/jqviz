import click
import subprocess
import os

from flask import Flask, g, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    g.filename = os.environ["JQ_FILENAME"]

    g.filter = '.'
    
    output = subprocess.check_output(["jq", g.filter, g.filename]).decode()
    return render_template("index.html", json=output, filename=g.filename, filter=g.filter)

@app.route('/update-filter', methods=['POST'])
def update_filter():
    g.filter = request.form["jq_filter"]
    return redirect(url_for("index"))

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    os.environ["FLASK_APP"] = __file__
    os.environ["JQ_FILENAME"] = filename
    subprocess.check_call(["flask", "run"])

if __name__ == "__main__":
    main()