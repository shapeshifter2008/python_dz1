def thesaurus(names):
    name_alphabet = {}
    for name in names:
        first_letter = name[0:1]
        if (name_alphabet.get(first_letter) == None):
            name_alphabet[first_letter] = [name]
        else:
            name_alphabet[first_letter].append(name)

    return name_alphabet

print(thesaurus(["Иван", "Мария", "Петр", "Илья"]))