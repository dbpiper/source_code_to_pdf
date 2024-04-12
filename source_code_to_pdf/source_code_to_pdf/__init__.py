from .create_pdfs_from_repos import create_pdfs_from_repos
from .combine_pdfs import combine_pdfs

from .CONSTANTS import RESUME_PATH

__name__ == "__main__"
__all__ = []


def create_multiple_pdfs():
    print("Scanning for repos to make into PDFs.")
    create_pdfs_from_repos()
    print("PDF generation complete.")


# def combine_pdfs_script():
#     combine_pdfs()


# def combine_pdfs_with_resume_script():
#     combine_pdfs()


def main():
    create_multiple_pdfs()
    combine_pdfs(RESUME_PATH)
