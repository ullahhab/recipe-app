import tkinter as tk
from tkinter import messagebox
import random
from recipeSelector import generator, writeFile
from functools import partial

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
recipes = {
    "Monday": "Recipe for Monday",
    "Tuesday": "Recipe for Tuesday",
    "Wednesday": "Recipe for Wednesday",
    "Thursday": "Recipe for Thursday",
    "Friday": "Recipe for Friday",
    "Saturday": "Recipe for Saturday",
    "Sunday": "Recipe for Sunday"
}


def runUI():
    # Create the main window
    global recipes

    def doneCommand():
        global recipes
        writeFile(recipes)
        root.destroy()

    def shuffle_recipes():
        # Gather selected days
        global recipes
        selected_days = {day: recipes[day] for day, var in day_vars.items() if var.get()}
        for day, var in day_vars.items():
            if var.get():
                print(day, recipes[day])
        print("selectedDays", selected_days)

        # Generate shuffled recipes
        recipes = generator(selected_days)
        print(recipes)
        # Update the labels with shuffled recipes
        print(labels)
        for day, label in labels.items():
            label.config(text=f"{day}: {recipes[day]}")

    root = tk.Tk()
    root.title("Recipe Shuffler")

    # List of days and recipes
    # Create a dictionary to hold the checkbox variables
    day_vars = {day: tk.BooleanVar(value=False) for day in days}

    # Create and place the checkboxes for each day
    labels = {}
    for day, var in day_vars.items():
        checkbox = tk.Checkbutton(root, text=f"{day}: {recipes[day]}", variable=var)
        checkbox.pack(anchor="w", padx=20, pady=5)
        labels[day] = checkbox

    # Create and place labels to display recipes

    # Create and place the shuffle button
    shuffle_button = tk.Button(root, text="Shuffle Recipes", command=shuffle_recipes)
    shuffle_button.pack(pady=10)

    doneButton = tk.Button(root, text="Done", command=doneCommand)
    doneButton.pack(pady=10)
    # Run the application
    root.mainloop()


if __name__ == "__main__":
    startup = True

    runUI()
