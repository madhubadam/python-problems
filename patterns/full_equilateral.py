n = 5

# Upper pyramid
for i in range(n):

    # spaces before stars
    print(" " * (n - i - 1), end="")

    # stars
    print("*" * (2 * i + 1))


# Lower inverted pyramid
for i in range(n):

    # spaces before stars
    for j in range(i + 1):
        print("", end=" ")

    # stars
    for k in range(2 * n - (2 * i + 1) - 2):
        print("*", end="")

    print()