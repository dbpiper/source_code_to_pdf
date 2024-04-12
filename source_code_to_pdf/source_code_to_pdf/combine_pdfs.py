import os
import PyPDF2
from .CONSTANTS import OUTPUT_DIR


def combine_pdfs(resume_path):
    pdf_writer = PyPDF2.PdfWriter()

    resume_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        resume_path,
    )

    output_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        OUTPUT_DIR,
    )
    if resume_path:
        pdf_reader = PyPDF2.PdfReader(resume_path)
        for page in range(len(pdf_reader.pages)):
            # Add each page to the writer object
            pdf_writer.add_page(pdf_reader.pages[page])

    for repo_pdf in os.listdir(output_path):
        repo_pdf_path = os.path.join(output_path, repo_pdf)

        pdf_reader = PyPDF2.PdfReader(repo_pdf_path)
        for page in range(len(pdf_reader.pages)):
            # Add each page to the writer object
            pdf_writer.add_page(pdf_reader.pages[page])

    output_pdf_path = os.path.join(output_path, "combined.pdf")
    # Write out the merged PDF
    with open(output_pdf_path, "wb") as out:
        pdf_writer.write(out)
