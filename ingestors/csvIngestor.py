import csv
from typing import List
from models.quoteModel import QuoteModel
from ingestors.ingestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        res = []
        with open(path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                res.append(QuoteModel(row['body'], row['author']))
            return res
