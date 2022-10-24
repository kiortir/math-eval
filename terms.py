class Term:
    def __init__(self, value: str):
        self.value = float(value)

    def __repr__(self) -> str:
        return f'Term {self.value}'

    def exec(self):
        return self.value


class Variable:

    def __init__(self, key, parent=None):
        self.parent = parent
        self.key = key

    def exec(self):
        scope = self.parent.scope
        if (scope is None) or (self.key not in scope):
            raise ValueError('Контекст неполон')

        return self.parent.scope[self.key]

    def __repr__(self) -> str:
        return f'Variable "{self.key}"'
