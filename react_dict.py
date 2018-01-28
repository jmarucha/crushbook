class ReactDict(dict):
    def add_react(self, reciever_id: str, giver_id: str, react_type: str) -> None:
        if reciever_id not in self:
            self[reciever_id] = {}
        if giver_id not in self[reciever_id]:
            self[reciever_id][giver_id] = {}
        if react_type not in self[reciever_id][giver_id]:
            self[reciever_id][giver_id][react_type] = 0
        if "total" not in self[reciever_id][giver_id]:
            self[reciever_id][giver_id]["total"] = 0
        self[reciever_id][giver_id][react_type] += 1
        self[reciever_id][giver_id]["total"] += 1
