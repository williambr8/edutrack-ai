def validar_cpf(cpf):
    # remove pontos e traço
    cpf = cpf.replace('.', '').replace('-', '')
    
    # verifica se tem 11 números
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    # evita CPFs com todos números iguais
    if cpf == cpf[0] * 11:
        return False

    # cálculo do primeiro dígito
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = soma % 11
    dig1 = 0 if resto < 2 else 11 - resto

    # cálculo do segundo dígito
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = soma % 11
    dig2 = 0 if resto < 2 else 11 - resto

    # verifica se os dígitos batem
    return cpf[-2:] == f"{dig1}{dig2}"


# exemplo
cpf = "123.456.789-09"
print(validar_cpf(cpf))