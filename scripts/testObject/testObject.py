shared = Shared()
class Test(shared):
    def __init__(self):
        print self.test


if __name__=='__main__':
    t = Test()
    print BUNDLE_ACP
