#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

```python
a)  a = 0 # O(1)
    while (a < n * n * n): O(n^3)
      a = a + n * n # O(1)
```

This is actually O(n) because inside the _while_ loop we add to the iterator by `n * n`, leaving only `while a < n` in the condition.

```python
b)  sum = 0 # O(1)
    for i in range(n): # O(n)
      j = 1 # O(1)
      while j < n: # O(log n)
        j *= 2 # O(1)
        sum += 1 # O(1)
```

The most dominant from the sum of these operations and loops is `O(n log n)`. The nested while loop is ran < half the times of n, making it `O(log n)` but we have to account for the fact the `loop` is being run `n times`.

```python
c)  def bunnyEars(bunnies):
      if bunnies == 0: # O(1)
        return 0 # O(1)

      return 2 + bunnyEars(bunnies-1) # O(n)
```

This recursive function calls itself `n times` because it is using `bunnies` like a counter and it starts at `n` and subtracts every recursive call down to 0.

## Exercise II

Option 1: If you don't want to break the eggs just use the first floor...

Option 2: A `O(n)` method would be to iterate thru each `nth floor` until the eggs started breaking. You would then know that `story[i] = f`. This breaks a lot of eggs though

pseudocode:

```
set f to 0
for each floor in n-story building
    if egg_breaks(floor):
        set f to floor
        break
    otherwise continue looping
return f
```

Option 3: A `O(log n)` method would be to use something like a binary search algorithm but with a target being when the egg breaks.

```
set a low and high variable for the first and last floors
loop while low <= high
    guess a floor in the middle of the n-story building

    check if egg breaks at guessed floor

    if yes guess return floor number

    if no guess a midpoint to the right of the current guess

```
