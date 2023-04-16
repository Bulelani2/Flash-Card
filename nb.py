# import random
# from tkinter import *
# import pandas
#
# pos = 0
# data = pandas.read_csv("C:/Users/AGCURCH/Downloads/flash-card-project-start/data/french_words.csv")
# to_learn = data.to_dict(orient="records")
# french_list = {}
#
#
# def french_word():
#     global pos, timer, french_list
#     # window.after_cancel(timer)
#     data = pandas.read_csv("C:/Users/AGCURCH/Downloads/flash-card-project-start/data/french_words.csv")
#     french_list = data["French"].to_list()
#     rand_f_word = random.choice(french_list)
#     pos = french_list.index(rand_f_word)
#     # canvas.itemconfig(rand_word, text=rand_f_word, fill="black")
#     # canvas.itemconfig(f_title, text="French", fill="black")
#     # canvas.itemconfig(card_bg, image=card_front)
#     # timer = window.after(3000, func=english_word)
#     return french_list
#
#
# def english_word():
#     data = pandas.read_csv("C:/Users/AGCURCH/Downloads/flash-card-project-start/data/french_words.csv")
#     english_list = data["English"].to_list()
#     e_word = english_list[pos]
#     # canvas.itemconfig(rand_word, text=e_word, fill="white")
#     # canvas.itemconfig(f_title, text="English", fill="white")
#     # canvas.itemconfig(card_bg, image=card_back)
#
#
# def is_known():
#     for ls in to_learn:
#         if ls in french_list:
#             print(french_list)
#     # to_learn.remove(french_list)
#     # print(len(to_learn))
#     # french_word()
# french_word()
# is_known()
#
# # BACKGROUND_COLOR = "#B1DDC6"
# # FONT_NAME = "Courier"
# # FONT_NAME2 = "Arial"
# #
# # window = Tk()
# # window.title("Flash Cards")
# # window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)
# # timer = window.after(3000, func=english_word)
# #
# # card_front = PhotoImage(file="C:/Users/AGCURCH/Downloads/flash-card-project-start/images/card_front.png")
# # card_back = PhotoImage(file="C:/Users/AGCURCH/Downloads/flash-card-project-start/images/card_back.png")
# # canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
# # card_bg = canvas.create_image(400, 264, image=card_front)
# # f_title = canvas.create_text(400, 100, text="", font=(FONT_NAME, 35, "bold"))
# # rand_word = canvas.create_text(400, 300, text="", font=(FONT_NAME2, 35, "bold"))
# # canvas.grid(column=0, row=0, columnspan=2)
# #
# # wrong_image = PhotoImage(file="C:/Users/AGCURCH/Downloads/flash-card-project-start/images/wrong.png")
# # cross_button = Button(width=50, height=50, image=wrong_image, highlightthickness=0, command=french_word)
# # cross_button.grid(column=0, row=1)
# #
# # right_image = PhotoImage(file="C:/Users/AGCURCH/Downloads/flash-card-project-start/images/right.png")
# # tick_button = Button(width=50, height=50, image=right_image, highlightthickness=0, command=is_known)
# # tick_button.grid(column=1, row=1)
# #
# # french_word()
# #
# # window.mainloop()
