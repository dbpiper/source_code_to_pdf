import os
from pathspec import PathSpec
from fpdf import FPDF
from .load_gitignore import load_gitignore


# Function to create a PDF for a single repository
def create_pdf_from_repo(repo_path, repo_name):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    spec: PathSpec = load_gitignore(repo_path)

    # Walk through the repository directory
    for subdir, dirs, files in os.walk(repo_path):
        files = [
            f for f in files if not spec.match_file(os.path.join(subdir, f))
        ]
        dirs[:] = [
            d for d in dirs if not spec.match_file(os.path.join(subdir, d))
        ]

        for file in files:
            file_path = os.path.join(subdir, file)
            try:
                # Add a page for each file
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                # Add the file path as a subtitle
                pdf.cell(200, 10, txt=file_path, ln=True)

                # Open and read the file
                with open(file_path, "r", encoding="utf-8") as f:
                    for line in f:
                        pdf.cell(200, 10, txt=line, ln=True)
            except Exception as e:
                print(f"Failed to add {file_path}: {e}")

    # Save the PDF named after the repository
    pdf.output(f"{repo_name}.pdf")
