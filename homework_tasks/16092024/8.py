from itertools import permutations

vowels = ['А', 'А', 'А', 'О']
consonants = ['П', 'Р', 'Б', 'Л']


def is_valid_code(code):
    for i in range(len(code) - 1):
        if (code[i] in 'АО' and code[i + 1] in 'АО') or (code[i] not in 'АО' and code[i + 1] not in 'АО'):
            return False
    return True


vowel_permutations = set(permutations(vowels))
consonant_permutations = set(permutations(consonants))

valid_codes = 0

for vowel_perm in vowel_permutations:
    for consonant_perm in consonant_permutations:
        code1 = []
        code2 = []
        for i in range(4):
            code1.append(vowel_perm[i])
            code1.append(consonant_perm[i])

            code2.append(consonant_perm[i])
            code2.append(vowel_perm[i])

        code1 = ''.join(code1)
        code2 = ''.join(code2)

        if is_valid_code(code1):
            valid_codes += 1
        if is_valid_code(code2):
            valid_codes += 1

print(valid_codes)
