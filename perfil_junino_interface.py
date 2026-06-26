import tkinter as tk
from tkinter import messagebox

def iniciar_quiz():
    # Esconde a tela inicial e mostra a tela de perguntas
    frame_inicial.pack_forget()
    frame_pergunta.pack(pady=20)
    mostrar_pergunta()

def mostrar_pergunta():
    global index_pergunta
    if index_pergunta < len(perguntas):
        p = perguntas[index_pergunta]
        lbl_pergunta.config(text=p["q"])
        
        # Atualiza o texto dos botões com as opções
        btn_op1.config(text=p["opcoes"][0], command=lambda: processar_resposta(1))
        btn_op2.config(text=p["opcoes"][1], command=lambda: processar_resposta(2))
        btn_op3.config(text=p["opcoes"][2], command=lambda: processar_resposta(3))
    else:
        mostrar_resultado()

def processar_resposta(escolha):
    global index_pergunta
    p = perguntas[index_pergunta]
    perfil_votado = p["mapeamento"][escolha]
    votos[perfil_votado] += 1
    
    index_pergunta += 1
    mostrar_pergunta()

def mostrar_resultado():
    frame_pergunta.pack_forget()
    frame_resultado.pack(pady=20)
    
    # Descobre o vencedor
    vencedor = max(votos, key=votos.get)
    
    lbl_resultado_titulo.config(text="🎯 SEU PERFIL CAIPIRA É:")
    lbl_resultado_texto.config(text=personagens[vencedor])

def reiniciar_quiz():
    global index_pergunta, votos
    index_pergunta = 0
    votos = {"ze": 0, "maria": 0, "tonho": 0, "dona": 0}
    frame_resultado.pack_forget()
    frame_inicial.pack(pady=20)

# --- CONFIGURAÇÃO DOS DADOS ---
votos = {"ze": 0, "maria": 0, "tonho": 0, "dona": 0}
index_pergunta = 0

perguntas = [
    {
        "q": "Qual comida junina você não vive sem?",
        "opcoes": ["Milho cozido 🌽", "Canjica 🍲", "Pamonha 🫔"],
        "mapeamento": {1: "ze", 2: "maria", 3: "tonho"}
    },
    {
        "q": "O que você mais gosta na festa?",
        "opcoes": ["Quadrilha 💃", "Fogueira 🔥", "Comida 😋"],
        "mapeamento": {1: "dona", 2: "maria", 3: "tonho"}
    },
    {
        "q": "Qual look combina mais com você?",
        "opcoes": ["Xadrez completo 👕", "Chapéu de palha 🎩", "Vestido caipira 👗"],
        "mapeamento": {1: "ze", 2: "tonho", 3: "dona"}
    },
    {
        "q": "Qual música você mais curte?",
        "opcoes": ["Forró animado 🪗", "Xote romântico 💕", "Piseiro junino 🎶"],
        "mapeamento": {1: "dona", 2: "ze", 3: "maria"}
    }
]

personagens = [
    "👒 ZÉ DA ROÇA – o caipira raiz que ama tudo da festa!",
    "🔥 MARIA FOGUEIRA – animada, não sai da quadrilha!",
    "🌽 TONHO MILHO – só pensa em comida junina!",
    "💃 DONA QUADRILHA – nasceu pra dançar forró!"
]
# Ajuste simples para ler o dicionário mantendo a lógica anterior
personagens = {
    "ze": "👒 ZÉ DA ROÇA \n\nO caipira raiz que ama tudo da festa!",
    "maria": "🔥 MARIA FOGUEIRA \n\nAnimada, não sai da quadrilha de jeito nenhum!",
    "tonho": "🌽 TONHO MILHO \n\nEita que a sua praia mesmo é a barraca de comida!",
    "dona": "💃 DONA QUADRILHA \n\nVocê nasceu para arrastar o pé e dançar forró!"
}

# --- CRIAÇÃO DA JANELA INTERFACE ---
janela = tk.Tk()
janela.title("Arraiá dos Perfis Caipiras")
janela.geometry("450x400")
janela.configure(bg="#FFF8EA") # Cor de fundo creme/junina

# --- TELA INICIAL ---
frame_inicial = tk.Frame(janela, bg="#FFF8EA")
frame_inicial.pack(pady=40)

lbl_titulo = tk.Label(frame_inicial, text="🎉🔥 ARRAIÁ DIGITAL 🔥🎉", font=("Arial", 18, "bold"), bg="#FFF8EA", fg="#E65C00")
lbl_titulo.pack(pady=10)

lbl_subtitulo = tk.Label(frame_inicial, text="Descubra qual personagem junino você seria!", font=("Arial", 11), bg="#FFF8EA", fg="#555")
lbl_subtitulo.pack(pady=10)

btn_iniciar = tk.Button(frame_inicial, text="Começar Quiz! 🤠", font=("Arial", 12, "bold"), bg="#FF9F1C", fg="white", padx=20, pady=10, command=iniciar_quiz, relief="flat")
btn_iniciar.pack(pady=30)

# --- TELA DE PERGUNTAS ---
frame_pergunta = tk.Frame(janela, bg="#FFF8EA")

lbl_pergunta = tk.Label(frame_pergunta, text="", font=("Arial", 13, "bold"), bg="#FFF8EA", fg="#333", wraplength=400, justify="center")
lbl_pergunta.pack(pady=20)

# Estilo padrão dos botões de opções
estilo_botoes = {"font": ("Arial", 11), "bg": "#FFF", "fg": "#333", "activebackground": "#FFEAA7", "width": 30, "pady": 8, "relief": "groove"}

btn_op1 = tk.Button(frame_pergunta, **estilo_botoes)
btn_op1.pack(pady=5)

btn_op2 = tk.Button(frame_pergunta, **estilo_botoes)
btn_op2.pack(pady=5)

btn_op3 = tk.Button(frame_pergunta, **estilo_botoes)
btn_op3.pack(pady=5)

# --- TELA DE RESULTADO ---
frame_resultado = tk.Frame(janela, bg="#FFF8EA")

lbl_resultado_titulo = tk.Label(frame_resultado, text="", font=("Arial", 14, "bold"), bg="#FFF8EA", fg="#E65C00")
lbl_resultado_titulo.pack(pady=10)

lbl_resultado_texto = tk.Label(frame_resultado, text="", font=("Arial", 12), bg="#FFF8EA", fg="#333", wraplength=350, justify="center")
lbl_resultado_texto.pack(pady=20)

btn_reiniciar = tk.Button(frame_resultado, text="Jogar Novamente 🔄", font=("Arial", 10, "bold"), bg="#2EC4B6", fg="white", padx=10, pady=5, command=reiniciar_quiz, relief="flat")
btn_reiniciar.pack(pady=10)

# Inicia o app gráfico
janela.mainloop()
