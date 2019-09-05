from unittest import TestLoader, TestSuite, TextTestRunner
from src.TestScripts.test_Home_Page import TestHomePage
from src.TestScripts.test_Search_Page import TestSearchPage
from src.TestScripts.test_Registration_Page import TestRegistration
from src.TestScripts.test_Login_Page import TestLoginPage

# import testtools as testtools


if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(TestHomePage),
        loader.loadTestsFromTestCase(TestSearchPage),
        loader.loadTestsFromTestCase(TestRegistration),
        loader.loadTestsFromTestCase(TestLoginPage)
        ))

#run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)


# #run test parallel using concurrent_suite
#     concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
#     concurrent_suite.run(testtools.StreamResult())