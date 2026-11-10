"""
Core objects of the veclib library.
"""

class Vector:
    """Base Vector object."""

    def __init__(self, x: int | float, y: int | float, z: int | float):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self) -> str:
        return f"Vector (x: {self.x}, y: {self.y}, z: {self.z})"

    def __neg__(self):
        """Negate the vector."""
        return Vector(-self.x, -self.y, -self.z)

    def __add__(self, other: "Vector | float | int") -> "Vector":
        """Add another Vector or constant to a Vector."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other, self.z + other)    
        raise NotImplemented

    def __sub__(self, other: "Vector | float | int") -> "Vector":
        """Subtract a vector or a number."""
        return self.__add__(other.__neg__())

    def __radd__(self, other: "Vector | float | int") -> "Vector":
        """Add another Vector or constant to a Vector."""
        return self.__add__(other)

    def __rsub__(self, other: "Vector | float | int") -> "Vector":
        """Subtract another Vector or constant to a Vector."""
        return self.__neg__().__add__(other)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z 

if __name__ == "__main__":
    a = Vector(1, 2, 3)
    b = Vector(1, 2, 3) 
    assert a - b == Vector(0, 0, 0)