def f(x):
    return {n * (x + 1)  for n in range(0, x)}


print("some Function:\nf(x) = {y, y = n(x+1), -1 < n < x, n ∈ I}  \n")

[print( f"f({k}) -> ", f(k)) for k in range(1,11)]

print("Use cases: fucntion to find diagonal element index of matrix")
