from banyan import SortedSet, OverlappingIntervalsUpdator
from DAPOS.utils import flatten

class BoundariesOverlap(object):
    EndOfBoundaries = 'EndOfText'
    def __init__(self, boundaries, edges):
        self.boundaries = boundaries
        self._edges = sorted(flatten(edges))
        self.edges = None
        self.edge = None
        self.switch = True

    def update_edge(self):
        try:
            self.edge = self.edges.pop(0)
        except IndexError:
            self.edge = self.EndOfBoundaries

    def is_edge(self, point):
        return point == self.edge

    def _init_iter(self):
        self.edges = self._edges[:]
        self.update_edge()
        self.switch = True

    def flip_switch(self):
        self.switch = not self.switch

    def __iter__(self):
        self._init_iter()
        for boundary in self.boundaries:
            if self.switch or self.is_edge(boundary):
                yield boundary
            if self.is_edge(boundary):
                self.flip_switch()
                self.update_edge()
