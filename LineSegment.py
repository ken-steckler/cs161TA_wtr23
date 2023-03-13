
class Point:
    """Represents an object on a Cartesian plane."""
    def __init__(self, x_coord, y_coord):
        """Specifies the location of an object on a Cartesian plane."""
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord


class Line:
    """Represents the line between 2 points on a Cartesian plane."""
    def __init__(self, point_1, point_2):
        self._point_1 = point_1
        self._point_2 = point_2

    def distance_to(self):
        """Returns the distance between the Point object the method is called on and
        the Point object passed as the argument."""
        x_value = self.point_2.get_x_coord - self.point_1.get_x_coord
        y_value = self.point_2.get_y_coord - self.point_1.get_y_coord
        distance = ((x_value ^ 2)+(y_value ^ 2))**0.5
        return distance


class LineSegment:
    """Identifies the line segment between 2 inputted points."""
    def __init__(self, endpoint_1, endpoint_2):
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def length(self):
        """Calculates the distance between 2 points."""
        # Use Point's distance_to method

    def slope(self):
        """Calculates the slope of 2 points."""
        x_value = self._endpoint_1.get_x_coord - self._endpoint_2.get_x_coord
        y_value = self._endpoint_1.get_y_coord - self._endpoint_2.get_x_coord
        slope = y_value/x_value
        return slope

    def is_parallel_to(self):
        """Compares the slopes of 2 line segments to determine if they're parallel."""
        # abs(num_1 - num_2) < 1e-7
        if abs(line_seg_1.slope() - line_seg_2.slope()) < 1e-7:
            print("The lines are parallel.")
        else:
            print("The lines are not parallel.")