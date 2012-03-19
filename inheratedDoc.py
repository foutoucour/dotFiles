import re
import inspect


class InheritedDoc(object):
    """ Decorator to find docstrings from subclass of the method class.
        Decorator are interpreted on the import and not on the call, so the inherated docstrings will be read when we call help.

        @type mroOrder: bool
        @param mroOrder: follow the order of the method resolution order (True)
            or reserse it (False). Default: True.
    """
    signature = '\n(Docstring inherated from "%s" class)'

    def __init__(self, mroOrder=True):
        """ Constructor
        """
        self.__mroOrder = mroOrder

    def __call__(self, method):
        """ If there are decorator arguments, __call__() is only called
            once, as part of the decoration process! You can only give
            it a single argument, which is the function object.
        """
        # Listing of super classes of the method class.
        classes = [
             element for name, element in method.func_globals.items() \
                if inspect.isclass(element)
        ]

        # We don't want to inheritate from the decorator itself.
        classes.remove(self.__class__)

        # Do we follow the order of the MRO or do we reverse it.
        if not self.__mroOrder:
            classes = reversed(classes)

        name = method.__name__

        for class_ in classes:

            # Testing if the class define the method
            if hasattr(class_, name):
                # Getting the method to find it doc
                class_method = eval('class_.%s' % name)
                doc = class_method.__doc__

                # We want to define the doc only if the method got a doc set.
                if doc:
                    # Displaying the source of docstring
                    # so the user can double check and verify it is the doc
                    # is coming from where he wanted to.
                    doc += self.signature % class_.__name__

                    method.__doc__ = doc

                    # the doc is defined and we don't want to keep on
                    # defining it again and again.
                    break

        return method


class SphinxInheritedDoc(InheritedDoc):
    """ Same as InheritedDoc but with a sphinx friendly signature,
        so the sphinx doc will create link to the class the docstring is coming from.
    """
    signature = '\n(Docstring inherated from ":class:`.%s`" class)'


class SuperClass(object):
    def foo(self):
        """ docstring

            @adding some more stuff of da doom
        """
        pass

class Test(SuperClass):
    @InheritedDoc()
    def foo(self):
        print

class Test2(Test):
    @SphinxInheritedDoc()
    def foo(self):
        pass

class Test3(Test):
    @InheritedDoc(mroOrder=False)
    def foo(self):
        pass

if __name__ == '__main__':
    print Test.foo.__doc__
    print Test2.foo.__doc__
    print Test3.foo.__doc__


