import logging

class Log:
    def __init__(self, archivo="acciones.log"):
        # Configuración básica solo una vez
        logging.basicConfig(
            filename=archivo,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger("ProyectoOro")

    def info(self, mensaje):
        self.logger.info(mensaje)

    def warning(self, mensaje):
        self.logger.warning(mensaje)

    def error(self, mensaje):
        self.logger.error(mensaje)
