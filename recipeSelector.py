import random
import os
import keyboard
import tkinter as tk
from tkinter import messagebox


def genRecipe(week, selected, lst, category, food, previousList, recipeSelector, want):
    try:
        for weekday in week:
            if weekday not in want:
                r = random.randint(0, (len(category) - 1))
                while selected[r] > 1:
                    r = random.randint(0, (len(category) - 1))
                selected[r] += 1
                f = random.randint(0, (len(lst[category[r]]) - 1))
                counter = 0
                while (lst[category[r]][f] in food) or (lst[category[r]][f] in previousList):
                    f = random.randint(0, (len(lst[category[r]]) - 1))
                    if counter >= 10:
                        r = random.randint(0, len(category) - 1)
                        while selected[r] > 1:
                            r = random.randint(0, len(category) - 1)
                    counter += 1
                food.append(lst[category[r]][f])
                recipeSelector[weekday] = lst[category[r]][f]
            else:
                recipeSelector[weekday] = want[weekday]
        for day in recipeSelector:
            print(day, ":", recipeSelector[day])
        for i in range(len(selected)):
            selected[i] = 0
    except Exception as e:
        print(r, f, e)


def generator(want):
    previousList = []
    if os.path.exists("./previousList.txt"):
        mem = open("previousList.txt", "r").read().split("\n")
        if mem[-1] == '':
            mem = mem[:-1]
        for recipe in mem:
            previousList.append(recipe.split(":")[1].strip())
    file = open("recipesList.txt", 'r')
    readContent = file.read().split('\n')
    lst = {}
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    recipeSelector = {}
    selected = []
    category = ["Italian:", "American:", "Mexican:", "Asian:", "Mediterranean food:", "Breakfast for dinner:", "Soup:"]
    food = []
    for num in category:
        selected.append(0)
    for line in readContent:
        try:
            if line[-1] != ':':
                lst[foodCat].append(line)
            else:
                foodCat = line
                lst[line] = []
        except Exception as e:
            pass
    for weekday in want:
        food.append(want[weekday])
    genRecipe(week, selected, lst, category, food, previousList, recipeSelector, want)
    return recipeSelector


# while In != "y":

def writeFile(recipeSelector):
    writer = open("previousList.txt", "w")
    #writer = open("testSelector.txt", 'w')
    for day in recipeSelector:
        writer.write(day + ":" + recipeSelector[day] + "\n")
    writer.close()

