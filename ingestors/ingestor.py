# from typing import List
# from ingestors.ingestorInterface import IngestorInterface
# from ingestors.csvIngestor import CSVIngestor
# from ingestors.docxIngestor import DocxIngestor
# from ingestors.pdfIngestor import PDFIngestor
# from ingestors.textIngestor import TextIngestor


# class Ingestor(IngestorInterface):
#     ingestors = {DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor}

#     @classmethod
#     def parse(cls, path: str) -> List[QuoteModel]:
#         for ingestor in cls.ingestors:
#             if ingestor.can_ingest(path):
#                 return ingestor.parse(path)
