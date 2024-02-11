from loguru import logger
import sys

def filtro_de_senha(record):
    if 'senha' in record['message']:
        return False
    return True

logger.remove()

logger.add(
    sys.stderr,
    format='{time} <r>{level}</r> <g>{message}</g> {file} {line}',
    filter= filtro_de_senha,
    level='DEBUG'
)

logger.debug('Debug')

logger.info('Info')

logger.warning('Warning')

logger.critical('senha')

logger.error('Error')

