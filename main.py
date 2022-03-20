from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill


app = Flask(__name__)

candidates = load_candidates_from_json('candidates.json')


@app.route("/")
def index():
    return render_template('index.html', candidates=candidates)


@app.route('/candidates/<int:id>')
def candidate_profile(id):
    candidate = get_candidate(id)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def search_name(candidate_name):
    candidates, len = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, len=len)


@app.route("/skill/<skill_name>")
def find_skill(skill_name):
    candidates, len = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates, len=len, skill_name=skill_name)


if __name__ == "__main__":
    app.run(debug=True)

