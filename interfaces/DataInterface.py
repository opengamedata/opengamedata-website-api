## import standard libraries
import abc
import logging
from datetime import datetime
from pprint import pformat
from typing import Any, Dict, List, Tuple, Optional, Union

# import local files
from config.config import settings as default_settings
from interfaces.Interface import Interface
#from schemas.Event import Event
#from schemas.IDMode import IDMode
#from schemas.TableSchema import TableSchema

class DataInterface(Interface):

    # *** ABSTRACTS ***

    # *** BUILT-INS ***
    def __init__(self, config:Dict[str,Any]):
        super().__init__(config=config)

    def __del__(self):
        self.Close()

    # *** PUBLIC STATICS ***

    # *** PUBLIC METHODS ***

    # *** PROPERTIES ***

    # *** PRIVATE STATICS ***

    # *** PRIVATE METHODS ***