import settingsmanager
import os


class Label:
    def __init__(self, name, sublabels=None, action=None, save_path=os.curdir, title=None):
        self.settings = settingsmanager.Settings(save_dir=save_path, name=name)
        self.sublabels = list() if not isinstance(sublabels, (list, tuple)) else list(sublabels)
        self.name = name
        self.action = action
        self.title = title
        self.settings.update_config(adds={
                "name": self.name,
                "sublabels": self.sublabels,
                "action": self.action,
                "arrow": "->",
                "title": title
        })
        self.config = self.settings.get_config()

    def add_sublabel(self, sublabel):
        if isinstance(sublabel, Label):
            self.config["sublabels"].append(sublabel)
        elif isinstance(sublabel, (list,tuple)):
            for label in sublabel:
                self.add_sublabel(label)
        else:
            raise TypeError("sublabel must be <Label | List of Label | Tuple of Label>")
        self.settings.save_config()

    def print_table(self, level=0):
        print("\t"*level, end="")
        print(self.config["name"])
        if len(self.config["sublabels"]) > 0:
            for i, label in enumerate(self.config["sublabels"]):
                label.print_table(level+1)

    def run_action(self, args):
        self.config["action"](args)

    def run_menu(self):
        while len(self.config["sublabels"]):
            print("0) Exit")
            for j, label in enumerate(self.config["sublabels"]):
                print("{}) {}".format(j+1, label.name))
            inp = self.get_inp(type_="number")
            if inp == 0: break
            if 0 <= inp <=len(self.config["sublabels"]):
                return self.config["sublabels"][inp-1].run_menu()
            else:
                print("error")
        if len(self.config["sublabels"]) == 0:
            print(self.config["title"])
            out = self.get_inp(type_="string")
            self.config["action"](out)

    def get_inp(self, type_):
        arguments = input(self.config["arrow"])
        if type_ == "number":
            try:
                return int(arguments)
            except:
                return "$"
        elif type_ == "string":
            return arguments


spth = "C:\\Users\\Enterprice\\Documents\\Programing\\Projects\\Algoritms-and-Libraires\\Libraries\\interactivecmd\\cfgs"
a = Label(
    name="Menu",
    sublabels=(
        Label(
            name="Run compiler with last parameters",
            save_path=spth,
        ),
        Label(
            name="Run compiler",
            save_path=spth,
        ),
        Label(
            name="Settings",
            sublabels=(
                Label(
                    name="Console settings",
                    save_path=spth,
                    sublabels=(
                        Label(
                            name="View parameters",
                            save_path=spth,
                        ),
                    ),
                ),
                Label(
                    name="Compiler settings",
                    save_path=spth,
                ),
            ),
            save_path=spth,
        ),
    ),
    save_path=spth,
)
a.run_menu()