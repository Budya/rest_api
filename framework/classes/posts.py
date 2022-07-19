
class Posts:
    def __init__(self, list_of_posts):
        self.posts = list_of_posts

    def is_sorted_by_id(self):
        sorted_list = sorted(self.posts, key=lambda x: x['id'])
        if sorted_list == self.posts:
            return True
        else:
            return False
