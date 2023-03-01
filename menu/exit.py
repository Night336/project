class Exit:
    def __init__(self, stack, player):
        self.stack = stack

    def exit(self):
        self.stack.clear()