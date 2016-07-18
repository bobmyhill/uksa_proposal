import numpy as np

def normalise_elements(f):
    elements = ['Si', 'Al', 'Mg', 'Ca', 'Fe']
    for e in elements:
        if e not in f:
            f[e] = 0.
        
    total = f['Si'] + f['Al'] + f['Mg'] + f['Ca'] + f['Fe']
    new_total = f['Si'] + f['Al']/2. + f['Mg'] + f['Ca'] + f['Fe']
    d = 1./new_total
    
    oxides= {'SiO2': d*f['Si'],
             'Al2O3': d*f['Al']/2.,
             'MgO': d*f['Mg'],
             'CaO': d*f['Ca'],
             'FeO': d*f['Fe']}
    return oxides

def W_Righter_Chabot_2011(f):
    oxides = normalise_elements(f)
    return 19.55*oxides['SiO2'] + 8.13*oxides['Al2O3'] - 1.89*oxides['MgO'] - 1.74*oxides['CaO'] + 1.94*oxides['FeO']
def Mo_Righter_Chabot_2011(f):
    oxides = normalise_elements(f)
    return 29.3*oxides['SiO2'] + 30.1*oxides['Al2O3'] + 29.3*oxides['MgO'] + 47.4*oxides['CaO'] + 40.*oxides['FeO']

class forsterite():
    name = 'forsterite'
    params={'formula': {'Mg': 2., 'Si': 1., 'O': 4.}}

class anorthite():
    name = 'anorthite'
    params={'formula': {'Ca': 1., 'Al': 2., 'Si': 2, 'O': 8.}}
    
class diopside():
    name = 'diopside'
    params={'formula': {'Mg': 1., 'Ca': 1., 'Si': 2., 'O': 6.}}


for m in [forsterite, anorthite, diopside]:
    print m.name, Mo_Righter_Chabot_2011(m.params['formula'])

gammas = [0.001, 0.005, 0.01, 0.02, 0.05]
gammas = [5., 50., 75., 100.]

for g in gammas:
    print np.log(g)


xs = [29.3, 34.025, 33.825]

ys = [30., 31., 32., 33., 34.]

for y in ys:
    print (y - xs[0])/(xs[1] - xs[0])
