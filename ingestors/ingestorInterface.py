from models import QuoteModel
from docx import Document

import csv
import os
import subprocess


class IngestorInterface:
    @classmethod
    def can_ingest(cls, path) -> boolean:
        pass

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass


class TextIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        res = []
        file = open(path, mode='r', encoding='utf-8-sig')
        lines = file.readlines()
        for row in lines:
            res.append(QuoteModel(row.rstrip('\n').split(' - ')))
        file.close()
        return res


class CSVIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        res = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    res.append(QuoteModel(row.rstrip('\n').split(' - ')))
                    line_count += 1
            return res


class DocxIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        res = []
        document = Document(path)
        for paragraph in document.paragraphs:
            paragraph.text and res.append(
                QuoteModel(paragraph.text.split(" - ")))
        return res


class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        text_file = "./resource/temp.txt"
        cmd = f"./resource/pdftotext -layout -nopgbrk {path} {text_file}"
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        res = TextIngestor.parse(text_file)
        os.remove(text_file)
        return res
