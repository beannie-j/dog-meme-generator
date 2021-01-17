import os
import subprocess

from typing import List
from ingestors.ingestorInterface import IngestorInterface
from ingestors.textIngestor import TextIngestor
from models.quoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
        # text_file = "./resource/temp.txt"
        # cmd = f"pdftotext {path} {text_file}"
        # subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        # res = TextIngestor.parse(text_file)
        # os.remove(text_file)
        # return res
