from __future__ import annotations


class Parenthesis:

    parenthesis_list = {}

    def __init__(self, open_, close=None, action=None):

        self.open_ = open_
        self.close = close or open_
        self.action = action
        self.parenthesis_list.update({
            open_: self,
            close: self
        })

    @property
    def escaped(self):
        return f'\{self.open_}\{self.close}'

    def exec(self, *args):
        filtered_args = [arg for arg in args if arg is not None]
        return self.action(*filtered_args)

    def __repr__(self) -> str:
        return f'Start: {self.open_}, End: {self.close}'

    def __hash__(self) -> int:
        return self.open_.__hash__()

    def __eq__(self, __o: Parenthesis) -> bool:
        return self is __o


Parenthesis('(', ')')
Parenthesis('|', '|', lambda x: abs(x))
Parenthesis('^', '^', lambda x: -abs(x))
