from phys import *

"""
Represents a material config file
Can be iterated over like a list of material sections
"""
class MaterialConfig:
    def __init__(self, path):
        with open(path, 'r') as fp:
            self.sections = list(self.parse(fp))

    def parse(self, fp):
        for line in fp:
            if line.startswith('#'):
                continue
            if line := line.strip():
                name, indices = line.split(',')
                a, b = indices.split(':')
                yield materials[name], (int(a), int(b))

    def __iter__(self):
        return iter(self.sections)

