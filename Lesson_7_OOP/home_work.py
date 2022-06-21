from abc import ABC, abstractclassmethod
from curses.textpad import rectangle
from random import choice, random
from turtle import circle


class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("----", "|  |", "----", sep="\n")


class Circle(Shape):
    def draw(self):
        print(" -- ", "-  -", " -- ", sep="\n")


def get_shape() -> Shape:
    options: list[Shape] = [circle(random), rectangle(random)]
    return choice(options)


def main():
    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()
