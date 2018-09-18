#!/usr/bin/env python

import os
import sys
import json
from distutils.version import StrictVersion

def main():
    versions = []
    for tmp in os.walk('.'):
        _, dirs, _ = tmp
        for directory in dirs:
            if (directory not in ('dev', 'devel', 'stable') and
                    directory[0] != '.'):
                versions.append(directory)
        break
    versions.sort(key=StrictVersion)
    versions = versions + ['stable', 'devel']
    with open('versions.json', 'w') as f:
        f.write(json.dumps(versions))


if __name__ == '__main__':
    sys.exit(main())

