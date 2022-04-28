# Problem 55:
#     Lychrel Numbers
#
# Description:
#     If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#
#     Not all numbers produce palindromes so quickly. For example,
#          349 +  943 = 1292,
#         1292 + 2921 = 4213
#         4213 + 3124 = 7337
#     That is, 349 took three iterations to arrive at a palindrome.
#
#     Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
#     A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
#     Due to the theoretical nature of these numbers, and for the purpose of this problem,
#       we shall assume that a number is Lychrel until proven otherwise.
#     In addition you are given that for every number below ten-thousand, it will either
#       (i)  become a palindrome in less than fifty iterations, or,
#       (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
#     In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome:
#       4668731596684224866951378664 (53 iterations, 28-digits).
#
#     Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
#     How many Lychrel numbers are there below ten-thousand?
#
#     NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

def is_palindromic(x):
    """
    Returns True iff `x` is a palindromic number.

    Args:
        x (int): Natural number

    Returns:
        (bool): True iff `x` is a palindromic number.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(x) == int and x > 0
    return x == int(str(x)[::-1])


def main():
    """
    Returns the count of Lychrel numbers below 10,000.

    Returns:
        (int): Number of Lychrel numbers below 10,000
    """
    i_max = 50
    count = 0
    for x in range(1, 10**4):
        is_lychrel = True  # Assume x is Lychrel until proven otherwise
        i = 0  # Number of iterations of 'reverse and add'
        y = x
        while i < (i_max - 1):
            # Perform one 'reverse and add' operation
            y += int(str(y)[::-1])
            i += 1
            if is_palindromic(y):
                is_lychrel = False
                break
        if is_lychrel:
            count += 1
    return count


if __name__ == '__main__':
    lychrel_count = main()
    print('Count of Lychrel numbers below 10,000:')
    print('  {}'.format(lychrel_count))
