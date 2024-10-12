from typing import AnyStr, List, Optional, Type
from scholarly import scholarly
from gentopia.tools.basetool import *
import PyPDF2

# PDF Reading Tool
class PDFReaderArgs(BaseModel):
    file_path: str = Field(..., description="Path to the PDF file")
    num_pages: int = Field(None, description="Number of pages to extract (default is all pages)")

class PDFReader(BaseTool):
    name = "pdf_reader"
    description = ("Read a PDF file and extract text from it. "
                   "You can specify the number of pages to extract.")
    args_schema: Optional[Type[BaseModel]] = PDFReaderArgs

    def _run(self, file_path: AnyStr, num_pages: Optional[int] = None) -> str:
        try:
            # Open and read the PDF file
            with open(file_path, 'rb') as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                total_pages = len(reader.pages)
                pages_to_read = total_pages if num_pages is None else min(num_pages, total_pages)

                extracted_text = ""
                for page_num in range(pages_to_read):
                    page = reader.pages[page_num]
                    extracted_text += page.extract_text()

                return extracted_text if extracted_text else "No text found in the PDF."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    # Example usage of PDFReader
    pdf_tool = PDFReader()
    pdf_text = pdf_tool._run(file_path="Project-Pitch.pdf", num_pages=2)
    print(pdf_text)
