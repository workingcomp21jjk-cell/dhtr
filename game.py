import tkinter as tk

from tkinter import messagebox

import random
 
# Функція, яка визначає переможця гри

def determine_winner(player_choice, computer_choice):

    if player_choice == computer_choice:

        return "Нічия!"

    elif (player_choice == "Камінь" and computer_choice == "Ножиці") or \

         (player_choice == "Ножиці" and computer_choice == "Бумага") or \

         (player_choice == "Бумага" and computer_choice == "Камінь"):

        return "Ви перемогли!"

    else:

        return "Комп'ютер переміг!"
 
# Функція для обробки вибору користувача та визначення переможця

def play_game(choice):

    computer_choice = random.choice(["Камінь", "Ножиці", "Бумага"])

    result = determine_winner(choice, computer_choice)

    messagebox.showinfo("Результат", f"Ви обрали: {choice}\nКомп'ютер обрав: {computer_choice}\n{result}")
 
# Створення вікна та його налаштування

root = tk.Tk()

root.title("Камінь, ножиці, бумага")
 
# Створення кнопок для вибору гравцем

btn_rock = tk.Button(root, text="Камінь", width=10, command=lambda: play_game("Камінь"))

btn_scissors = tk.Button(root, text="Ножиці", width=10, command=lambda: play_game("Ножиці"))

btn_paper = tk.Button(root, text="Бумага", width=10, command=lambda: play_game("Бумага"))
 
# Розміщення кнопок на вікні

btn_rock.grid(row=0, column=0, padx=10, pady=5)

btn_scissors.grid(row=0, column=1, padx=10, pady=5)

btn_paper.grid(row=0, column=2, padx=10, pady=5)
 
# Запуск головного циклу програми

root.mainloop()
 