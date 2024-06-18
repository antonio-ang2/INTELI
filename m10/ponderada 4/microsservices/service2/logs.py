# src/logs.py
import logging

# Altera o arquivo de logs para salvar as mensagens em um arquivo
logging.basicConfig(filename='logs/app.log', level=logging.DEBUG)

logger = logging.getLogger(__name__)

def log_info(message: str):
    logger.info(message)

def log_debug(message: str):
    logger.debug(message)

def log_warning(message: str):
    logger.warning(message)

def log_error(message: str):
    logger.error(message)

def log_critical(message: str):
    logger.critical(message)
