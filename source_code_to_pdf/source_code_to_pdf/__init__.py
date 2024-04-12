from .create_pdfs_from_repos import create_pdfs_from_repos

__name__ == "__main__"
__all__ = ["train", "forecast", "saturn_utils", "saturn_forecaster"]


def main():
    print("Scanning for repos to make into PDFs.")
    create_pdfs_from_repos()
    print("PDF generation complete.")
