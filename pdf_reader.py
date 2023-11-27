## pdf_reader.py
import PyPDF2
from typing import Union
import streamlit as st

class PDFReader:
    def read_pdf(self, file: Union[st.file_uploader, str]) -> str:
        """
        Reads a PDF file and returns its content as a string.

        Parameters:
        file (Union[UploadedFile, str]): The PDF file to read. Can be a Streamlit UploadedFile (from file_uploader) or a string path to a file.

        Returns:
        str: The content of the PDF file.
        """
        if isinstance(file, st.file_uploader):
            # If the file is a Streamlit UploadedFile, we need to convert it to a byte stream
            pdf_file = PyPDF2.PdfFileReader(file)
        else:
            # If the file is a string path, we can directly read it
            with open(file, 'rb') as f:
                pdf_file = PyPDF2.PdfFileReader(f)

        content = ""
        for page_num in range(pdf_file.getNumPages()):
            content += pdf_file.getPage(page_num).extractText()

        return content
