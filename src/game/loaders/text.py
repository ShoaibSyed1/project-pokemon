import json

class TextLoader:
    def load(path, name):
        path = "assets/textboxes/" + path + ".json"

        text = None
        with open(path) as file:
            text = json.load(file)
        
        return text[name]