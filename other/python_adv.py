#Created on 26. July 2020, lecture 1 of the day

pows = [2**i for i  in range(10000000) if 2**i < 1_000_000_000]
print(*pows)
print(2**1000000)