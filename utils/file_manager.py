import json

class FileManager:
    @staticmethod
    def save_to_file(filename, data):
        with open(filename, "w") as f:
            json.dump(data, f)
    
    @staticmethod
    def load_from_file(filename):
        with open(filename, "r") as f:
            return json.load(f)