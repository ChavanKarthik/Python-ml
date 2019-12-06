fib = {1: "one", 2: "two", 3: "three", 4: "four", }
print(fib.get(1 in fib))

fiib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fiib.get(4, 0) + fib.get(7, 5))

primes = {1: 2, 2: 3, 4: 8, 7: 17, 8: 28}
print(primes[primes[4]])

swc = 0, 5, 6, 8
if swc[2] == 1 + 2 + 3:
    print(swc[2])

ss = list(range(0, 13))
print(ss)
print(ss[2:])
print(ss[:5])
print(ss[1::4])
print(ss[2:-2])
print(ss[7:3:-1])
