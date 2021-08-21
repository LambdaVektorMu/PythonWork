# データベースのテーブルカラム情報を定義する

from datetime import datetime


class OnegaiContent(object):
    __collection_name__ = 'jinja'
    def __init__(self) -> None:
        self.title = ''
        self.body = ''
        self.date = datetime.now()

    def __init__(self, title=None, body=None, date=None):
        # お願い題名
        if title is not None:
            self.title = title
        else:
            self.title = ''

        # お願いの内容
        if body is not None:
            self.body = body
        else:
            self.body = ''

        # 日付
        if date is not None:
            self.date = date
        else:
            self.date = datetime.now()
