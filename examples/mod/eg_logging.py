import logging

logging.basicConfig(filename='/path/to/logging.log',
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)
