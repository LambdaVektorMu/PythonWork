# DBとの接続情報

from datetime import datetime
from pymongo import MongoClient
from . import models
from models.models import OnegaiContent
from bson.objectid import ObjectId


class MongoDB(object):
    def __init__(self, db_name, collection_name):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db.get_collection(collection_name)

    # 1レコードを発見
    def select_one_onegai(self, id:str):
        return self.collection.find_one(filter={models.WISH_ID:ObjectId(id)})

    # 1レコードを挿入
    def insert_one_onegai(self, doc:OnegaiContent):
        return self.collection.insert_one(doc.onegai_dict)

    # 1レコードを更新
    def update_one_onegai(self, doc):
        return self.collection.update_one({models.WISH_ID:ObjectId(doc[models.WISH_ID])}, {'$set':doc})

    # 1レコードを削除
    def delete_one_onegai(self, id:str):
        return self.collection.delete_one(filter={models.WISH_ID:ObjectId(id)})

def cursor_2_onegai_list(cur):
    onegai_list = []
    for c in cur:
        d = {}
        d[models.WISH_ID] = c[models.WISH_ID]
        d[models.WISH_TITLE] = c[models.WISH_TITLE]
        d[models.WISH_BODY] = c[models.WISH_BODY]
        if models.WISH_DATETIME in c and type(c[models.WISH_DATETIME]) is datetime:
            d[models.WISH_DATETIME] = c[models.WISH_DATETIME].strftime('%Y年%m月%d日 %H:%M:%S')
        else:
            d[models.WISH_DATETIME] = '未設定'
        onegai_list.append(d)

    return onegai_list
