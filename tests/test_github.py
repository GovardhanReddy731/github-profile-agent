from app.github import get_user, get_repositories


def test_get_user(mocker):

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "login": "testuser",
        "name": "Test User",
        "followers": 10
    }

    mocker.patch(
        "app.github.requests.get",
        return_value=mock_response
    )

    result = get_user("testuser")

    assert result["login"] == "testuser"
    assert result["name"] == "Test User"
    assert result["followers"] == 10


def test_get_repositories(mocker):

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = [
        [
            {
                "name": "project-a",
                "stargazers_count": 10
            }
        ],
        []
    ]

    mocker.patch(
        "app.github.requests.get",
        return_value=mock_response
    )

    result = get_repositories("testuser")

    assert len(result) == 1
    assert result[0]["name"] == "project-a"