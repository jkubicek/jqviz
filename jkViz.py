import click
import subprocess
import os

from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__)
app.secret_key = "soTjK_UgaHcK8HM4nBTwFv.UvzMcNxyPXKnH_TWYoZ@Dc.*PdKxVs.kaCTtJ-UXZ"

@app.route('/')
def index():
    filename = os.environ["JQ_FILENAME"]
    jq_filter = session.get("filter", ".")
    print(f"jq_filter: {jq_filter}")
    try:
        output = subprocess.check_output(["jq", jq_filter, filename]).decode()
    except subprocess.CalledProcessError as jq_err:
        output = jq_err.output.decode()
    return render_template("index.html", json=output, filename=filename, filter=jq_filter)

@app.route('/update-filter', methods=['POST'])
def update_filter():
    session["filter"] = request.form["jq_filter"]
    return redirect(url_for("index"))

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    os.environ["FLASK_APP"] = __file__
    os.environ["JQ_FILENAME"] = filename
    subprocess.check_call(["flask", "run"])

if __name__ == "__main__":
    main()