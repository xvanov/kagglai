
class InvalidTuningMethod(Exception):
    def __init__(self, method, message="Tuning Method is invalid"):
        self.method = method
        self.message = f"{method} is an invalid tuning method"
        super().__init__(self.message)
