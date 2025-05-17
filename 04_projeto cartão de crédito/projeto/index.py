import re

CARDPATTERNS = [
    (r"^4", "VISA"),
    (r"^5[1-5]", "MASTERCARD"),
    (r"^(36|38)", "DINNERS CLUB"),
    (r"^6011", "DISCOVER"),
    (r"^35", "JCB"),
    (r"^(34|37)", "AMERICAN EXPRESS"),
    (r"^2[01]", "enRoute"),
    (r"^6[02]", "HIPERCARD"),
    (r"^50", "AURA"),
]

def luhn_check(card_number: str) -> bool:
    """
    Valida o número do cartão de crédito usando o algoritmo de Luhn.

    Args:
        card_number (str): Número do cartão de crédito como string.

    Returns:
        bool: True se o número for válido, False caso contrário.
    """
    card_number = re.sub(r"[ -]", "", card_number)
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0

def get_emissor(card_number: str) -> str:
    """
    Identifica o emissor do cartão de crédito com base no prefixo do número informado,
    e valida o número usando o algoritmo de Luhn.

    Args:
        card_number (str): Número do cartão de crédito como string.

    Returns:
        str: Nome do emissor ou 'DESCONHECIDO' se não encontrado ou inválido.
    """
    card_number = re.sub(r"[ -]", "", card_number)

    if not re.fullmatch(r"\d+", card_number) or not luhn_check(card_number):
        return "DESCONHECIDO"

    for pattern, name in CARDPATTERNS:
        if re.match(pattern, card_number):
            return name
    return "DESCONHECIDO"

# Exemplo de teste:
if __name__ == "__main__":
    numero = input("Digite o número do cartão de crédito: ")
    emissor = get_emissor(numero)
    if emissor == "DESCONHECIDO":
        print("Cartão inválido ou emissor desconhecido.")
    else:
        print(f"EMISSOR: {emissor}")