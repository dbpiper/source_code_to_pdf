import os
from .CONSTANTS import ROOT_DIR, OUTPUT_DIR
import shutil

from .create_pdf_from_repo import create_pdf_from_repo


def create_pdfs_from_repos():
    rood_dir = os.path.expanduser(ROOT_DIR)
    # Iterate through each repository directory
    for repo in os.listdir(rood_dir):
        repo_path = os.path.join(rood_dir, repo)
        if os.path.isdir(repo_path):
            repo_pdf_name = f"{repo}.pdf"
            print(f"Found repo: {repo} to make into a PDF")
            repo_pdf = create_pdf_from_repo(repo_path)
            repo_pdf.output(repo_pdf_name)

            current_repo_pdf_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "..",
                repo_pdf_name,
            )
            output_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "..",
                OUTPUT_DIR,
                repo_pdf_name,
            )
            print("current_repo_pdf_path:", current_repo_pdf_path)
            print("output_path:", output_path)
            shutil.move(current_repo_pdf_path, output_path)
            # Save the PDF named after the repository
            print(f"Made repo: {repo} into a PDF")
