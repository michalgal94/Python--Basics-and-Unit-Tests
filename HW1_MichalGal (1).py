# ---------------------------- #1 ---------------------------
def q1(list1):
    sum = 0
    for i in list1:
        for j in i:
            sum += j
    return sum

# ---------------------------- #2 ---------------------------
def q2_a(input):
    return input[::-1]

def q2_b(list1):
    reversedlist = list1[::-1]
    for i in reversedlist:
        if isinstance(i, list):
            reversedlist[reversedlist.index(i)] = i[::-1]
    return reversedlist

def q2_c(tuple):
    return tuple[::-1]

# ---------------------------- #3 ---------------------------
def q3_a(tuple):
    charSet = set()
    numSet = set()
    for i in range(0, len(tuple), 1):
        if len(tuple[i]) == 0:
            continue
        for j in tuple[i]:
            break
        if isinstance(j, str):
            charSet = charSet.union(tuple[i])
        else:
            numSet = numSet.union(tuple[i])
    return sorted(list(charSet)) + sorted(list(numSet))

def q3_b(tuple):
    sortedTuple = q3_a(tuple)
    diction = {}
    return {i:sortedTuple.__getitem__(i) for i in range(0, len(sortedTuple), 1)}

# ---------------------------- #4 ---------------------------
def q4_a():
    x = int(input("Please enter a number "))
    y = 9
    while(x > 10):
        y = 6
        break
    return y

def q4_a_test_version(x):
    y = 9
    while(x > 10):
        y = 6
        break
    return y

def q4_b():
    x = int(input("Please enter a number "))
    y = 6 if x > 10 else 9
    return y

def q4_b_test_version(x):
    y = 6 if x > 10 else 9
    return y

# ---------------------------- #5 ---------------------------
def q5_a():
    even_set = set()
    num1 = int(input("Please enter a number "))
    num2 = int(input("Please enter another number "))
    x = 1
    for i in range(0, num1 % 2, 1):
        x = 0
    for i in range(0, x, 1):
        even_set.add(num1)
    for i in range(num1, num2, 1):
        even_set.add(i+(i%2))
    print(sorted(even_set))
    print(sorted(even_set, reverse=True))

# needed for test, works exactly the same as the regular version above.
def q5_a_test_version(num1, num2):
    even_set = set()
    x = 1
    for i in range(0, num1 % 2, 1):
        x = 0
    for i in range(0, x, 1):
        even_set.add(num1)
    for i in range(num1, num2, 1):
        even_set.add(i+(i%2))
    return even_set

def q5_b():
    even_set = set()
    num1 = int(input("Please enter a number "))
    num2 = int(input("Please enter another number "))
    while (num1 == num2 and (num1 % 2) == 0):
        even_set.add(num1)
        break
    while(num1 < num2):
        even_set.add(num1+(num1%2))
        num1 += 1
    print(sorted(even_set))
    print(sorted(even_set, reverse=True))

# needed for test, works exactly the same as the regular version above.
def q5_b_test_version(num1, num2):
    even_set = set()
    while(num1 == num2 and (num1 % 2) == 0):
        even_set.add(num1)
        break
    while(num1 < num2):
        even_set.add(num1+(num1%2))
        num1 += 1
    return even_set

'''
question 5 c:
A solution is possible in a recursive way.
First we receive two numbers from the user and using it only once before enter into the recursive part.
Then we call a recursive function with the terminate condition to stop when the two numbers are equal and print the final result,
or else add the number to a set that we carry as a parameter and call another iteration of the recursive func.
Also if numbers are equal, check if they are even to cover the case when there's no gap between the numbers.
therefore, we can use only if statements without loops.
'''
def getNumsFromUser():
    num1 = int(input("Please enter a number "))
    num2 = int(input("Please enter another number "))
    return num1, num2

def recursiveWay(num1, num2, even_set):
    if num1 == num2:
        if num1 % 2 == 0:
            even_set.add(num1)
        print(sorted(even_set))
        print(sorted(even_set, reverse=True))
    else:
        even_set.add(num1 + (num1%2))
        recursiveWay(num1+1, num2, even_set)

def q5_c():
    set1 = set()
    num1, num2 = getNumsFromUser()
    recursiveWay(num1, num2, set1)

# Following methods works exactly the same as the regular version above.
def recursiveWay_for_test_version(num1, num2, even_set):
    if num1 == num2:
        if num1 % 2 == 0:
            even_set.add(num1)
    else:
        even_set.add(num1 + (num1%2))
        recursiveWay_for_test_version(num1+1, num2, even_set)


def q5_c_test_version(num1, num2):
    set1 = set()
    recursiveWay_for_test_version(num1, num2, set1)
    return set1


# ---------------------------- TESTS ---------------------------
def test_q1():
    assert(q1([[1, 2], [3], [4, 5]]) == 15)
    assert(q1([[0]]) == 0)
    assert(q1([[11, 22], [33]]) == 66)


def test_q2_a():
    assert(q2_a("nir-michal") == "lahcim-rin")
    assert(q2_a("") == "")


def test_q2_b():
    assert(q2_b([[1, 2], 3, [4, 5]]) == [[5, 4], 3, [2, 1]])
    assert(q2_b([1, 2, 3, 4]) == [4, 3, 2, 1])


def test_q2_c():
    assert(q2_c((1, 2, 3)) == (3, 2, 1))
    assert(q2_c((1, [2, 3])) == ([2, 3], 1))
    assert(q2_c(()) == ())


def test_q3_a():
    assert(q3_a(({1, 2, 3, 3}, {"d", "t", "f"}, {3.4, 1.2, 5.6, 0.9}, {'a', 'g', 'e', 'b'}, {4}, {})) == ['a', 'b', 'd', 'e', 'f', 'g', 't', 0.9, 1, 1.2, 2, 3, 3.4, 4, 5.6])
    assert(q3_a(()) == [])


def test_q3_b():
    assert(q3_b(({1, 2, 3, 3}, {"d", "t", "f"}, {3.4, 1.2, 5.6, 0.9}, {'a', 'g', 'e', 'b'}, {4}, {})) == {0: 'a', 1: 'b', 2: 'd', 3: 'e', 4: 'f', 5: 'g', 6: 't', 7: 0.9, 8: 1, 9: 1.2, 10: 2, 11: 3, 12: 3.4, 13: 4, 14: 5.6})
    assert(q3_b(()) == {})


def test_q4_a():
    assert(q4_a_test_version(1) == 9)
    assert(q4_a_test_version(10) == 9)
    assert(q4_a_test_version(11) == 6)


def test_q4_b():
    assert(q4_b_test_version(1) == 9)
    assert(q4_b_test_version(10) == 9)
    assert(q4_b_test_version(11) == 6)


def test_q5_a():
    assert(q5_a_test_version(1, 11) == {2, 4, 6, 8, 10})
    assert(q5_a_test_version(6, 12) == {6, 8, 10, 12})
    assert(q5_a_test_version(3, 3) == set())
    assert(q5_a_test_version(0, 0) == {0})


def test_q5_b():
    assert(q5_b_test_version(1, 11) == {2, 4, 6, 8, 10})
    assert(q5_b_test_version(6, 12) == {6, 8, 10, 12})
    assert(q5_b_test_version(3, 3) == set())
    assert(q5_b_test_version(0, 0) == {0})


def test_q5_c():
    assert (q5_c_test_version(1, 11) == {2, 4, 6, 8, 10})
    assert (q5_c_test_version(6, 12) == {6, 8, 10, 12})
    assert (q5_c_test_version(3, 3) == set())
    assert (q5_c_test_version(0, 0) == {0})


if __name__ == "__main__":
    test_q1()
    test_q2_a()
    test_q2_b()
    test_q2_c()
    test_q3_a()
    test_q3_b()
    test_q4_a()
    test_q4_b()
    test_q5_a()
    test_q5_b()
    test_q5_c()
    # q5_c()

