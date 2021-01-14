import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    filename='app.log'
)

a = 0
b = 5

cur_user = 'boof958'

try:
    c = b / a
except:
    logging.error('Exception occured: ', exc_info=True)
    # logging.exception ~= logging.error(exc_info=True). But it works only with exception level. You won't see terminal
    #output.