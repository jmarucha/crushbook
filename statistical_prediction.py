from math import log, inf

class StatisticalPrediction:
    def __init__(self, data):
        self.attention_total = 0
        self.attention_given = {}
        self.attention_received = {}
        self.actual_data = data
        for receiver in data:
            for giver in data[receiver]:
                attention_delta = self.actual_data[receiver][giver]["total"]
                self.attention_given[giver] = self.attention_given.get(giver, 0) + attention_delta
                self.attention_received[receiver] = self.attention_received.get(receiver, 0) + attention_delta
                self.attention_total += attention_delta

    def predict(self, reciever, giver):
        return self.attention_given.get(giver, 0)*self.attention_received.get(reciever, 0)/self.attention_total

    def compare(self, reciever, giver):
        predicted = self.predict(reciever, giver)
        actual = self.actual(reciever, giver)
        try:
            return log(actual/predicted)
        except ValueError:
            return -inf
        except ZeroDivisionError:
            return -inf
    
    def actual(self, reciever, giver):
        return self.actual_data.get(reciever, {}) \
            .get(giver, {}).get("total", 0)