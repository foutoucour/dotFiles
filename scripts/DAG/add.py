#!/usr/bin/python

from DAG.node import Node

class Add(Node):
    """ Node to add inputs.
    """
    def __init__(self):
        Node.__init__(self)

    def command(self, *args, **kwargs):
        """
        """
        result = 0
        for arg in args :
            result += arg
        return result

# Ni !
