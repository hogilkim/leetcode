import collections
def main():
    list1 = ['a', 'b','a','c']
    counter = collections.Counter(list1).items()
    for key, val in counter:
        print(key, val, sep=" ")



main()