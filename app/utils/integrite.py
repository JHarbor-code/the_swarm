from pathlib import Path
from pydantic import BaseModel, ValidationError

class ConfigfileNotFound(Exception): pass
class LogfileNotFound(Exception): pass

class Paths(BaseModel):
    logfile_path: Path


class Config(BaseModel):
    paths: Paths



def check_integrity():
    """
    Vérifie l'existance des fichiers : config, log

    Raises: 
        ConfigfileNotFound : si le fichier de ./res/config.json n'existe pas
        LogfileNotFound : si le fichier log (chemin mutable dans config.json) n'existe pas
        ValueError : si erreur de lecture du fichier config
    """

    ROOT = Path(__file__).resolve().parent.parent.parent

    configfile_path = ROOT / "config" / "config.json"

    if not configfile_path.exists():
        raise ConfigfileNotFound(f"Le fichier {configfile_path} n'existe pas.")
    
    try:
        data = configfile_path.read_text()
        config = Config.model_validate_json(data)

    except ValidationError as e:
        raise ValueError(f"Erreur lors de la vérification de la config : {e}") from e


    logfile_path = (ROOT / config.paths.logfile_path).resolve()
        
    if not logfile_path.exists():
        raise LogfileNotFound(f"Le fichier {logfile_path} n'existe pas.")