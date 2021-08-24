# データベースのテーブルカラム情報を定義する

from datetime import datetime


class OnegaiContent(object):
    __collection_name__ = 'jinja'
    onegai_dict = {}
    def __init__(self) -> None:
        self.onegai_dict['title'] = ''
        self.onegai_dict['body'] = ''
        self.onegai_dict['date'] = datetime.now()

    def __init__(self, title=None, body=None, date=None):
        # お願い題名
        if title is not None:
            self.onegai_dict['title'] = title
        else:
            self.onegai_dict['title'] = ''

        # お願いの内容
        if body is not None:
            self.onegai_dict['body'] = body
        else:
            self.onegai_dict['body'] = ''

        # 日付
        if date is not None:
            self.onegai_dict['date'] = date
        else:
            self.onegai_dict['date'] = datetime.now()
