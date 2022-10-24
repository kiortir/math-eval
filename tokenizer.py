import re
from operators import Operator
from parenthesis import Parenthesis
from terms import Term, Variable


class TokenizerMixin:

    __operators = ''.join(
        [operator.escaped for operator in Operator.operators.values()])

    __parenthesis = ''.join(
        [parenthesis.escaped for parenthesis in Parenthesis.parenthesis_list.values()])

    __re_str = fr'\d+[\.,]\d+|\d+|[{__operators}]+|\w+|[{__parenthesis}]'

    __TOKENS = re.compile(__re_str)

    def __get_class(self, token: str):
        try:
            return Term(float(token))
        except ValueError:
            return Operator.operators.get(token) or Parenthesis.parenthesis_list.get(token) or Variable(token, self)

    def tokenize(self, string: str):
        parsed_tokens = self.__TOKENS.finditer(string)
        tokens = [self.__get_class(token.group()) for token in parsed_tokens]
        return tokens