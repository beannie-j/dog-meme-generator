from models import QuoteModel


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
        for line in lines:
            res.append(QuoteModel(line.rstrip('\n').split(' - ')))
        file.close()
        return res


class CSVIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass


class DocxIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass


class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
