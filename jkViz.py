import click
import subprocess
import os

from flask import Flask, g
app = Flask(__name__)

@app.route('/')
def hello_world():
    g.filename = os.environ["JQ_FILENAME"]
    query = '.'
    output = subprocess.check_output(["jq", query, g.filename])
    return output.decode()

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    os.environ["FLASK_APP"] = __file__
    os.environ["JQ_FILENAME"] = filename
    subprocess.check_call(["flask", "run"])

if __name__ == "__main__":
    main()