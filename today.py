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
    miasto = []
    R=0
    C=0
    F=0
    N=0
    B=0
    T=0
    rides = []
    for line in readfile:
        print(line)
        if i == 0:
            metadane = line
            metadane = line.strip('\n')
            metadane = metadane.split(' ')
            R = int(metadane[0])
            C = int(metadane[1])
            F = int(metadane[2])
            N = int(metadane[3])
            B = int(metadane[4])
            T = int(metadane[5])


        else:
            line = line.strip('\n')
            row = line.split(' ')
            rides.append([])
            for elem in row:
                rides[i-1].append(int(elem))


        i += 1

    #print(metadane)
    #print(miasto)
    print(rides)








if __name__ == "__main__":
    main()