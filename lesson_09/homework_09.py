import logging

class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "side_a":
            if not isinstance(value, (int, float)):
                raise TypeError(f"Rhombus Side = {value} (type: {type(value)}), length should have type 'int' or 'float'")
            elif value <= 0:
                raise ValueError(f"Rhombus Side = {value} (type: {type(value)}), length should be > 0 and < 180")
            else:
                super().__setattr__(key, value)

        elif key == "angle_a":
            if not isinstance(value, (int, float)):
                raise TypeError(f"Rhombus Angle = {value} (type: {type(value)}), length should have type 'int' or 'float'")
            if value <= 0 or value >= 180:
                raise ValueError(f"Rhombus Angle {value} (type: {type(value)}), length should be > 0 and < 180")
            super().__setattr__(key, value)
            super().__setattr__("angle_b", 180 - value)

        elif key == "angle_b":
            raise AttributeError("The angle_b is calculated automatically through the angle_a")
        else:
            super().__setattr__(key, value)

    def __str__(self):
        return f"Rhombus parameters: side = {self.side_a}, angle_a = {self.angle_a}, angle_b = {self.angle_b}"

r = Rhombus(side_a = 10, angle_a = 30)
print(r)

side_values = [12.0, "15", -17]
for value in side_values:
    try:
        r.side_a = value
        print(r)
        #print(f"OK: side_a = {value}")
    except (TypeError, ValueError) as e:
        # print("Error:", e)
        logging.error(f"Error: {e}")

angle_values = [45.0, "50", -25, 0, 180]
for value in angle_values:
    try:
        r.angle_a = value
        print(r)
        #print(f"OK: angle_a = {value}")
    except (TypeError, ValueError) as e:
        # print("Error:", e)
        logging.error(f"Error: {e}")


