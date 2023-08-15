# Three in One: Describe how you could use a single array to implement three stacks.

# To do what is described I would implement as follows:

# The methods peek, pop, push, and isEmpty would have to take an additional argument to decided which stack the
# action would apply to.

# There would have to be at least 2 int indexes to keep track of the starting point of stack 2 and stack 3.
# I would save them in an array like this: [0, stack2Index, stack3Index] so that we can use the stack number - 1 to get
# the index. (assuming stacks are 1, 2, or 3

# pop(int stack): would remove the item at the top of the stack, stackIndices[stack-1], and move over the other indices
# that follow, ie popping on stack 1 would remove the top element of stack 1 and would cause stack 2 and 3 indices to
# decrement by one. Popping on two would have 3 update and popping on 3 would need no action.

# peek(int stack): would work in a similar manner except it would return the top value instead of removing

# push(int stack,any item): would insert at the corresponding stack index and, like before, the stack items the
# follow would be updated.

# isEmpty(int stack): so if an index starts at another's index, its empty. if stack 1 index is the same as stack 2,
# its empty (technically the second index would be 0 since the first index doesn't move). Stack two is empty if stack
# 2 and stack 3 are the same. However, for stack 3, we have to find the size of stack 2 and if stack 3 is empty the
# index would be stack 2 index + stack 2 size
