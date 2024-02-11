from logging import error, warning, debug, info, critical
from logging import basicConfig
from logging import DEBUG
from logging import FileHandler, StreamHandler
from logging import Formatter



formater_file_handler = Formatter(
    '%(asctime)s:%(name)s:%(levelname)s:%(message)s'
)
file_handler= FileHandler("meus_logs.txt", "w")
file_handler.setLevel(DEBUG)
file_handler.setFormatter(formater_file_handler)

strem_handler = StreamHandler()

# Configure logging
basicConfig(
    level=DEBUG,
    encoding='utf-8',
    format='%(levelname)s:%(asctime)s:%(message)s',
    handlers=[file_handler,strem_handler]    
)

# Log messages
error('Ihh, deu erro!')
warning('Algo de errado, não está certo!')
debug('entrei aqui!')
debug('sai daqui')
info('Pessoa logou')
critical('senha 123')
