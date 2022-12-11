'''you have to enter a positive integer range[A,B] and system will find out the status(prime or composite) of each number available in the given range. At the end print the count also'''


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
count = 0
for i in range(start,end+1):
    if isPrime(i):
        print("{} is a prime".format(i))
        count = count + 1
    else:
        print("{} is a composite number".format(i))
print("\nThere are {} prime numbers and {} composite numbers in the range".format(count,end-start+1-count))