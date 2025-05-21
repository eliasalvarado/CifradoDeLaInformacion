# Recurso en: https://github.com/eliasalvarado/CifradoDeLaInformacion/tree/main/Laboratorios/Lab5

import random
import pandas as pd
from tabulate import tabulate

def generateBitsBases(length=10):
    bits = [random.randint(0, 1) for _ in range(length)]
    bases = [random.choice(['↕', '↗']) for _ in range(length)]
    return bits, bases

# Codificar los fotones según los bits y bases de Alice
def encodePhotons(bits, bases):
    photons = []
    for bit, base in zip(bits, bases):
        if base == '↕':
            photons.append('|' if bit == 0 else '-')
        else:
            photons.append('/' if bit == 0 else '\\')
    return photons

# Medir los fotones para Bob (con posible interferencia de Eve)
def measurePhotons(photons, bobBases, interRate=0.2):
    measurements = []
    for photon, base in zip(photons, bobBases):
        # Simular la interferencia de Eve
        if random.random() < interRate:
            # Si Eve elige la misma base, no altera el fotón. Caso contrario, lo altera.
            eveBase = random.choice(['↕', '↗'])
            if eveBase == '↕':
                photon = photon if photon in ['|', '-'] else ('/' if random.choice([0, 1]) == 0 else '\\')
            else:
                photon = photon if photon in ['/', '\\'] else ('|' if random.choice([0, 1]) == 0 else '-')
        # Bob mide el fotón
        if base == '↕':
            measurements.append(0 if photon == '|' else 1)
        else:
            measurements.append(0 if photon == '/' else 1)
    return measurements

def printTable(alice_bits, alice_bases, photons, bob_bases, bob_bits):
    data = []
    for i, (a_bit, a_base, photon, b_base, b_bit) in enumerate(zip(alice_bits, alice_bases, photons, bob_bases, bob_bits)):
        match = a_base == b_base
        use_bit = 'Si' if a_bit == b_bit else 'No'
        usar = match and use_bit == 'Si'
        data.append([i+1, a_bit, a_base, photon, b_base, b_bit, 'Si' if match else 'No', use_bit, usar])
    df = pd.DataFrame(data, columns=["No", "Bit de Alice", "Base de Alice", "Fotón enviado", "Base de Bob", "Bit recibido", "¿Bases coinciden?", "¿Usar bit?", "usar"])
    print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))
    return df




def main():
    alice_bits, alice_bases = generateBitsBases(length=50)
    photons = encodePhotons(alice_bits, alice_bases)
    bob_bases = [random.choice(['↕', '↗']) for _ in range(len(alice_bits))]
    bob_bits = measurePhotons(photons, bob_bases, interRate=0.2)
    
    df = printTable(alice_bits, alice_bases, photons, bob_bases, bob_bits)

    key = df[df['usar']].loc[:, 'Bit de Alice'].tolist()
    #key = [str(bit) for bit in key]
    print("Clave final:", key)
    print("Longitud de la clave:", len(key))


if __name__ == "__main__":
    main()
