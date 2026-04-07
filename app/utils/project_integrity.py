import os 
from pathlib import Path
import json

class ConfigfileNotFound(): pass
class LogfileNotFound(): pass

ROOT = Path(__file__).parent.parent.parent

config_file_path = ROOT / "config" / "config.json"

def check_integrity():
    """
    Vérifie l'existance des fichiers : config, log

    Raises: 
        ConfigfileNotFound : si le fichier de ./res/config.json n'existe pas
        LogfileNotFound : si le fichier log (chemin mutable dans config.json) n'existe pas
        ValueError : si erreur de lecture du fichier config
    """

    if not config_file_path.exists():

        return ConfigfileNotFound
    
    try:
        with open(config_file_path, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Parsage du fichier config.json impossible")

    log_file_path = Path(data["paths"]["logfile"])
        
    if not log_file_path.exists():

        return LogfileNotFound