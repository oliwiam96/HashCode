import matplotlib
import scipy
import numpy


def openReadableFile(nazwa):
    f = open(nazwa, "r")
    return f

def main():
    i = 0
    readfile = open("a_example.in", "r")
    metadane = []
    for line in readfile:
        print(line)

        if i == 0:
            metadane = line
        i += 1
    print(metadane)

    print("Hello world")





if __name__ == "__main__":
    main()