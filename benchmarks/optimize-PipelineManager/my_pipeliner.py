#!/usr/bin/env python2
# coding: utf-8

from sys import stdout
from logging import Logger, StreamHandler, Formatter
from pypelinin import Pipeliner


def main():
    logger = Logger('Pipeliner')
    handler = StreamHandler(stdout)
    formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - '
                          '%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    pipeliner = Pipeliner(api='tcp://localhost:12345',
                          broadcast='tcp://localhost:12346', logger=logger)
    pipeliner.start()

if __name__ == '__main__':
    main()

