from main import Calculator


if __name__ == '__main__':
    expression = Calculator('|-16 * (2+10)%2 + 14%(2 + a) - b|')
    print(expression.eval({
        "a": 5,
        "b": 4
    }))

    print(Calculator.static_eval('-^|-16 * (2+10)%2 + 14%(2 + a) - b|^', {
        "a": 5,
        "b": 4
    }))
