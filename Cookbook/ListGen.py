if __name__ == "__main__":
    print([x * x for x in range(1, 11)])
    print([m + n for m in 'ABC' for n in 'XYZ'])
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    print([k + '=' + v for k, v in d.items()])
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [s.lower() for s in L1 if isinstance(s, str)]
    print(L2)
