def coin_change(amount, coins):
    """
    Calculate the minimum number of coins needed to make the given amount
    using a greedy approach.

    Args:
        amount (int): The total amount to make change for.
        coins (list of int): List of coin denominations available.

    Returns:
        dict or None: A dictionary with coin denominations as keys and counts
                      as values, or None if change cannot be made exactly.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """

    coins.sort(reverse=True)  # Decending order start with largest
    result = {}

    for coin in coins:
        # Determine how many coins of this denomination we can use.
        count = amount // coin

        # If at least one coin of this denomination can be used:
        if count:
            # Record the count in the result.
            result[coin] = count
            # Reduce the remaining amount accordingly.
            amount -= coin * count

    # Return the result if we've exactly reached 0; otherwise, return None.
    return result if amount == 0 else None


# Example:
coins = [1, 5, 10, 25]
amount = 63
print(coin_change(amount, coins))
