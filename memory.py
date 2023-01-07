class Memory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.left_memory = capacity
        self.page_size = None
        self.page_left = None
        self.page_count = None
