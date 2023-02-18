import os
import pickle


class Settings:
    def __init__(self, save_dir=os.getcwd(), name="settings"):
        self.save_dir = save_dir
        self.name = name + ".ecfg" if ".ecfg" not in name else name
        self.path = os.path.join(self.save_dir, self.name).__str__()

        if not os.path.exists(self.path):
            with open(self.path, "wb") as file:
                pickle.dump(None, file=file)
                self.config = dict()
        else:
            with open(self.path, "rb") as file:
                load = pickle.load(file)
                self.config = load if load is not None else dict()

    def update_config(self, adds: dict):
        new_config = dict()
        for key in adds:
            new_config[key] = adds[key]
        for key in self.config:
            if not new_config.__contains__(key):
                new_config[key] = self.config[key]
        self.config = new_config
        return self.config

    def save_config(self):
        with open(self.path, "wb") as file:
            pickle.dump(self.config, file)

    def view_config(self):
        print(self.config)

    def get_config(self):
        return self.config