#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(filename='example.log',format='%(asctime)s %(levelname)s %(message)s')
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)


logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything

# A fichero NUEVO cada vez

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.error('And this, too')

# Config. con timestamp

logging.warning('is when this event was logged.')

# Formateado de cadenas
logging.warning('%s before you %s', 'Look', 'leap!')
x, y = 'Look', 'leap!'
logging.warning(f'{x} before you {y}')
