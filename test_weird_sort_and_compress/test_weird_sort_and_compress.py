from random import randint
from weird_sort_and_compress.weird_sort_and_compress import compress, decompress
from unittest import TestCase, main


class TestWeirdSortAndCompress(TestCase):
    def test_compress_decompress(self):
        for array, result in {
            (1, 2, 2, 2, 3): ("101111101", 1, 2),
            (10, 25, 25, 25, 28, 90, 91): ("0010100100111111000011011111100100000101", 6, 2),
            (2, 3, 6, 7, 8, 9): ('101011111011011011', 2, 1)
        }.items():
            self.assertEqual(tuple(compress(array)), result)
            a, b, c = result
            self.assertEqual(tuple(decompress(a, b, c)), array)

    # def test_random(self):
    #     n = 100
    #     for _ in range(n):
    #         random_list = [randint(0, n) for _ in range(n)]
    #         a, b, c = compress(random_list)
    #         self.assertEqual(decompress(a, b, c), random_list)


if __name__ == "__main__":
    main()
