import logging
import os

class LoggerApp:
    def __init__(self):
        ruta_log = os.path.join(os.path.dirname(os.path.dirname(__file__)), "app.log")
        logging.basicConfig(
            filename=ruta_log,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%d/%m/%Y %H:%M:%S"
        )
        self._logger = logging.getLogger("app_logger")

    def info(self, mensaje):
        self._logger.info(mensaje)

    def warning(self, mensaje):
        self._logger.warning(mensaje)

    def error(self, mensaje):
        self._logger.error(mensaje)
