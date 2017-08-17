from os import path

def airport():
    print('Airport Routing Filter')
    num=0
    trycount = 0 
    while True and trycount<10:
        while trycount<3:
            try:
                rfile = str(input('Enter the source file name: '))
                sfile = open(rfile,'r')
                trycount = 4
            except FileNotFoundError:
                print('File not found.')
                trycount += 1
                if trycount == 3:
                    return False

        
        ofile = str(input('Enter the output file name: '))
        if path.isfile(ofile):
            q = str(input('File exists... overwrite? (y/n): '))
            if q == 'y':
                ifile = open(ofile,'w')
            else:
                return False
        else:
            ifile = open(ofile,'w')

        airport = str(input('Enter airport symbol: '))
        airport = airport.upper()
        airport = str(airport)
        
    
        line = sfile.readline()
    
        print(type(line))
        while line != '':
            line = str(line)
            linelist = line.strip()
            linelist = line.split(',')
            if linelist[2]==airport or linelist[4]==airport:
                for i in range(len(linelist)-1):
                    ifile.write(linelist[i])
                ifile.write('\n')
                
            line = sfile.readline()

        print('Finised')
        trycount = 10
    
    sfile.close()
    ifile.close()

