# source: https://www.youtube.com/watch?v=EacYNe7moSs&


# square * square + circle = 16
# triangle * triangle * triangle = 27
# triangle * square = 6

# square * circle * triangle = ?

from z3 import *

square = Int('square')
triangle = Int('triangle')
circle = Int('circle')

solver = Solver()

solver.add(square * square + circle == 16)
solver.add(triangle * triangle * triangle == 27)
solver.add(triangle * square == 6)

if solver.check() == sat:
    model = solver.model()

    # convert to int
    circle_val = model.eval(circle).as_long()
    triangle_val = model.eval(triangle).as_long()
    square_val = model.eval(square).as_long()

    result = square_val * circle_val * triangle_val
    print(result)


# x = Real('x')
# y = Real('y')
# s = Solver()
# s.add(x + y > 5, x > 1, y > 1)
# print(s.check())
# print(s.model())
