from __future__ import annotations

from collections import defaultdict
from parenthesis import Parenthesis
from operators import Operator
from tokenizer import TokenizerMixin


class Node:

    def __init__(self, value, left_child: Node = None, right_child: Node = None) -> None:
        self.val = value
        self.lch = left_child
        self.rch = right_child

    def __repr__(self) -> str:
        return f'Value: {self.val}'

    def __str__(self) -> str:
        return self.__repr__()

    def exec(self):

        lch_value = self.lch.exec() if self.lch else None
        rch_value = self.rch.exec() if self.rch else None
        return self.val.exec(lch_value, rch_value)



class Calculator(TokenizerMixin):
    def __init__(self, expression: str) -> None:
        self.expression = expression
        tokens = self.tokenize(self.expression)
        self.tree = self.make_tree(tokens)

        self.scope = None

    def make_tree(self, tokens):
        tokens = tokens[:]
        parenthesis_list = []
        operators_map = defaultdict(int)

        idx = -1
        for token in tokens:
            idx += 1

            if isinstance(token, Parenthesis):
                if parenthesis_list and parenthesis_list[-1][0] is token:
                    parenthesis, previous_idx = parenthesis_list.pop()
                    slice = tokens[previous_idx+1:idx]
                    sub = self.make_tree(slice)
                    if parenthesis.action is not None:
                        sub = Node(
                            parenthesis,
                            sub,
                            None
                        )
                    subbed_operrators = [operator for operator in tokens[previous_idx:idx+1] if isinstance(operator, Operator)]
                    tokens = tokens[:previous_idx] + [sub] + tokens[idx+1:]
                    for operator in subbed_operrators:
                        operators_map[operator] -= 1
                    idx = previous_idx
                else:
                    parenthesis_list.append((token, idx))
                    continue
            elif isinstance(token, Operator):
                operators_map[token] += 1

        operators_map = sorted(operators_map.items(),
                               key=lambda x: x[0].priority, reverse=True)

        for operator, count in operators_map:
            for _ in range(count):
                idx = tokens.index(operator)
                right = None
                value = None
                left = None
                try:
                    right = tokens.pop(
                        idx+1) if not isinstance(tokens[idx+1], Operator) else None
                    value = tokens.pop(idx)
                    left = tokens.pop(
                        idx-1) if not isinstance(tokens[idx-1], Operator) and idx != 0 else None
                except IndexError:
                    pass
                node = Node(
                    value,
                    left,
                    right
                )
                tokens.insert(idx-1 if idx != 0 else idx, node)
        return tokens[0]

    def eval(self, scope=None):
        self.scope=scope
        result = self.tree.exec()
        self.scope = None

        return result

    @classmethod
    def static_eval(cls, expression: str, scope=None):
        temp_class = cls(expression)
        value = temp_class.eval(scope)
        return value
