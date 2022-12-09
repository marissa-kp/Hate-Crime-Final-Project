import pandas as pd

CrimeData = {'Date': [],
             'Year': [],
             'State': [],
             'Total Offenders': [],
             'Race of Offenders': [],
             'Offense Type':[],
             'Incident Location':[],
             'Bias Motivation': []
             }

list_of_files = ['1991.dat', '1992.dat', '1993.dat', '1994.dat', '1995.dat', 
                '1996.dat', '1997.dat', '1998.dat', '1999.DAT', '2000.DAT', 
                '2001.DAT', '2002.DAT', '2003.DAT', '2004.txt', '2005.DAT', 
                '2006.txt', '2007.DAT', '2008.DAT', '2009.DAT', '2010.DAT', 
                '2011.DAT', '2012.DAT', '2013.TXT', '2014.DAT', '2015.txt', 
                '2016.TXT', '2017.txt', '2018.txt','2019.txt', '2020.txt']


for doc in list_of_files:

    f = open(doc, "r")   
    list_of_lines = f.readlines()

    for line in list_of_lines:  
        if line[0:2] == "IR": 
            CrimeData['Date'].append(line[25:33])
            CrimeData['Year'].append(line[25:29])
            CrimeData['State'].append(line[2:4])
            CrimeData['Total Offenders'].append(line[38:40])
            CrimeData['Race of Offenders'].append(line[40])
            CrimeData['Offense Type'].append(line[41:44])
            CrimeData['Incident Location'].append(line[47:49])
            CrimeData['Bias Motivation'].append(line[49:51])

#debug
#print(CrimeData['Date'])
#print(CrimeData['State'])
#print(CrimeData['Total Offenders'])
#print(CrimeData['Race of Offenders'])
#print(CrimeData['Offense Type'])
#print(CrimeData['Incident Location'])
#print(CrimeData['Bias Motivation'])

CrimeDataFrame = pd.DataFrame(CrimeData)

#print(CrimeDataFrame)

for x in range(1991, 2021) :

    print(x, CrimeDataFrame['Year'].value_counts()[str(x)])