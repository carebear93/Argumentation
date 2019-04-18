class Argument:
    def __init__(self,subarguments,toprule):
        """ subarguments are the subarguments used to generate this argument. toprule
        is the rule applied to move from subarguments to the current argument. A rule
        of the form -> a has no subarguments."""
        self.subarguments=subarguments + self #note an argument is its own subargument
        self.toprule=toprule
