import logging

logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('This is a debug message')
logging.info('This is an INFO message')
logging.warning('This is a WARNING message')
logging.error('This is an ERROR message')
