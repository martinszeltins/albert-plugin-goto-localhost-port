# -*- coding: utf-8 -*-

"""Go to localhost port.
Type :PORT and it will open http://localhost:PORT/
Synopsis: <trigger> <filter>"""

import os
from albert import *

__title__ = "Go to localhost port"
__version__ = "0.1.0"
__triggers__ = ":"
__authors__ = "Martins Zeltins"

iconPath = os.path.dirname(__file__) + "/www.png"

def handleQuery(query):
    items = []

    if query.isTriggered:
        item = Item(
            id='goto-localhost-port',
            icon=iconPath,
            text="http://localhost:%s" % (query.string),
            subtext="Open http://localhost:%s" % (query.string),
            actions=[
                UrlAction(text="Open URL", url="http://localhost:%s" % (query.string)),
            ]
        )

        items.append(item)

        return items
