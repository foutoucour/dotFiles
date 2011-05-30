#!/usr/bin/python

class Node(object):
    """
    """
    def __init__(self, *args, **kwargs):
        """ Ctr.
        Should basically create the interface :
            - value to modify
        Should also init the unittest of the inputs.
        """
        pass

    def __call__(self, *args, **kwargs):
        """ Method executing the node
        """
        return self.command(*args, **kwargs)

    def command(self, *args, **kwargs):
        """ Method called when the node is executed.
        """
        return args, kwargs

# Ni !
