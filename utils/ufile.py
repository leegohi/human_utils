from pathlib import Path,PosixPath
from typing import Union

def get_filename(path:Union[Path,str])->str:
    return Path(path).resolve().name

