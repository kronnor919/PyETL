from threading import Lock
import logging
from pathlib import Path
import os

class Logger:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize()
    
    def _initialize(self):
        self._logger = logging.getLogger('logger')
        self.handlers = {}
        self.log_file_path = Path(os.path.join('src' ,'logs')).resolve()
        self.log_file_path.mkdir(exist_ok=True)

        self.formatter = logging.Formatter(
            fmt='%(levelname)s - %(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:S'
        )