class Romb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Довжина сторони повинна бути більше 0.")
            super().__setattr__(name, value)

        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут повинен бути між 0 і 180 градусами.")
            super().__setattr__(name, value)
            super().__setattr__('angle_b', 180 - value)

        elif name == "angle_b":
            raise AttributeError("Кут angle_b не можна встановити вручну.")
        else:
            super().__setattr__(name, value)

    def __str__(self):
        return f"Ромб: сторона_a={self.side_a}, кут_a={self.angle_a}, кут_b={self.angle_b}"


romb = Romb(10, 70)
print(romb)