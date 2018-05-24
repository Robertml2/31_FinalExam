"""
Final exam, problem 1.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Madison Robertson.  May 2018.

"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    # ------------------------------------------------------------------
    # Uncomment the following calls to the testing functions
    # one at a time as you work the problems.
    # ------------------------------------------------------------------
    print()
    print('Un-comment the calls in MAIN one by one')
    print(' to run the testing code as you complete the TODOs.')
    # run_test_problem1a()
    # run_test_problem1b()


def run_test_problem1a():
    """ Tests the  problem1a   function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1a   function:')
    print('--------------------------------------------------')

    format_string = '    problem1a( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    sequence = [5, 3, 10, 8, 1]
    expected = 16
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem1a(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    sequence = [9, 15, 12, 20, 2, 6, 8, 1, 17]
    expected = 28
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem1a(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    sequence = [5, 7, 2]
    expected = 14
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem1a(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence = [0, 0, 20, 9, 0]
    expected = 20
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem1a(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)


def problem1a(numbers):
    """
    What comes in:
      -- A sequence of numbers, with the sequence having a length
            that is odd and at least 3.
    What goes out:
      -- Returns the sum of the first, middle, and last numbers
           in the sequence.
    Side effects:  None.
    Examples:
      problem1a( [5, 3, 10, 8, 1] )                  returns 16
      problem1a( [9, 15, 12, 20, 2, 6, 8, 1, 17] )   returns 28
      problem1a( [5, 7, 2] )                         returns 14
      problem1a( [0, 0, 20, 9, 0] )                  returns 20
    Type hints:
      :type numbers:  [int]
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------

    for k in range(len(numbers)):
        


def run_test_problem1b():
    """ Tests the  problem1b   function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b   function:')
    print('--------------------------------------------------')

    format_string = '    problem1b( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    expected = 26
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    sequence = [5, 3, 10, 8, 1, 100]
    expected = 18

    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    sequence = [5, 7, 2]
    expected = 7

    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence = [9, 15, 12, 20, 30, 10, 8, 1, 17]
    expected = 60

    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)


def problem1b(numbers):
    """
    What comes in:
      -- A non-empty sequence of numbers, with the sequence having a length
            that is evenly divisible by 3
    What goes out:
      -- Returns the sum of the middle third of the numbers in the sequence.
    Side effects:  None.
    Examples:
      problem1b( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] )
                                      returns 5 + 6 + 7 + 8, which is 26

      problem1b( [5, 3, 10, 8, 1, 100] )     returns 10 + 8, which is 18
      problem1b( [5, 7, 2] )                              returns 7
      problem1b( [9, 15, 12, 20, 30, 10, 8, 1, 17] )      returns 60
    Type hints:
      :type numbers:  [int]
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


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
