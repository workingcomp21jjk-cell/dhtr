
import tkinter as tk

# змінна для зберігання кліків
score = 0

# функція для кліку
def click():
    global score
    score += 1
    label_score.config(text=f"Кліки: {score}")

# функція для скидання
def reset():
    global score
    score = 0
    label_score.config(text="Кліки: 0")

# створюємо вікно
window = tk.Tk()
window.title("Гра-клікер")
window.geometry("300x200")

# текст з рахунком
label_score = tk.Label(window, text="Кліки: 0", font=("Arial", 16))
label_score.pack(pady=20)

# кнопка кліку
button_click = tk.Button(window, text="Клікни мене!", font=("Arial", 14), command=click)
button_click.pack(pady=10)

# кнопка скидання
button_reset = tk.Button(window, text="Скинути", command=reset)
button_reset.pack()

# запуск гри
window.mainloop()
