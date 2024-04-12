import os
import pathspec


def load_gitignore(repo_path):
    gitignore_path = os.path.join(repo_path, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as file:
            spec = pathspec.PathSpec.from_lines("gitwildmatch", file)
    else:
        spec = pathspec.PathSpec.from_lines("gitwildmatch", [])
    return spec
