from datetime import datetime

def calculate_score(p):
    score = 0

    if p['description']:
        score += 2

    updated = datetime.strptime(p['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
    days = (datetime.now() - updated).days

    if days < 180:
        score += 3
    elif days < 365:
        score += 2

    if 0 < p['stars'] < 1000:
        score += 2

    if p['forks'] > 50:
        score += 2

    if p['issues'] > 5:
        score += 2

    return score


def filter_projects(projects):
    filtered = []

    for p in projects:
        updated = datetime.strptime(p['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
        days = (datetime.now() - updated).days

        if (
            0 < p['stars'] < 1000 and
            days < 365 * 2 and
            p['description'] and
            p['size'] > 10
        ):
            filtered.append(p)

    if len(filtered) < 5:
        return projects

    return filtered