import os

from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route("/")
def get_home():
    return render_template("index.html", section_id="about", active_page="about")


@app.route("/skills")
def skills():
    return render_template("skills.html", section_id="skills", active_page="skills")


@app.route("/projects")
def projects():
    return render_template(
        "projects.html", section_id="projects", active_page="projects"
    )


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static/assets"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    app.run(debug=True)
