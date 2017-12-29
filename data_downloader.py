from users_dict import UsersDict
from react_dict import ReactDict
import facebook


class DataDownloader:
    def __init__(self, access_token):
        self.graph = facebook.GraphAPI(access_token=access_token, version="2.11")
        self.users_dict = UsersDict(self.graph)
        self.react_dict = ReactDict()
        self.group_id = None

    def group_list(self) -> dict:
        return self.graph.get_all_connections("me", "groups")

    def select_group(self) -> str:
        groups = list(self.group_list())
        for num, group in enumerate(groups):
            print("%d: %s (%s)" % (num, group["name"], group["id"]))
        try:
            x = int(input())
            self.group_id = groups[x]["id"]
        except ValueError:
            self.group_id = groups[0]["id"]

    def group_feed(self) -> dict:
        return self.graph.get_all_connections(self.group_id, "feed")

    def process_reacts(self, object_id) -> None:
        author_id = self.graph.get_object(object_id, fields="from{id}").get("from").get("id")
        for react in self.graph.get_all_connections(object_id, "reactions"):
            self.react_dict.add_react(author_id, react['id'], react['type'])

    def process_post(self, post) -> None:
        post_id = post["id"]
        print(post_id)
        self.process_reacts(post_id)
        for comment in self.graph.get_all_connections(post_id, "comments"):
            self.process_reacts(comment["id"])
            for response in self.graph.get_all_connections(comment["id"], "comments"):
                self.process_reacts(response["id"])

    def process_feed(self):
        for i in self.group_feed():
            self.process_post(i)