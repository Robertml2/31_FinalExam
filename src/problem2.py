"""
Final exam, problem 2.

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
    run_test_problem2a()
    run_test_problem2b()
    run_test_problem2c()


def is_prime(n):
    """
    What comes in:  An integer n.
    What goes out:
      -- Returns True if the given integer is prime,
                 False if the given integer is NOT prime.
         Treats integers less than 2 as NOT prime.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
      -- is_prime(1)  returns  False
    Note: The algorithm used here is simple and clear but slow.
    """
    if n < 2:
        return False
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no TO DO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # ------------------------------------------------------------------


def sum_of_digits(number):
    """
    What comes in:  An integer.
    What goes out:  Returns the sum of the digits in the given integer.
    Side effects:   None.
    Example:
      If the integer is 83135,
      this function returns (8 + 3 + 1 + 3 + 5), which is 20.
    """
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  sum_of_digits function - it has no TO DO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # ------------------------------------------------------------------


def run_test_problem2a():
    """ Tests the  problem2a   function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2a   function:')
    print('--------------------------------------------------')

    format_string = '    problem2a( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    x = 5
    sequence = [9, 15, 2, -1, 5, 17, 4]
    expected = [9, 15, 17]
    print_expected_result_of_test([x, sequence], expected,
                                  test_results, format_string)
    actual = problem2a(x, sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    x = 6
    sequence = [9, 15, 2, -1, 5, 17, 4]
    expected = [9, 15, 17]
    print_expected_result_of_test([x, sequence], expected,
                                  test_results, format_string)
    actual = problem2a(x, sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    x = 16
    sequence = [9, 15, 2, -1, 5, 17, 4]
    expected = [17]
    print_expected_result_of_test([x, sequence], expected,
                                  test_results, format_string)
    actual = problem2a(x, sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    x = 17
    sequence = [9, 15, 2, -1, 5, 17, 4]
    expected = []
    print_expected_result_of_test([x, sequence], expected,
                                  test_results, format_string)
    actual = problem2a(x, sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    x = -10000000000000
    sequence = []
    expected = []
    print_expected_result_of_test([x, sequence], expected,
                                  test_results, format_string)
    actual = problem2a(x, sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)


def problem2a(x, sequence):
    """
    What comes in:
      -- An integer  x  and a sequence of integers.
    What goes out:
      -- Returns a list containing all the numbers in the given sequence
           that are strictly greater than the given x,
           in the same order that they appear in the give sequence.
    Side effects:  None.
    Examples:
      problem2a(  5, [9, 15, 2, -1, 5, 17, 4] )    returns [9, 15, 17]
      problem2a(  6, [9, 15, 2, -1, 5, 17, 4] )    returns [9, 15, 17]
      problem2a( 16, [9, 15, 2, -1, 5, 17, 4] )    returns [17]
      problem2a( 17, [9, 15, 2, -1, 5, 17, 4] )    returns []

      problem2a( -5, [9, 15, 2, 20, 13, 6, 8, -1, 17] )
             returns [9, 15, 2, 20, 13, 6, 8, -1, 17]

      problem2a( -100000000, [] )    returns []
    Type hints:
      :type x:    int
      :type sequence:  [int]
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    list = []
    for k in range(len(sequence)):
        if sequence[k] > x:
            list = list + [sequence[k]]
    return list



def run_test_problem2b():
    """ Tests the  problem2b   function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2b   function:')
    print('--------------------------------------------------')

    format_string = '    problem2b( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    sequence = [9, 88, 2, -1, 5, 17, 4]
    expected = 1
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem2b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    sequence = [9, 13, 2, -1, 5, 17, 4]
    expected = 5
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem2b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    sequence = [9, -88, 2, -1, 5, 17, 4]
    expected = 1
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem2b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence = [-500]
    expected = 0
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem2b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    sequence = [1, 2, 3, 4, 5, 6, 7, -500]
    expected = 7
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem2b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)
    
    
def problem2b(sequence):
    """
    What comes in:
      -- An non-empty sequence of integers with no duplicates.
    What goes out:
      -- Returns the index of the number in the sequence
           whose absolute value is largest.
    Side effects:  None.
    Examples:
      problem2b( [9,  88, 2, -1, 5, 17, 4] )   returns 1   (index of 88)
      problem2b( [9,  13, 2, -1, 5, 17, 4] )   returns 5   (index of 17)
      problem2b( [9, -88, 2, -1, 5, 17, 4] )   returns 1   (index of -88)
      problem2b( [-500] )                      returns 0
      problem2b( [1, 2, 3, 4, 5, 6, 7, -500] ) returns 7
    Type hints:
      :type sequence  [int]
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    total = 0
    for k in range(len(sequence)):
        if abs(sequence[k]) > abs(sequence[total]):
            total = k
    return total


def run_test_problem2c():
    """ Tests the  problem2c   function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2c   function:')
    print('--------------------------------------------------')

    format_string = '    problem2c( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    x = 17
    expected = 23
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem2c(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    x = 101
    expected = 101
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem2c(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    x = 4
    expected = 5
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem2c(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    x = 61
    expected = 61
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem2c(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    x = 62
    expected = 67
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem2c(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    x = 9999
    expected = 10037
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem2c(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    x = 5555555
    expected = 5555629
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem2c(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    x = 10000001
    expected = 10000019
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem2c(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    x = 111
    expected = 113
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem2c(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    x = 112
    expected = 113
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem2c(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    x = 113
    expected = 113
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem2c(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    x = 114
    expected = 131
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem2c(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)
    
    
def problem2c(x):
    """
    What comes in:  An integer  x  that is at least 2.
    What goes out:
      -- Returns the smallest prime such that:
           -- the prime is bigger than or equal to x, AND
           -- the (sum of the digits of the prime) is itself prime.
    Side effects:  None.
    Examples:
      problem2c( 17)   returns  23  because:
            - the sum of the digits of 17 is 8, which is NOT prime
            - 18 is not prime
            - the sum of the digits of 19 is 10, which is NOT prime
            - 20 is not prime
            - 21 is not prime
            - 22 is not prime
            - the sum of the digits of 23 is 5, which IS prime
      problem2c( 101 )    returns 101  (because 101 and 1+0+1 are prime)
      problem2c(   4 )    returns 5
      problem2c(  61 )    returns 61
      problem2c(  62 )    returns XX
    Type hints:
      :type x:    int
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------

    for k in range(sum_of_digits(x)):
        if k >= is_prime(k):
            return k



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
