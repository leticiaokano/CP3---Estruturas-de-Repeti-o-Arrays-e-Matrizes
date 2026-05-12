temperatura_sala = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

for sala in temperatura_sala:
    soma = 0
    critico = 0
    for temperatura in sala:
        soma = soma + temperatura
        if temperatura >= 33:
            critico += 1

    print(f"Sala1")
    print(soma/4)
    print(critico)

    print(f"Sala2")
    print(soma/4)
    print(critico)

    print(f"Sala3")
    print(soma / 4)
    print(critico)

    print(f"Sala4")
    print(soma / 4)
    print(critico)