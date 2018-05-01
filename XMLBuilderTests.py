from XMLBuilder import *

def testClosure():
    """test environment"""
    # --- setup
    cls_test = XmlBuilder(url='xxx', version=2.6)
    cls_test.build_xml(True, name='Administrator', password='xxx')
    cls_test.make_request()
    cls_test.get_token()
    passed = 0
    failed = 0

    def test():
        """test to make sure tests are working properly
        test should always be true"""
        try:
            assert True == True
            print("test: {} passed".format(test.__name__))
        except:
            print("test: {} failed".format(test.__name__))

    def test200Status():
        """test to check for login success"""
        global passed
        global failed
        cls_test.make_request()
        print(cls_test.status)
        assert cls_test.status == 200, "test: {} failed".format(test200Status.__name__)



    def test204Status():
        """test to check for logout success"""
        global passed
        global failed
        print(cls_test.status)
        cls_test.logout()
        print(cls_test.status)
        assert cls_test.status == 204, "test: {} failed".format(test204Status.__name__)



    def testXMLtree():
        """test for successful xml tree creation"""

    def run_tests():
        # --- base case test
        test()
        # --- test for successful login
        test200Status()
        # --- test for successful logout
        test204Status()


    run_tests()


if __name__=="__main__":
    testingEnv = testClosure()

