#!/usr/bin/python

from DAG.node import Node

class Corner(Node):
    """ Neutral node mostly used for layouting.
    Inputs are just going through the node without any change.
    """
    def __init__(self):
        """ ctr.
        """
        Node.__init__(self)

# Ni !
