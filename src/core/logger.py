from threading import Lock
import logging
from pathlib import Path
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime
from typing import List

class Logger:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self._logger = logging.getLogger('logger')
        self.handlers = {}
        self.log_file_path = Path(os.path.join('src' ,'logs')).resolve()
        self.log_file_path.mkdir(exist_ok=True)

        self.formatter = logging.Formatter(
            fmt='%(levelname)s - %(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:S'
        )

        self.stream_handler = logging.StreamHandler()
        self.stream_handler.set_name('stream_handler')
        self.stream_handler.setFormatter(self.formatter)
        self.stream_handler.setLevel(logging.DEBUG)
        self.handlers[self.stream_handler.name] = self.stream_handler

        filename = Path(f'{datetime.now().strftime('%Y-%m-%d')}.log')
        self.file_handler = RotatingFileHandler(
            filename=self.log_file_path / filename,
            maxBytes=25*1024*1024,
            backupCount=7,
            encoding='utf-8'
        )
        self.file_handler.set_name('file_handler')
        self.file_handler.setFormatter(self.formatter)
        self.file_handler.setLevel(logging.INFO)
        self.handlers[self.file_handler.name] = self.file_handler

        self.updateLoggerHandlers()

    def updateLoggerHandlers(self):
        [self._logger.addHandler(hdlr) for hdlr in self.handlers.values() if hdlr not in self._logger.handlers]

    def addHandler(self, hdlr: logging.Handler):
        self.handlers[hdlr] = hdlr
        self.updateLoggerHandlers()

    def addHandlers(self, hdlrs: List[logging.Handler]):
        for hdlr in hdlrs:
            self.addHandler(hdlr)

    def getHandler(self, name: str):
        return self.handlers[name]

    def removeHandler(self, name: str):
        handler = self.getHandler(name)
        if handler:
            del self.handlers[name]
            self._logger.removeHandler(handler)
    
    def modifyHandler(self, name: str, modify_func):
        handler = self.getHandler(name)
        if handler:
            new_handler = modify_func(name)
            
            del self.handlers[name]
            self.handlers[new_handler.name] = new_handler