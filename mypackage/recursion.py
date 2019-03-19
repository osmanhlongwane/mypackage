 """Return the top n items in an array, in descending order.

    Args:
        items (array): list or array-like object containing numerical values.
        n (int): number of top items to return.

    Returns:
        array: top n items, in descending order.

    Examples:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 3]
    """
def sum_array(array):
    
    '''Return sum of all items in array'''
    if len(array)== 1:
        return array[0]
    else:
        return array[0]+ sum_array(array[1:])

def fibonacci(n):
    
    '''Return nth term in fibonacci sequence'''
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

def factorial(n):
    
    '''Return n!'''
    if n == 1:
        return n
    else:
        lower_fact = factorial(n-1)
        current_fact = n * lower_fact
        return  current_fact


def reverse(word):
    
    '''Return word in reverse'''
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0] 