#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Timewarrior adapter for `argos <https://github.com/p-e-w/argos>`."""
# <bitbar.title>timewarrior</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Tobias Schmidl</bitbar.author>
# <bitbar.author.github>schtobia</bitbar.author.github>
# <bitbar.desc>Greps and formats data from timewarrior.</bitbar.desc>
# <bitbar.image></bitbar.image>
# <bitbar.dependencies>python,timew</bitbar.dependencies>
# <bitbar.abouturl>https://github.com/schtobia/argos-timewarrior/blob/master/timewarrior.py</bitbar.abouturl>


import functools
import locale
from datetime import datetime, timedelta

from timew import TimeWarrior

TW = TimeWarrior()
TIMEFORMATTER = '%Y%m%dT%H%M%S%z'
locale.setlocale(locale.LC_ALL, '')
RESULTS = sorted(map(
    lambda x: {
        'start':
        datetime.strptime(x['start'], TIMEFORMATTER).astimezone(tz=None),
        'end':
        datetime.strptime(x['end'], TIMEFORMATTER).astimezone(tz=None)
        if 'end' in x else datetime.now().astimezone(tz=None),
        'id':
        x['id'],
        'tags':
        x['tags']
    }, TW.summary()),
                 key=lambda x: x['start'])

print("TW: {}\n-----".format(
    str(functools.reduce(lambda total, x: total + x['end'] - x['start'], RESULTS, timedelta())).split(sep='.', maxsplit=1)[0]
))
print(
    " | font=monospace | size=8\n".join(
        map(
            lambda x: str({
                'start': datetime.strftime(x['start'], "%x %X"),
                'end': datetime.strftime(x['end'], "%x %X"),
                'tags': x['tags']
            }), RESULTS)), "| font=monospace | size=8")
