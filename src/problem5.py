"""
Final exam, problem 5.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Madison Robertson.  May 2018.

"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem5()


def run_test_problem5():
    """ Tests the  problem5   function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem5   function:')
    print('--------------------------------------------------')

    format_string = '    problem5( {}, {},\n                 {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    m = 3
    numbers1 = [10, 4, 20, 6, 8]
    numbers2 = [88, 8, 60, 6, 4]
    expected = [20, 60]
    print_expected_result_of_test([m, numbers1, numbers2], expected,
                                  test_results, format_string)
    actual = problem5(m, numbers1, numbers2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    m = 2
    numbers1 = [10, 4, 20, 6, 8]
    numbers2 = [88, 8, 60, 6, 4]
    expected = [4, 8]
    print_expected_result_of_test([m, numbers1, numbers2], expected,
                                  test_results, format_string)
    actual = problem5(m, numbers1, numbers2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    m = 1
    numbers1 = [10, 4, 20, 6, 8]
    numbers2 = [88, 8, 60, 6, 4]
    expected = [6, 6]
    print_expected_result_of_test([m, numbers1, numbers2], expected,
                                  test_results, format_string)
    actual = problem5(m, numbers1, numbers2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    m = 9
    numbers1 = [10, 4, 20, 6, 8]
    numbers2 = [88, 8, 60, 6, 4]
    expected = []
    print_expected_result_of_test([m, numbers1, numbers2], expected,
                                  test_results, format_string)
    actual = problem5(m, numbers1, numbers2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    m = 0
    numbers1 = [10, 4, 20, 6, 8]
    numbers2 = [88, 8, 60, 6, 4]
    expected = []
    print_expected_result_of_test([m, numbers1, numbers2], expected,
                                  test_results, format_string)
    actual = problem5(m, numbers1, numbers2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    m = 0
    numbers1 = [10, 0, 20, 6, 8, 50, 8, 100]
    numbers2 = [88, 8, 60, 6, 0, 50, 1, 200]
    expected = [8, 0]
    print_expected_result_of_test([m, numbers1, numbers2], expected,
                                  test_results, format_string)
    actual = problem5(m, numbers1, numbers2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    m = -1
    numbers1 = [10, 0, 20, 6, 8, 50, 8, 100]
    numbers2 = [88, 8, 60, 6, 0, -50, 1, 200]
    expected = [50, -50]
    print_expected_result_of_test([m, numbers1, numbers2], expected,
                                  test_results, format_string)
    actual = problem5(m, numbers1, numbers2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)


def problem5(m, numbers1, numbers2):
    """
    What comes in:
       -- An integer m
       -- Two non-empty sequences of numbers, each with the same length.
    What goes out:
       Looks for an index I such that the second sequence's value at that index
          is   m   times the first sequence's value at that same index.
       If it finds such an index, this function returns a list of two items:
         -- the first sequence's value at the index I
         -- the second sequence's value at the index I
    Side effects: None.
    Examples:
      problem5(3, [10, 4, 20, 6, 8],
                  [88, 8, 60, 6, 4])    returns [20, 60]

      problem5(2, [10, 4, 20, 6, 8],
                  [88, 8, 60, 6, 4])    returns [4, 8]

      problem5(1, [10, 4, 20, 6, 8],
                  [88, 8, 60, 6, 4])    returns [6, 6]

      problem5(9, [10, 4, 20, 6, 8],
                  [88, 8, 60, 6, 4])    returns []

      problem5(0, [10, 4, 20, 6, 8],
                  [88, 8, 60, 6, 4])    returns []

      problem5(0, [10, 0, 20, 6, 8, 50, 0, 100],
                  [88, 8, 60, 6, 0, 50, 0, 200])    returns [0, 0]
    Type hints:
      :type [str]
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    for k in range(len(numbers1)):
        if numbers1[k]*m == numbers2[k]:
            return [numbers1[k], numbers2[k]]
    return []



###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results,
                                                 format_string)


def print_actual_result_of_test(expected, actual, test_results):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
