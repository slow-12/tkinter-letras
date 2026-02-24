import tkinter as tk
from tkinter import messagebox

letra = [
    "Quiero que mires las ojeras de mi cara\nY digas todo lo que ves\nFuck, ya yo perdí la fe, chica\nComo se siente la mirada de tu ser\nQue ayer juraba proteger lo que hoy termina destruyendo",
    "Cuelga el phone, no vistas, girl\nEn el bosque y la montaña se derrama el champagne\nBrilla tu ser, pero a orillas de qué\n¿Cómo está tu alma cuando se termina?",
    "Pero la encontré cerca del café\nDemasiada alejada de tus aires\nBaby, yo lo sé, pero es que nadie ve\nQue no queda calma dentro de mis aires",
    "Pero la encontré cerca del café\nDemasiada alejada de tus aires\nBaby, yo lo sé, pero es que nadie ve\nQue no queda calma dentro de mis aires",
    "Traté de no fallarte, pero muero como siempre\nEn el mismo lugar\nCreo que en otra parte tal vez estará mi suerte\nO estará por el bar",
    "¡Ay chica, si supieras lo que causas!\n¡Ay chica, si tú lo pudieras ver!\nVoy tan vacío, alucinando tu esperanza\nPensé que ya no estaría",
    "Pero la encontré cerca del café\nDemasiada alejada de tus aires\nBaby, yo lo sé, pero es que nadie ve\nQue no queda calma dentro de mis aires",
    "Pero la encontré cerca del café\nDemasiada alejada de tus aires\nBaby, yo lo sé, pero es que nadie ve\nQue no queda calma dentro de mis aires"
]

# Ventana raíz oculta
root = tk.Tk()
root.withdraw()

for estrofa in letra:
    messagebox.showwarning("Advertencia", estrofa)

root.destroy()