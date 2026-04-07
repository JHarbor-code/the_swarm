import json
from pathlib import Path 
import os

class ConfigManager:
    
    def __init__(self):
        
        self.root = Path(__file__).parent.parent
        self.paths = {
            "phenotype" : self.root / "config" / "phenotype.json"
        }
        


    
    def check_files(self):

        for name, path in self.paths.items():
            if not 