from typing import List
from models.quoteModel import QuoteModel
from ingestors.ingestorInterface import IngestorInterface


class TextIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        res = []
        file = open(path, mode='r', encoding='utf-8-sig')
        lines = file.readlines()
        file.close()

        for quote in lines:
            body, author = quote.rstrip("\n").split(" - ")
            if body and author:
                res.append(QuoteModel(body, author))
        return res
