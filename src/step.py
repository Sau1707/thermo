class Step:
    """
        A single step in a thermodynamic process

        it has a start and and end point
    """
    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end

    def compute(self):
        """
            Compute the properties of the end point
            Tries first in one direction and then in the other one
        """
        # The values are updated to the point


