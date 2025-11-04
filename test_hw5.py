





























#Test 3.1
import math
import pytest
from hw5_formulas import PlaneFigure

def test_planefigure_cannot_be_instantiated():
    with pytest.raises(TypeError):
        PlaneFigure()


class Circle(PlaneFigure):
    def __init__(self, radius):
        self.radius = radius

    def compute_perimeter(self):
        return 2 * math.pi * self.radius

    def compute_surface(self):
        return math.pi * self.radius**2



def test_circle_instance_and_inheritance():
    circle = Circle(3)
    assert isinstance(circle, Circle)
    assert isinstance(circle, PlaneFigure)
    assert hasattr(circle, "compute_perimeter")
    assert hasattr(circle, "compute_surface")


def test_circle_perimeter_and_surface_values():
    circle = Circle(2)
    expected_perimeter = 2 * math.pi * 2
    expected_surface = math.pi * 2**2
    assert math.isclose(circle.compute_perimeter(), expected_perimeter, rel_tol=1e-5)
    assert math.isclose(circle.compute_surface(), expected_surface, rel_tol=1e-5)


# Test 3.2 
from hw5_formulas import PlaneFigure, Triangle

def test_triangle_inheritance():
    triangle = Triangle(8, 7, 5, 4.2)
    assert isinstance(triangle, PlaneFigure)
    assert hasattr(triangle, "compute_perimeter")
    assert hasattr(triangle, "compute_surface")


def test_triangle_perimeter():
    triangle = Triangle(8, 7, 5, 4.2)
    expected_perimeter = 8 + 7 + 5  # base + c1 + c2
    assert triangle.compute_perimeter() == expected_perimeter


def test_triangle_surface():
    triangle = Triangle(8, 7, 5, 4.2)
    expected_surface = (8 * 4.2) / 2  # (base * height) / 2
    assert triangle.compute_surface() == expected_surface


#Test 3.3 


import math
from hw5_formulas import PlaneFigure, Circle


def test_circle_inheritance():
    circle = Circle(7)
    assert isinstance(circle, PlaneFigure)
    assert hasattr(circle, "compute_perimeter")
    assert hasattr(circle, "compute_surface")


def test_circle_perimeter():
    circle = Circle(7)
    expected_perimeter = 2 * math.pi * 7
    assert math.isclose(circle.compute_perimeter(), expected_perimeter, rel_tol=1e-5)


def test_circle_surface():
    circle = Circle(7)
    expected_surface = math.pi * (7 ** 2)
    assert math.isclose(circle.compute_surface(), expected_surface, rel_tol=1e-5)
