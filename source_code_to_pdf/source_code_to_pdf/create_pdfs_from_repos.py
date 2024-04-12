import os
from .CONSTANTS import ROOT_DIR

from .create_pdf_from_repo import create_pdf_from_repo


def create_pdfs_from_repos():
    rood_dir = os.path.expanduser(ROOT_DIR)
    # Iterate through each repository directory
    for repo in os.listdir(rood_dir):
        repo_path = os.path.join(rood_dir, repo)
        if os.path.isdir(repo_path):
            print(f"Found repo: {repo} to make into a PDF")
            create_pdf_from_repo(repo_path, repo)
            print(f"Made repo: {repo} into a PDF")
