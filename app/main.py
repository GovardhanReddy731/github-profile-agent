from fastapi import FastAPI
from pydantic import BaseModel

from app.github import get_user, get_repositories
from app.analyzer import get_top_repositories

app = FastAPI()


class GitHubRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {
        "message": "GitHub Profile Analyzer is running"
    }


@app.post("/analyze")
def analyze(request: GitHubRequest):

    username = request.url.rstrip("/").split("/")[-1]

    user = get_user(username)
    repositories = get_repositories(username)

    top_repositories = get_top_repositories(repositories)

    return {
        "github_url": request.url,
        "username": user["login"],
        "name": user["name"],
        "bio": user["bio"],
        "followers": user["followers"],
        "public_repos": user["public_repos"],
        "top_repositories": [
            {
                "name": repo["name"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
                "language": repo["language"]
            }
            for repo in top_repositories
        ]
    }