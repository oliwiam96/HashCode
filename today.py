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
            rides.append({'a': int(row[0]), 'b': int(row[1]), 'x': int(row[2]), 'y': int(row[3]),'s': int(row[4]), 'f': int(row[5]), 'status': 0})
            # 0 not done
            # 1 in progress
            # 2 done
        i += 1
    print(str(R))
    print(rides)
    readfile.close()

    miasto = []
    for i in range(R):
        row = []
        for j in range(C):
            row.append(1)
        miasto.append(row)

    print(miasto)

    vehicles = []
    for i in range(F):
        vehicles.append({'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0, 'status': 0, 'podroze': []})
            # 0 zupelnie wolny
            # 1 jedzie do klienta
            # 2 jedzie z klientem


    for t in range(T):
        for i in range(len(rides)):
            podroz = rides[i]
            #najpierw przydziel
            for j in range(len(vehicles)):
                pojazd = vehicles[j]
                if(pojazd['status'] == 0):
                    pojazd['status'] = 1
                    pojazd['x2'] = podroz['a']
                    pojazd['y2'] = podroz['b']
                    podroz['status'] = 1
                    pojazd['podroze'].append(i)
                    break
        #potem przesun pojazdy
        for pojazd in vehicles:
            if pojazd['x1'] < pojazd['x2']:
                pojazd['x1'] += 1
            elif pojazd['x1'] > pojazd['x2']:
                pojazd['x1'] -= 1
            else:
                if pojazd['y1'] < pojazd['y2']:
                    pojazd['y1'] += 1
                elif pojazd['y1'] > pojazd['y2']:
                    pojazd['y1'] -= 1
                else:
                    #dojechal do celu
                    if pojazd['status'] == 1:
                        #dojechal do klienta
                        indexPodrozy = pojazd['podroze'][-1]
                        podroz = rides[indexPodrozy]
                        pojazd['x2'] = podroz['x']
                        pojazd['y2'] = podroz['y']
                    elif pojazd['status'] == 2:
                        print("siema")
                        # sukces!!!








if __name__ == "__main__":
    main()