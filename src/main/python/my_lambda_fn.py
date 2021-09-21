#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# vim: tabstop=2 shiftwidth=2 softtabstop=2 expandtab

import sys
import os

import pymysql

DATABASE_PORT = os.getenv('databasePort')
DDB_TABLE_NAME = os.getenv('ddbTableName')

def lambda_handler(event, context):
  print('[INFO] databasePort: {}'.format(DATABASE_PORT), file=sys.stderr)
  print('[INFO] ddbTableName: {}'.format(DDB_TABLE_NAME), file=sys.stderr)


if __name__ == '__main__':
  event = {}
  lambda_handler(event, {})
