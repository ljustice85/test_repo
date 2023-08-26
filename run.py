import sys
import math


# For your reference
def fahrenheit_to_celsius(temp_f):
    temp_c = (temp_f - 32) * 5 / 9
    return temp_c


# For your reference
def circle_circumference(radius):
    return 2 * math.pi * radius


# Q1
def celsius_to_fahrenheit(temp_c):
    temp_f = (temp_c * 9 / 5) - 32
    return temp_f


# Q2
def circle_area(radius):
    area_of_circle = math.pi * (radius ** 2)
    return area_of_circle


# Q3
def cylinder_volume_surface(radius, height):
    cylinder_surface_volume = math.pi * radius * height + 2 * math.pi * (radius ** 2)
    return cylinder_surface_volume


def count_occurrences(sentence, search_letter):
    count = 0
    for i in sentence:
        if sentence[i] == search_letter:
            count += 1
    return count


if __name__ == '__main__':

    fn_name = sys.argv[1]
    exp_out = sys.argv[-1]

    match fn_name:
        case 'circle_area':
            assert circle_area(float(sys.argv[2])) == float(exp_out)

        case 'celsius_to_fahrenheit':
            assert celsius_to_fahrenheit(float(sys.argv[2])) == float(exp_out)

        case 'cylinder_volume_surface':
            assert cylinder_volume_surface(float(sys.argv[2]), float(sys.argv[3])) == float(exp_out)

