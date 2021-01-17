import os
import subprocess

from docx import Document
from typing import List
from models.quoteModel import QuoteModel
from ingestors.ingestorInterface import IngestorInterface


class DocxIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        res = []
        document = Document(path)
        for paragraph in document.paragraphs:
            paragraph.text and res.append(
                QuoteModel(paragraph.text.split(" - ")))
        return res
