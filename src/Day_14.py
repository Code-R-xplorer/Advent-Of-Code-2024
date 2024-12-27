import math
from typing import List

from utils import read_file
from collections import namedtuple, Counter

Vector = namedtuple('Vector', ['x', 'y'])


class Robot:
    position = Vector(0, 0)
    velocity = Vector(0, 0)

    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity


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
        start_position = robot.position
        velocity = robot.velocity
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


# print(f'Part 1: {math.prod(get_final_robots_in_quads(get_robots(values), 101, 103))}')
# Part 1: 229069152


def print_grid(positions: List[Vector], width: int, height: int) -> None:
    with open("output.txt", "a") as output:
        c = Counter(positions)
        for y in range(height):
            for x in range(width):
                if cell := c.get((x, y)):
                    print(cell, end="", file=output)
                else:
                    print(".", end="", file=output)
            print(file=output)
        output.close()


def simulate_robots_movement(robots, width, height, seconds):
    robots = robots.copy()
    for second in range(seconds):
        with open("output.txt", "a") as output:
            print(f"========== Seconds {second} ===========", file=output)
            output.close()
        for robot in robots:
            start_position = robot.position
            velocity = robot.velocity
            next_position = Vector(
                (start_position.x + velocity.x) % width,
                (start_position.y + velocity.y) % height,
            )
            robot.position = next_position
        print_grid([r.position for r in robots], width, height)


simulate_robots_movement(get_robots(values), 101, 103, 10001)
# Part 2: 7383
