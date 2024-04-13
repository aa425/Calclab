import math
class Calculator:
    def quadratic_equation(self, A, B, C):
        Discriminant = B * B - 4 * A * C
        sqrt_Discriminant = math.sqrt(Discriminant)
        
        if Discriminant < 0:
            real_part = -B / (2 * A)
            imaginary_part = sqrt_discriminant / (2 * A)
            Root1 = complex(real_part, imaginary_part)
            Root2 = complex(real_part, -imaginary_part)
            return Root1, Root2
        else:
            Root1 = (-B + sqrt_Discriminant) / (2 * A)
            Root2 = (-B - sqrt_Discriminant) / (2 * A)
            
            return Root1, Root2
    def parabola(self, A, B, C):
            Discriminant = B * B - 4 * A * C
            sqrt_Discriminant = math.sqrt(Discriminant)
            axis_of_symmetry = -B / (2 * A)
            vertex = A * axis_of_symmetry**2 + B * axis_of_symmetry + C

            if Discriminant < 0:
                real_part =-B / (2 * A)
                imaginary_part = sqrt_discriminant / (2 * A)
                Root1 = complex(real_part, imaginary_part)
                Root2 = complex(real_part, -imaginary_part)
            else:
                Root1 = (-B + sqrt_Discriminant) / (2 * A)
                Root2 = (-B - sqrt_Discriminant) / (2 * A)

            return Root1, Root2, axis_of_symmetry, vertex
    def graph_distance(self, X1, Y1, X2, Y2):
        A = (X2 - X1) * (X2 - X1)
        B = (Y2 - Y1) * (Y2 - Y1)
        C = A + B 
        D = math.sqrt(C)
        return D
    def sqrt(self, a):
        b = math.sqrt(a)
        return b
    def square(self, a):
        b = a * a
        return b 
    def cube(self, a):
        b = a * a * a
        return b 
    def line_find(self, X1, Y1, X2, Y2):
        slope = (Y2 - Y1) / (X2 - X1)
        y_intercept = Y1 - slope * X1
        equation = f"Y = {slope}x + {y_intercept}"
        if y_intercept < 0: 
            equation = f"Y = {slope}x - {abs(y_intercept)}"
        return equation

