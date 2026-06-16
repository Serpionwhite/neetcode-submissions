class Logger:

    def __init__(self):
        self.timestamp_keeper = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.timestamp_keeper:
            self.timestamp_keeper[message] = timestamp
        else:
            difference = timestamp - self.timestamp_keeper[message]
            if difference >= 10:
                self.timestamp_keeper[message] = timestamp
            else:
                return False

        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
