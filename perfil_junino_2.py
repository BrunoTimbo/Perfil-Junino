import random

def perfil_junino_caipira():
    print("🎉🔥 BEM-VINDO AO ARRAIÁ DOS PERFIS CAIPIRAS! 🔥🎉")
    print("Responda e descubra qual personagem junino você seria!\n")

    pontos = 0

    perguntas = [
        {
            "q": "Qual comida junina você não vive sem?",
            "opcoes": ["1 - Milho cozido 🌽", "2 - Canjica 🍲", "3 - Pamonha 🫔"],
            "resposta": 1
        },
        {
            "q": "O que você mais gosta na festa?",
            "opcoes": ["1 - Quadrilha 💃", "2 - Fogueira 🔥", "3 - Comida 😋"],
            "resposta": 2
        },
        {
            "q": "Qual look combina mais com você?",
            "opcoes": ["1 - Xadrez completo 👕", "2 - Chapéu de palha 🎩", "3 - Vestido caipira 👗"],
            "resposta": 3
        },
        {
            "q": "Qual música você mais curte?",
            "opcoes": ["1 - Forró animado 🪗", "2 - Xote romântico 💕", "3 - Piseiro junino 🎶"],
            "resposta": 1
        }
    ]

    for p in perguntas:
        print("\n" + p["q"])
        for op in p["opcoes"]:
            print(op)

        escolha = int(input("Sua resposta (1/2/3): "))

        if escolha == p["resposta"]:
            pontos += 1

    print("\n🎯 RESULTADO FINAL 🎯\n")

    personagens = [
        "👒 ZÉ DA ROÇA – o caipira raiz que ama tudo da festa!",
        "🔥 MARIA FOGUEIRA – animada, não sai da quadrilha!",
        "🌽 TONHO MILHO – só pensa em comida junina!",
        "💃 DONA QUADRILHA – nasceu pra dançar forró!"
    ]

    if pontos == 4:
        print(personagens[0])
    elif pontos == 3:
        print(personagens[1])
    elif pontos == 2:
        print(personagens[2])
    else:
        print(personagens[3])

    print("\n🎊 Obrigado por participar do nosso arraiá digital! 🎊")

perfil_junino_caipira()