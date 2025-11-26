import logging

class Log:
    def __init__(self, archivo="acciones.log"):
        logging.basicConfig(
            filename=archivo,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger()

    def registrar(self, mensaje):
        self.logger.info(mensaje)
