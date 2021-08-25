# データベースのテーブルカラム情報を定義する

from datetime import datetime


# 願い事
WISH_ID = '_id'
WISH_TITLE = 'title'
WISH_BODY = 'body'
WISH_DATETIME = 'date'

class OnegaiContent(object):
    onegai_dict = {}
    def __init__(self) -> None:
        self.onegai_dict[WISH_TITLE] = ''
        self.onegai_dict[WISH_BODY] = ''
        self.onegai_dict[WISH_DATETIME] = datetime.now()

    def __init__(self, title=None, body=None, date=None):
        # お願い題名
        if title is not None:
            self.onegai_dict[WISH_TITLE] = title
        else:
            self.onegai_dict[WISH_TITLE] = ''

        # お願いの内容
        if body is not None:
            self.onegai_dict[WISH_BODY] = body
        else:
            self.onegai_dict[WISH_BODY] = ''

        # 日付
        if date is not None:
            self.onegai_dict[WISH_DATETIME] = date
        else:
            self.onegai_dict[WISH_DATETIME] = datetime.now()
