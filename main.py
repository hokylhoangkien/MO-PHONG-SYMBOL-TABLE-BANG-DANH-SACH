from TestUtils import TestUtils
from TestSuite import TestSymbolTable
from pprint import pprint
from io import StringIO
import unittest


def test(suite):
    """
    Executes a suite of unit tests and prints the results.

    Args:
        suite (unittest.TestSuite): A collection of test cases to be executed.

    Outputs:
        - The total number of tests run.
        - A list of errors encountered during the test execution.
        - A list of test failures with detailed information.
        - The full output of the test runner.

    Note:
        This function uses an in-memory stream to capture the output of the test runner.
    """
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print("Tests run ", result.testsRun)
    print("Errors ", result.errors)
    pprint(result.failures)
    stream.seek(0)
    print("Test output\n", stream.read())


if __name__ == "__main__":
    TestUtils.clean()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSymbolTable)
    test(suite)
