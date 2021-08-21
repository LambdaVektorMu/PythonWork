# DBとの接続情報

from pymongo import MongoClient


class MongoDB(object):
    def __init__(self, db_name, collection_name):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db.get_collection(collection_name)
