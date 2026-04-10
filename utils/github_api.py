import requests

def search_github_projects(keyword):
    url = f"https://api.github.com/search/repositories?q={keyword}&per_page=50"

    response = requests.get(url)
    data = response.json()

    projects = []

    for item in data['items']:
        project = {
            "name": item['name'],
            "owner": item['owner']['login'],
            "stars": item['stargazers_count'],
            "forks": item['forks_count'],
            "description": item['description'] or "",
            "url": item['html_url'],
            "updated_at": item['updated_at'],
            "created_at": item['created_at'],
            "issues": item['open_issues_count'],
            "size": item['size']
        }
        projects.append(project)

    return projects