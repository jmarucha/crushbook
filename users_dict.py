class UsersDict(dict):
    def __init__(self, graph):
        self.graph = graph
        super().__init__()
    def get(self, user_id: str):
        if user_id not in self:
            self[user_id] = self.graph.get_object(user_id)
        return self[user_id]