from typing import List
from models.quoteModel import QuoteModel
from abc import ABC, abstractclassmethod


class IngestorInterface(ABC):

    file_extensions = {'txt', 'csv', 'pdf', 'docx'}

    @classmethod
    def can_ingest(cls, path) -> bool:
        extension = path.split('.')[-1]
        return extension in cls.file_extensions

    @abstractclassmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
