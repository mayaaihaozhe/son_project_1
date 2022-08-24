name = 'test'
print('this is a test branch!')
branch_name = 'test branch'


def add(a: int, b: int, env='test'):
    if not isinstance(a, int) or not isinstance(b, int):
        return 0
    return a + b
