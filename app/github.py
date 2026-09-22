import requests

GITHUB_API = "https://api.github.com"
TIMEOUT = 10


def get_user(username: str):
    url = f"{GITHUB_API}/users/{username}"

    response = requests.get(url, timeout=TIMEOUT)

    if response.status_code == 404:
        raise Exception("GitHub user not found")

    if response.status_code == 403:
        raise Exception("GitHub API rate limit exceeded")

    if response.status_code != 200:
        raise Exception("Failed to fetch GitHub user")

    return response.json()


def get_repositories(username: str):
    url = f"{GITHUB_API}/users/{username}/repos"

    response = requests.get(
        url,
        params={
            "per_page": 100,
            "page": 1
        },
        timeout=TIMEOUT
    )

    if response.status_code == 404:
        raise Exception("GitHub user not found")

    if response.status_code == 403:
        raise Exception("GitHub API rate limit exceeded")

    if response.status_code != 200:
        raise Exception("Failed to fetch repositories")

    return response.json()