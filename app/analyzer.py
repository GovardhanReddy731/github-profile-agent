def get_top_repositories(repositories, limit=5):

    sorted_repositories = sorted(
        repositories,
        key=lambda repo: repo["stargazers_count"],
        reverse=True
    )

    return sorted_repositories[:limit]