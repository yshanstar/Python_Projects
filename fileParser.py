import csv
import json
from collections import *
from decimal import *
from FmaCoefficient import *
def dataParser():
    dicts = {'Fast Track':'fast_track_premium', 'AFN':'amazon_fba_premium'}
    with open ('/Users/yeshan/Desktop/Premiums/allPremia2/smoothedCoefficients_0_1_107.csv', 'rb') as f:
        fileReader = csv.reader(f, delimiter=',')
        premiumType = str(fileReader.next()[0])
        #print (premiumType)
        coefficientType = ''
        coeList = []
        asp_dicts= {}
        for row in fileReader:
            col = len(row)
            if col == 1:
                coefficientType = str(row[0])
                #print (coefficientType)
                premiums = dicts.get(coefficientType)
            else:
                start = row[0]
                end = row[1]
                b = row[2]
                c = row[3]
                if premiums != None:
                    asp_range = tuple( [float(start), float(end)] )
                    coefficientList = asp_dicts.get(asp_range)
                    if coefficientList == None:
                        asp_dicts[asp_range] = { (str(premiums) + '_b') :float(b), (str(premiums) + '_c'):float(c) }
                    else:
                        coefficientList[(str(premiums) + '_b')] = float(b)
                        coefficientList[(str(premiums) + '_c')] = float(c)

                    #coe = CoefficientList(float(start),float(end), { (str(premiums) + '_b') :float(b), (str(premiums) + '_c'):float(c)})
                    #print vars(coe)
                    #coeList.append(vars(coe))

        #print (coeList)
        asp_map = OrderedDict(sorted(asp_dicts.items(), key=lambda t: t[0][0]))
        for key, value in asp_map.iteritems():
            #print (key)
            coe = CoefficientList(float(key[0]),float(key[1]), value)
            #print vars(coe)
            coeList.append(vars(coe))

        gl_book = Premiua('fma_version_configs', "3", 'gl_book', "DEFAULT", coeList)
        #print vars(gl_book)
        print json.dumps(vars(gl_book),sort_keys=True, indent=4)

dataParser()
