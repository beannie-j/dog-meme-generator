import csv
from typing import List
from models.quoteModel import QuoteModel
from ingestors.ingestorInterface import IngestorInterface


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
