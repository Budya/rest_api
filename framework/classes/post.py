
class Post:
    def __init__(self, post):
        self.userId = post['userId']
        self.id = post['id']
        self.title = post['title']
        self.body = post['body']

    def is_id_equal(self, id_):
        if self.id == id_:
            return True
        else:
            return False

    def is_user_id_equal(self, user_id):
        if self.userId == user_id:
            return True
        else:
            return False

    def is_title_equal(self, title_):
        if self.title == title_:
            return True
        else:
            return False

    def is_body_equal(self, body_):
        if self.body == body_:
            return True
        else:
            return False
