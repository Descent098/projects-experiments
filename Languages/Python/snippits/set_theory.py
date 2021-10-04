# Some custom functions for answering set theory based questions
A = [1, 2, 3, 4, 5, 6, 7, 8]
B = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
C = [2, 3, 4, 5, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 23, 24]

def union(l1:list, l2:list) -> list:
    """Calculates the Union of l1 and l2; l1 ∪ l2

    Parameters
    ----------
    l1 : list
        The first list/set
    l2 : list
        The second list/set

    Returns
    -------
    list
        The list of the union between the two
    """
    
    result = []
    result = l1
    for value in l2:
            if value not in l1:
                    result.append(value)
    return result


def intersection(l1:list, l2:list) -> list:
    """Calculates the intersection of l1 and l2; l1 ∩ l2

    Parameters
    ----------
    l1 : list
        The first list/set
    l2 : list
        The second list/set

    Returns
    -------
    list
        The list of the intersection between L1 and L2
    """
    result = []
    for value in l1:
            if value in l2:
                    result.append(value)
    return result


def difference(l1:list, l2:list)-> list:
    """Takes the differnece of the lists; l1 - l2 or l1\l2

    Notes
    -----
    Values found in l1, but not in l2

    Parameters
    ----------
    l1 : list
        The first list/set
    l2 : list
        The second list/set

    Returns
    -------
    list
        The list containing the difference of l1 and l2
    """
    result = []

    for value in l1:
        if value not in l2:
            result.append(value)
    return result

# # Check 1-3
# print(len(A) == 8)
# print(len(B) == 14)
# print(len(C) == 16)

# # Check 4
# print(intersection(A, B))
# print(len(intersection(A, B)) == 5)
# # Check 5
# print(intersection(A, C))
# print(len(intersection(A, C)) == 4)
# # Check 6
# print(intersection(B, C))
# print(len(intersection(B, C)) == 7)
# # Check 7
# print(union(union(A, B), C))
# print(len(union(union(A, B), C)) == 24) 

# # Question

# exp_1 = difference(intersection(A, B), C)

# exp_2 = difference(intersection(A, C), B)

# exp_3 = difference(intersection(B, C), A)

# print(exp_1, exp_2, exp_3)

# ans = union(union(exp_1, exp_2), exp_3)
# # X = ((A ∩ B) ∖ C) ∪ ((A ∩ C) ∖ B) ∪ ((B ∩ C) ∖ A) what is the cardinality of set X
# print(ans)
# print(len(ans))