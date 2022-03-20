import json

candidates = []

def load_candidates_from_json(path):
    """
    возвращает список всех кандидатов
    """
    global candidates
    with open(path, 'r', encoding='UTF-8') as fp:
        candidates = json.load(fp)
        return candidates


def get_candidate(candidate_id):
    """
    возвращает одного кандидата по его id
    """
    for candidate in candidates:
        if candidate_id == candidate["id"]:
            return candidate
    return {"not_found": "Ушел на обед"}


def get_candidates_by_name(candidate_name):
    """
    возвращает кандидатов по имени
    """
    candidates_names = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            candidates_names.append(candidate)
    return candidates_names, len(candidates_names)


def get_candidates_by_skill(skill_name):
    """
    возвращает кандидатов по навыку
    """
    candidates_with_skills = []
    for candidate in candidates:
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill_name.lower() in candidate_skills:
            candidates_with_skills.append(candidate)
    return candidates_with_skills, len(candidates_with_skills)


