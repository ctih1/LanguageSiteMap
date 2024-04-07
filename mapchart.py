import json
from utils import *

class Map:
    def __init__(self):
        self.config = {}
        self.settings = json.load(open("resources/settings.json","r"))
    def create(self,groups: list):
        """_summary_

        Args:
            groups (dict):
                Groups
                example:
                    [{"failed": "color": "#ff0000", "countries": "us"...}]
        """
        self.config["groups"]={}
        for group in groups:
            self.config["groups"][group.get("color",None)] = {}
            self.config["groups"][group.get("color",{})]["label"] = group.get("title","Not defined")
            self.config["groups"][group.get("color",{})]["paths"] = group.get("countries",[])
        self.config.update(self.settings)
        return format_config(str(self.config))
    
