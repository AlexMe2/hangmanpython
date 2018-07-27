import random
import os
cuvinte = [
    'unlagging',
    'rainier',
    'ibarruri',
    'culinarian',
    'ladanum',
    'tranquilized',
    'illuminati',
    'owenism',
    'glove',
    'fecundating',
    'revibrating',
    'chanterelle',
    'gossaert',
    'preengaging',
    'kinetoscope',
    'preenumerated',
    'dextrine',
    'vibrometer',
    'phonographer',
    'unpersonable',
    'inswathing',
    'terror',
    'slavophobia',
    'sound',
    'flaxen',
    'tricentennial',
    'grumpily',
    'conelrad',
    'antimilitarist',
    'superlativeness',
    'outpop',
    'antanarivo',
    'soerabaja',
    'nonbrutal',
    'underbeam',
    'tonnish',
    'percussion',
    'deanthropomorphic',
    'heterogeneousness',
    'pulpwood',
    'chlorinating',
    'nganhwei',
    'boloney',
    'pacificistic',
    'braz',
    'erfurt',
    'ochreous',
    'elkhart',
    'overorganpassing',
    'signet',
    'ecotone',
    'tailstock',
    'zucchini',
    'tacit',
    'mailman',
    'lustring',
    'hypergeusesthesia',
    'nonaddicting',
    'unkemptness',
    'monomethylamine',
    'nontitled',
    'shearer',
    'heath',
    'baseline',
    'pennon',
    'execrate',
    'lima',
    'jarovized',
    'faeroes',
    'overfamous',
    'randolph',
    'interjoist',
    'ditchdigger',
    'requiem',
    'concretionary',
    'abysmal',
    'adam',
    'nonreparable',
    'flirtational',
    'outbudded',
    'nonprofessorial',
    'permutableness',
    'creon',
    'draper',
    'rehung',
    'tiglon',
    'perionychia',
    'myerstown',
    'eisenstein',
    'intercalarily',
    'rancidness',
    'accountableness',
    'program',
    'gautama',
    'jabrud',
    'santana',
    'shingler',
    'stridulated',
    'analytical',
    'saruk']

def alegerecuvant():
    cuvant = random.choice(cuvinte)
    return cuvant
def curatare():
    os.system('clear')
cuvant = alegerecuvant()
print(cuvant)
lungime = len(cuvant)
cenzura = ''
for i in range(lungime):
    cenzura += '*'
cenzura = list(cenzura)
cenzura[0] = cuvant[0]
cenzura[-1] = cuvant[-1]
cenzura = ''.join(cenzura)
curatare()
vieti = 6
print('The word is', cenzura)
print('You have ',vieti)
while '*' in cenzura:
    if vieti == 0:
        print('Game Over\nThe word was', cuvant)
        break

    alegere = input('Your choice ')
    curatare()
    if alegere in cuvant:
        cenzura = list(cenzura)
        for index, litera in enumerate(cuvant):
            if litera == alegere:
                cenzura[index] = alegere
        cenzura = ''.join(cenzura)
    else:
        vieti -= 1
        print('Life remaining {}'.format(vieti))
    print(cenzura)
if cenzura == cuvant:
    print('You guessed it,\n The word was', cenzura)
else:
    print('Maybe next time')
