# Weird Sort-and-Compress Thing
A weird integer sorting + compression algorithm inspired by a conversation with [Luthingx]( https://github.com/Luthingx ) (it probably already exists by some name I don't know yet). There's a lot still to improve about this algorithm, so be careful where you use it.


## How it works
Here's an example for the following list:

    l = [1, 2, 2, 2, 3]

The algorithm starts with counting sort, creating a dictionary with each unique number as key and the number of occurences of it in the list as the value:

    d = {1: 1, 2: 3, 3: 1}

To decrease the space needed to store the numbers in memory, we'll only store the first number and then the difference between each of the next numbers and the previous one:

    d2 = [(1, 1), (1, 3), (1, 1))
    
Now, the minimum amount of memory we need to store every key that's in d2 is 1 bit, since 1 is the maximum difference between any subsequent elements. The same applies to the values, except that to store any value here we need 2 bits of memory, since the maximum value is 3(11 in binary).
So we know that we can store this list as a sequence of 3 bits elements, like this:

    d2_bin = ["101", "111", 101"]
    
We can now return the list as a single number, along with a pair of integers containing the number of bits in each key and the number of bits in each value, allowing the value to be decompressed.

## Memory efficiency

Here's a list with the sum of the number of bits of all numbers in a list with 100 elements, generated with random values in the range 0 to 50 and generated 20 times, vs. the number of bits in the resulting compressed integer(taking as a premise that all numbers in the array are all actually stored in continuous memory, including duplicates):

    467 => 208
    486 => 230
    490 => 221
    491 => 216
    493 => 222
    491 => 221
    494 => 230
    485 => 235
    494 => 217
    490 => 252
    461 => 265
    476 => 241
    492 => 247
    487 => 230
    474 => 246
    460 => 222
    484 => 216
    486 => 203
    484 => 222
    485 => 231
    
And 1000 numbers from 0 to 50, also 20 times:

    4724 => 358
    4827 => 309
    4818 => 308
    4801 => 309
    4763 => 309
    4763 => 309
    4801 => 359
    4757 => 359
    4766 => 309
    4794 => 309
    4769 => 309
    4789 => 359
    4887 => 359
    4787 => 309
    4761 => 309
    4749 => 309
    4844 => 308
    4798 => 359
    4799 => 308
    4763 => 359
