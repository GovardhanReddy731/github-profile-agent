from app.analyzer import get_top_repositories


def test_get_top_repositories():

    repositories = [
        {
            "name": "project-a",
            "stargazers_count": 10
        },
        {
            "name": "project-b",
            "stargazers_count": 100
        },
        {
            "name": "project-c",
            "stargazers_count": 50
        }
    ]

    result = get_top_repositories(repositories)

    assert result[0]["name"] == "project-b"
    assert result[1]["name"] == "project-c"
    assert result[2]["name"] == "project-a"