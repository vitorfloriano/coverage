# Function with multiple branches.
import sys


def StatementCoverageDemo(number):
    if number < 0:
        print(str(number) + " is negative.")
    elif number == 0:
        print(str(number) + " is 0.")
    else:
        print(str(number) + " is positive.")


# Main processing starts here.
if __name__ == "__main__":
    n = float(sys.argv[1])
    StatementCoverageDemo(n)
