from collections.abc import Sequence
from collections import defaultdict


def compress(seq: Sequence):
    c = defaultdict(int)
    max_val = 0
    for num in seq:
        c[num] += 1
        if max_val < c[num]:
            max_val = c[num]
    items = sorted(c.items())
    k, v = next(iter(items))
    k, v = bin(k)[2:], bin(v)[2:]
    item_keys = [k for k, _ in items]
    n_bits_max_key = len(bin(max(b - a for a, b in zip(item_keys, item_keys[1:])))) - 2
    n_bits_max_val = len(bin(max_val)) - 2
    result = f"{(n_bits_max_key - len(k)) * '0'}{k}{(n_bits_max_val - len(v)) * '0'}{v}"
    for a, b in zip(items, items[1::]):
        k_a, v_a = a
        k_b, v_b = b
        k_b, v_b = bin(k_b - k_a)[2:], bin(v_b)[2:]
        result += f"{(n_bits_max_key - len(k_b)) * '0'}{k_b}{(n_bits_max_val - len(v_b)) * '0'}{v_b}"
    return result, n_bits_max_key, n_bits_max_val


def decompress(compression_result: str, n_bits_key: int, n_bits_val: int):
    result = list()
    last_k = 0
    for i in range(0, len(compression_result), n_bits_key + n_bits_val):
        k = int(compression_result[i:i + n_bits_key], 2) + last_k
        v = int(compression_result[i + n_bits_key:i + n_bits_key + n_bits_val], 2)
        result += [k] * v
        last_k = k
    return result


def bit_size_of_seq(seq: Sequence):
    return sum((len(bin(e)) - 2 for e in seq))


def test_input():
    input_list = list(map(int, input().split()))
    res = list(compress(input_list))
    res[0] = int(res[0], 2)
    print(f"{bit_size_of_seq(input_list)} => {bit_size_of_seq(res)}")
    print(compress(input_list))
