# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

# I would implement a second, minimum stack that would store smaller values.

# min would work like peek but for the smaller stack

# if an item is pushed and considered smaller, it is also pushed onto the min stack

# if an item is popped, and it is also the top of the min stack, it will be popped from the min stack as well

