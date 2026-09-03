import requests

GITHUB_API = "https://api.github.com"


def get_user(username: str):
    url = f"{GITHUB_API}/users/{username}"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("GitHub user not found")

    return response.json()


def get_repositories(username: str):
    url = f"{GITHUB_API}/users/{username}/repos"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Could not fetch repositories")

    return response.json()