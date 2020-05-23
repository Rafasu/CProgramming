#Link to problem: https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
#!/bin/python3

# Complete the countSwaps function below.
def countSwaps(a):
    n = len(a)
    counter = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                counter += 1
    printResult(counter, a)

def printResult(counter:int, a:list):
    print("Array is sorted in {} swaps.".format(counter))
    print ("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
