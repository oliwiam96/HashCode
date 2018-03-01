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
            # 0 nikt jej nie chce na razie
            # 1 ktos do niej jedzie
            # 2 ktos na niej jedzie
            # 3 skonczona
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
        print("Chwila t: "+ str(t))
        for i in range(len(rides)):
            if rides[i]['status'] == 0:
                podroz = rides[i]
                #najpierw przydziel
                for j in range(len(vehicles)):
                    pojazd = vehicles[j]
                    #print("Status vehicle: "+ str(pojazd['status']))
                    if(pojazd['status'] == 0):
                        pojazd['status'] = 1
                        pojazd['x2'] = podroz['a']
                        pojazd['y2'] = podroz['b']
                        podroz['status'] = 1
                        #print("Dodaje")
                        pojazd['podroze'].append(i)
                        print("ZNALAZLEM POJAZD " + "index pojazdu ", j, "index podrozy ", i)
                        break
        #potem przesun pojazdy

        for pojazd in vehicles:
            if pojazd['status'] == 0:
                continue
            elif pojazd['status'] == 1:
                print("Jade")
                if pojazd['x1'] < pojazd['x2']:
                    pojazd['x1'] += 1
                elif pojazd['x1'] > pojazd['x2']:
                    pojazd['x1'] -= 1
                else:
                    # x1 == x2
                    if pojazd['y1'] < pojazd['y2']:
                        pojazd['y1'] += 1
                    elif pojazd['y1'] > pojazd['y2']:
                        pojazd['y1'] -= 1
                    else:
                        #(x1, y1) == (x2, y2)
                        #dojechal do klienta
                        indexPodrozy = pojazd['podroze'][-1]
                        podroz = rides[indexPodrozy]
                        pojazd['status'] = 2
                        podroz['status'] = 2
                        pojazd['x2'] = podroz['x']
                        pojazd['y2'] = podroz['y']
            else: #pojazd['status'] == 2
                if pojazd['x1'] < pojazd['x2']:
                    pojazd['x1'] += 1
                elif pojazd['x1'] > pojazd['x2']:
                    pojazd['x1'] -= 1
                else:
                    # x1 == x2
                    if pojazd['y1'] < pojazd['y2']:
                        pojazd['y1'] += 1
                    elif pojazd['y1'] > pojazd['y2']:
                        pojazd['y1'] -= 1
                    else:
                        #(x1, y1) == (x2, y2)
                        #dojechal do celu
                        indexPodrozy = pojazd['podroze'][-1]
                        podroz = rides[indexPodrozy]
                        pojazd['status'] = 0    #zwalniam pojazd
                        #print("Blad!!!" + str(pojazd['status']) + "a drugi ", vehicles[0]['status'], " ", vehicles[1]['status'])
                        podroz['status'] = 3    #podroz zakonczona





    print("POJAZDY KONIEC:")
    print(vehicles)
    print("TRASY KONIEC:")
    print(rides)


    Output = ""
    for i in range(len(vehicles)):
        ile = len(vehicles[i]['podroze'])
        Output += str(ile)
        for indexOfRide in vehicles[i]['podroze']:
            Output += " " + str(indexOfRide)
        Output += "\n"
    print(Output)

    writefile = open("wynik.txt","w")
    writefile.write(Output)
    writefile.close()








if __name__ == "__main__":
    main()