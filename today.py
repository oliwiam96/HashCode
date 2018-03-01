import matplotlib
import scipy
import numpy



def main():
    i = 0
    readfile = open("a_example.in", "r")
    metadane = []
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
            rides.append({'a': row[0], 'b': row[1], 'x': row[2], 'y': row[3],'s': row[4], 'f': row[5]})
        i += 1
    print(str(R))
    print(rides)
    readfile.close()





if __name__ == "__main__":
    main()