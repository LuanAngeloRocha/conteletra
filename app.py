with open("sequence.fasta", "r") as fasta_file:
    sequencia = str(fasta_file.read())

    cont = 0

    letras_disponiveis = {
        "A": 0,
        "C": 0,
        "T": 0,
        "G": 0
    }

    for linha in sequencia:
        for letra in linha:
            if letra != "\n" and letra in ["A", "C", "T", "G"]:
                letras_disponiveis[letra] = letras_disponiveis[letra] + 1


    sum = letras_disponiveis["A"] + letras_disponiveis["C"] + letras_disponiveis["T"] + letras_disponiveis["G"];

    porc_a = (letras_disponiveis["A"] / sum) * 100
    porc_c = (letras_disponiveis["C"] / sum) * 100
    porc_t = (letras_disponiveis["T"] / sum) * 100
    porc_g = (letras_disponiveis["G"] / sum) * 100

    print(letras_disponiveis)
    print("A: {}%, C: {}%, T: {}%, G: {}%".format(porc_a, porc_c, porc_t, porc_g))