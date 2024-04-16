import tkinter as tk
from tkinter import ttk

# # Função chamada quando o botão é clicado
# def on_submit():
#     print(f"Nome do Campo: {entry_nome_campo.get()}")
#     print(f"Operador: {combo_operador.get()}")
#     print(f"Texto: {entry_texto.get()}")

def on_submit():
    nome_campo = entry_nome_campo.get()
    operador = f" {combo_operador.get()} "
    registros = entry_texto.get().split(",")  # Separa os registros pelo caractere ','
    
    # Monta a string de consulta
    consulta = operador.join([f"{nome_campo} = '{registro.strip()}'" for registro in registros])
    
    # Limpa o bloco de texto antes de inserir o resultado
    text_resultado.delete('1.0', tk.END)
    # Insere a consulta no bloco de texto
    text_resultado.insert(tk.END, consulta)

    print(f"Nome do Campo: {entry_nome_campo.get()}")
    print(f"Operador: {combo_operador.get()}")
    print(f"Texto: {entry_texto.get()}")


# Cria a janela principal
root = tk.Tk()
root.title("Filtro APSDU")
root.geometry("800x600")  # Define o tamanho da janela para 800x600

# Cria o primeiro campo de entrada para o nome do campo
label_nome_campo = tk.Label(root, text="Nome do Campo:")
label_nome_campo.place(x=10, y=10)  # Posiciona no canto superior esquerdo

entry_nome_campo = tk.Entry(root)
entry_nome_campo.place(x=10, y=30)  # Abaixo do label_nome_campo

# Cria o segundo campo de entrada para o texto
label_texto = tk.Label(root, text="Dados separados por ',':")
label_texto.place(x=10, y=60)  # Abaixo do combo_operador

entry_texto = tk.Entry(root)
entry_texto.place(x=10, y=80)  # Abaixo do label_texto

# Cria o menu dropdown para selecionar o operador
label_operador = tk.Label(root, text="Operador:")
label_operador.place(x=10, y=110)  # Abaixo do entry_nome_campo

combo_operador = ttk.Combobox(root, values=[".AND.", ".OR."])
combo_operador.place(x=10, y=130, width=125)  # Abaixo do label_operador

# Cria o botão de submit
submit_button = tk.Button(root, text="Enviar", command=on_submit)
submit_button.place(x=10, y=160)  # Abaixo do entry_texto

# Definindo o bloco de texto do lado direito
text_resultado = tk.Text(root, wrap="word")
text_resultado.place(x=170, y=10, width=620, height=580) 

# Inicia o loop principal da GUI
root.mainloop()
