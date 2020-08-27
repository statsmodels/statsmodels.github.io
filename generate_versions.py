#!/usr/bin/env python

import os
import sys
import json
from distutils.version import LooseVersion


def sort_versions(versions):
    stripped_version = [version[1:] if version[0] == 'v' else version
                        for version in versions]
    argsort = [x for x, y in sorted(enumerate(stripped_version),
                                    key=lambda x: LooseVersion(x[1]))]
    return [versions[i] for i in argsort]


def main():
    versions = []
    for tmp in os.walk('.'):
        _, dirs, _ = tmp
        for directory in dirs:
            if (directory not in ('dev', 'devel', 'stable')
                    and directory[0] != '.'):
                versions.append(directory)
        break

    versions = sort_versions(versions)
    versions = versions + ['stable', 'devel']
    with open('versions.json', 'w') as f:
        f.write(json.dumps(versions))


if __name__ == '__main__':
    sys.exit(main())
