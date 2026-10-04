class DataController:
    def __init__(self) -> None:
        self.initialized = True
    
    def process_data(self, data: dict) -> dict:
        return data