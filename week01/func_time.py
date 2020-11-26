from datetime import datetime
import logging
from pathlib import Path

def functimelog():
    path = Path(f"D:/huoya/python/week1/python-{datetime.now().strftime('%Y-%m-%d')}")
    path.exists()
    if not path.exists() :
        path.mkdir()
    logging.basicConfig(filename=f"D:/huoya/python/week1/python-{datetime.now().strftime('%Y-%m-%d')}/test.log",level=logging.DEBUG,datefmt='%Y-%m-%d %H:%M:%S',format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s')
    logging.debug(f'调用的时间为{datetime.now()}')

functimelog()
