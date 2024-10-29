class MockModel:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs




    def generate(self, question):
        return question