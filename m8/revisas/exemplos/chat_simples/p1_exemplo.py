import re

intencoes = {
    r"(((A|a)tualiz|(M|m)ud|(M|m)odific|(A|a)lter|(T|t)roc)(?s).*((P|p)ix|(c|C)r(é|e)dito|(C|c)art|(D|d)(é|e)bito|(P|p)ag)|(desatualiz))": "atualizar_pagamento",
    r"(status|rastre|(O|o)nde est)": "rastrear",
    r"((O|o)(i|i(ê|E)|ii|l(a|á)))": "oi"
}

acoes = {
        "atualizar_pagamento": "Para modificar sua forma de pagamento, liga para nosso 0800 e prepara-se para uma imersão no inferno burocrático kafkiano!",
        "rastrear": 'Para rastrear seu pedido, sente na porta de casa e espere o motoqueiro aparecer. Quando isso acontecer, faltará poucos segundos para sua entrega.',
        "oi": "Olá <3"
}

while True:
    command = input("Você: ")
    if command == "sair":
        print("Até mais")
        exit()
    for key, value in intencoes.items():
        pattern = re.compile(key)
        groups = pattern.findall(command)
        if groups:
            print(acoes[value])
    print()