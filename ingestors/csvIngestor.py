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
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                res.append(QuoteModel(row['body'], row['author']))
            return res
