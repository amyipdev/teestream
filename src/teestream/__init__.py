#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later

import datetime
import sys

class TeeStream:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, message):
        for s in self.streams:
            s.write(message)
            s.flush()

    def flush(self):
        for s in self.streams:
            s.flush()

class TeeStdout(TeeStream):
    def __init__(self, logfile):
        super().__init__(sys.stdout, logfile)

def load_redirect_path(path: str):
    logfile = open(path, "a", buffering=1)
    sys.stdout = TeeStream(sys.stdout, logfile)
    sys.stderr = TeeStream(sys.stderr, logfile)

def load_default_redirect(pname: str):
    load_redirect_path(f"/tmp/{pname}-{datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')}.log")
