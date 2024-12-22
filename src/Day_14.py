import math

from utils import read_file
from collections import namedtuple

Vector = namedtuple('Vector', ['x', 'y'])
Robot = namedtuple('Robot', ['Position', 'Velocity'])

values = read_file(14, str, False)


def get_robots(inputs):
    robots = []
    for line in inputs:
        raw_pos, raw_vel = line.split(' ')
        pos_x, pos_y = raw_pos.split('=')[1].split(',')
        vel_x, vel_y = raw_vel.split('=')[1].split(',')
        robots.append(Robot(Vector(int(pos_x), int(pos_y)), Vector(int(vel_x), int(vel_y))))
    return robots


def get_final_robots_in_quads(robots, width, height):
    quadrants = [0] * 4

    for robot in robots:
        start_position = robot.Position
        velocity = robot.Velocity
        final_position = Vector(
            (start_position.x + (velocity.x * 100)) % width,
            (start_position.y + (velocity.y * 100)) % height,
        )
        is_left = final_position.x < width // 2
        is_right = final_position.x > width // 2
        is_top = final_position.y < height // 2
        is_bottom = final_position.y > height // 2
        if is_left and is_top:
            quadrants[0] += 1
        elif is_right and is_top:
            quadrants[1] += 1
        elif is_left and is_bottom:
            quadrants[2] += 1
        elif is_right and is_bottom:
            quadrants[3] += 1
    return quadrants


print(f'Part 1: {math.prod(get_final_robots_in_quads(get_robots(values), 101, 103))}')
# Part 1: 229069152
