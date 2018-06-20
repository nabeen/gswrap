#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser
from gswrap.Gswrap import Gswrap

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_FILE = os.path.join(CURRENT_DIR, 'keys', 'keys.json')
CREDENTIAL_FILE = os.path.join(CURRENT_DIR, 'keys', 'credential.json')


def main(sheet_id: str, sheet_name: str) -> dict:
    gs = Gswrap(KEY_FILE, CREDENTIAL_FILE)
    return gs.get_value(sheet_id, sheet_name + '!A:CK')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('sheet_id',
                        metavar='sheet_id',
                        type=str,
                        help='an string of Spread Sheet ID.')
    parser.add_argument('sheet_name',
                        metavar='sheet_name',
                        type=str,
                        help='an string of Spread Sheet name.')
    args = parser.parse_args()
    items = main(args.sheet_id, args.sheet_name)

    for item in items:
        print(item)
