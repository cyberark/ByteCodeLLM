class BaseHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def handle(self):
        raise NotImplementedError("This method must be implemented by a subclass")