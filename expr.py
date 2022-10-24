from main import Calculator
import timeit

expr = '-16 * (2+10)%2 + 14%(2 + a) - b'
expression = Calculator(expr)
scope = {
    "a": 5000,
    "b": 4000
}


def static_eval():
    return Calculator.static_eval(expr, scope)

def compiled_eval():
    return expression.eval(scope)


def native_eval():
    a = 5000
    b = 4000
    return eval(expr)


if __name__ == '__main__':
    print(static_eval())
    print(compiled_eval())
    print(native_eval())



    print(timeit.timeit('static_eval()', number=50000,
          setup="from __main__ import static_eval"))
    print(timeit.timeit('compiled_eval()', number=50000,
          setup="from __main__ import compiled_eval"))
    print(timeit.timeit('native_eval()', number=50000,
          setup="from __main__ import native_eval"))

    
    