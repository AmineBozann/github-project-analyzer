from flask import Flask, render_template, request
from utils.github_api import search_github_projects
from utils.scoring import calculate_score, filter_projects
from utils.ml import apply_kmeans
from utils.database import create_db, insert_project
import os

app = Flask(__name__)

create_db()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']

    projects = search_github_projects(keyword)
    projects = filter_projects(projects)

    for p in projects:
        p['score'] = calculate_score(p)
        insert_project(p)  # database kaydet

    projects = sorted(projects, key=lambda x: x['score'], reverse=True)

    projects = apply_kmeans(projects)

    return render_template("results.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))