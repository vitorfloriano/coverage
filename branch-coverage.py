import sys


def BranchCoverageDemo(n):
    if n > 0:
        x = n
    print("The value of x is " + str(x) + ".")


def DeadFunction():
    print("I am not being used.")


if __name__ == "__main__": # pragma: no cover
    n = int(sys.argv[1])
    BranchCoverageDemo(n)
