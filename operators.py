from __future__ import annotations


class Operator:

    operators = {}
    signs = set()

    def __init__(self, sign, priority: int = 0, u_function=None, b_function=None) -> None:

        self.sign = sign
        self.priority = priority
        self.u_function = u_function
        self.b_function = b_function
        self.operators[sign] = self
        self.signs.add(sign)

    def exec(self, *args: list[int | float]):
        filtered_args = [arg for arg in args if arg is not None]
        return self.u_function(*filtered_args) if len(filtered_args) == 1 else self.b_function(*filtered_args)

    @property
    def escaped(self):
        return f'\{self.sign}'

    def __repr__(self) -> str:
        return f'Operator "{self.sign}"'

    def __str__(self) -> str:
        return self.__repr__()

    def __hash__(self) -> int:
        return self.sign.__hash__()

    def __eq__(self, __o: Operator) -> bool:
        return self is __o

    def __gt__(self, __o: Operator) -> bool:
        return self.priority > __o.priority


Operator(sign='+', priority=1, u_function=lambda x: abs(x),
         b_function=lambda x, y: x+y)
Operator(sign='-', priority=1, u_function=lambda x: -
         abs(x), b_function=lambda x, y: x-y)
Operator(sign='*', priority=5, b_function=lambda x, y: x*y)
Operator(sign='/', priority=5, b_function=lambda x, y: x/y)
Operator(sign='%', priority=7, b_function=lambda x, y: x % y)
Operator(sign='**', priority=10, b_function=lambda x, y: x**y)
