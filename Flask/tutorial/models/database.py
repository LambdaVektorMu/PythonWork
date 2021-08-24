# DBとの接続情報

from pymongo import MongoClient
from models.models import OnegaiContent


class MongoDB(object):
    def __init__(self, db_name, collection_name):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db.get_collection(collection_name)

    def insert_one_onegai(self, doc:OnegaiContent):
        self.collection.insert_one(doc.onegai_dict)
