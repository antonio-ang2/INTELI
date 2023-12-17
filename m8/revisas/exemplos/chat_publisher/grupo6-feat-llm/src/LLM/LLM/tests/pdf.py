from abc import ABC, abstractmethod
from langchain.document_loaders import PyPDFLoader, TextLoader, DirectoryLoader


class AbstractLoader(ABC):
    def __init__(self, loader):
        self.path = f"./data/"
        self.loader = loader
    
    @abstractmethod
    def load(self):
        pass

loaders = {
    "pdf": PyPDFLoader,
    "txt": TextLoader,
    "/": DirectoryLoader
}

def process_document(path):
    
    loader = DirectoryLoader("./data/", glob="")