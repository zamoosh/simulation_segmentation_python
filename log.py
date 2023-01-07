class Log:
    def __init__(self, time, content):
        self.time = time
        self.content = content

    def __str__(self):
        return f'{self.content}'
