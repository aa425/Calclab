# Calclab

This Python library provides mathematical functions and utilities, including:

- Solving quadratic equations
- Analyzing parabolas
- Calculating distances between points
- Performing basic arithmetic operations
- Finding equations of lines

More functions will be add in the future

## Installation

You can install this library using pip:

```bash
pip install calculator-library
```
## Usage

```python
from calclab import *

# Initialize the calculator
calc = Calculator()

# Solve quadratic equation: Ax^2 + Bx + C = 0
root1, root2 = calc.quadratic_equation(A, B, C)

# Analyze parabola: y = Ax^2 + Bx + C
root1, root2, axis_of_symmetry, vertex = calc.parabola(A, B, C)

# Calculate distance between two points (X1, Y1) and (X2, Y2)
distance = calc.graph_distance(X1, Y1, X2, Y2)

# Perform square root operation
sqrt_result = calc.sqrt(a)

# Perform square operation
square_result = calc.square(a)

#Perform cube operartion 
cube_result = calc.cube(a)

#Perform line-find operation 
line_equation = calc.line_find(X1, Y1, X2, Y2)

```

## Example

```python

from calculator import Calculator

# Initialize the calculator
calc = Calculator()

# Example: Solving quadratic equation
root1, root2 = calc.quadratic_equation(1, -3, 2)
print("Roots of the equation x^2 - 3x + 2 = 0 are:", root1, "and", root2)
```

## Note:
The quadratic equation and the parabola Function Do MALFUNCTION when the 2 roots are not real, imaginary numbers will be added to those functions in a future update
Please read the Usage/Examples above to use the functions correctly

## Contribute
Please feel free to suggest any ways to make this library better!! 
