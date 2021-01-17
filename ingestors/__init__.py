import os
from typing import List
from ingestors.ingestorInterface import IngestorInterface
from ingestors.csvIngestor import CSVIngestor
from ingestors.docxIngestor import DocxIngestor
from ingestors.pdfIngestor import PDFIngestor
from ingestors.textIngestor import TextIngestor
from models.quoteModel import QuoteModel


class Ingestor(IngestorInterface):
    file_extensions = {'.txt', '.csv', '.pdf', '.docx'}

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        filename, extension = os.path.splitext(path)
        print(filename, "ext", extension)
        if extension not in cls.file_extensions:
            raise ValueError(f"ValueError: {extension} is not supported.")
        if extension == '.txt':
            return TextIngestor.parse(path)
        if extension == '.docx':
            return DocxIngestor.parse(path)
        if extension == '.pdf':
            return PDFIngestor.parse(path)
        if extension == '.csv':
            return CSVIngestor.parse(path)
