#!/usr/bin/env python
# Loop 1 always finishes
n = 20
i = 0
while i <= n:
    i = i + 1
    print i

# Loop 2 always finishes
n = 2
i = 1
while True:
    i = i * 2
    n = n + 1
    if i > n:
        break
    print i

# Loop 3
n = 3
while n != 1:
    if n % 2 == 0: #n is even
        n = n/2
    else:
        n = 3 * n + 1

