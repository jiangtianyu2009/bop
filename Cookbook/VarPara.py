def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


if __name__ == "__main__":
    print(calc(1, 2))
    person('Adam', 45, gender='M', job='Engineer')
