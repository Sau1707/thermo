class Cycle:
    """
        Generic Thermodynamic Process

        A process have multiple Steps. The last step added close the cycle.

        Once all the steps are added, the process can be analyzed
        We do a while loop in two directions. Until all the points are computed
    """
    def __init__(self):
        self.steps: list[Step] = []

    def add_step(self, step: Step):
        self.steps.append(step)

    def solve(self):
        """
        TODO: Try to solve the process, raise and error if it's impossible
        """
        
    def plot(self):
        """
        TODO: Plot the process in a T-s and p-v diagram
        """
        
    def table(self):
        """
        TODO: Print a table with the properties of each point
        """