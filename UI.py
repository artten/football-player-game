import tkinter as tk
from tkinter import messagebox
import fake_logic_backend


def login(entry_username, entry_password):
    username = entry_username.get()
    password = entry_password.get()
    if fake_logic_backend.login(username, password):
        clear_root()
        draw_homepage()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def next_random_player():
    player_label = root.winfo_children()[1]
    player_label.config(text=f"{fake_logic_backend.get_fake_random_player()}")



def back_to_homepage():
    clear_root()
    draw_homepage()


def search_player():
    clear_root()
    draw_search_player()


def filter_player(name):
    clear_root()
    draw_filtered_player(name)


def random_player():
    clear_root()
    draw_random_player()


def back_to_filtered():
    clear_root()
    draw_search_player()

def choose_difficulty():
    clear_root()
    draw_choose_difficulty()


def play_game(difficulty):
    clear_root()
    draw_play_game(difficulty)


def create_root():
    ret_root = tk.Tk()
    ret_root.geometry("500x500")
    return ret_root


def clear_root():
    for child in root.winfo_children():
        child.destroy()


def draw_login_page():
    label_username = tk.Label(root, text="Username:")
    label_username.place(x=150, y=150)
    entry_username = tk.Entry(root)
    entry_username.place(x=250, y=150)
    label_password = tk.Label(root, text="Password:")
    label_password.place(x=150, y=200)
    entry_password = tk.Entry(root, show="*")
    entry_password.place(x=250, y=200)
    button_login = tk.Button(root, text="Login",
                             command=lambda: login(entry_username, entry_password))
    button_login.place(x=235, y=250)


def draw_homepage():
    label_hello = tk.Label(root, text=f"Hello {fake_logic_backend.get_user_name()}")
    label_hello.place(x=200, y=0)
    label_high_score = tk.Label(root, text=f"Highest score {fake_logic_backend.get_high_score()}")
    label_high_score.place(x=200, y=20)

    button_search_player = tk.Button(root, text="Search Player", command=search_player, width=25, height=3)
    button_search_player.place(x=150, y=150)

    button_random_player = tk.Button(root, text="Learn About Random Players", command=random_player, width=25, height=3)
    button_random_player.place(x=150, y=215)

    button_play = tk.Button(root, text="Play Game", command=choose_difficulty, width=25, height=3)
    button_play.place(x=150, y=280)


def draw_random_player():
    button_search_player = tk.Button(root, text="Back", command=back_to_homepage, width=5, height=1)
    button_search_player.place(x=20, y=20)

    random_player_text = tk.Label(root, text=f"{fake_logic_backend.get_fake_random_player()}")
    random_player_text.place(x=220, y=40)

    button_next_player = tk.Button(root, text="Next Player", command=next_random_player, width=8, height=1)
    button_next_player.place(x=420, y=300)


def draw_search_player():
    button_search_player = tk.Button(root, text="Back", command=back_to_homepage, width=5, height=1)
    button_search_player.place(x=20, y=20)

    label_player_name = tk.Label(root, text="player name")
    label_player_name.place(x=150, y=80)
    player_name = tk.Entry(root, width=25)
    player_name.place(x=250, y=80)

    button_search_player = tk.Button(root, text="Search", command=lambda: filter_player(player_name.get()), width=5, height=1)
    button_search_player.place(x=245, y=425)


def draw_play_game(difficulty):
    button_search_player = tk.Button(root, text="Back", command=back_to_homepage, width=5, height=1)
    button_search_player.place(x=20, y=20)

    random_player_text = tk.Label(root, text=f"{difficulty}")
    random_player_text.place(x=220, y=40)


def draw_choose_difficulty():
    button_search_player = tk.Button(root, text="Back", command=back_to_homepage, width=5, height=1)
    button_search_player.place(x=20, y=20)

    button_search_player = tk.Button(root, text="Hard", command=lambda: play_game("Hard"), width=10, height=3)
    button_search_player.place(x=25, y=100)

    button_search_player = tk.Button(root, text="Medium", command=lambda: play_game("Medium"), width=10, height=3)
    button_search_player.place(x=200, y=100)

    button_search_player = tk.Button(root, text="Easy", command=lambda: play_game("Easy"), width=10, height=3)
    button_search_player.place(x=375, y=100)


def draw_filtered_player(name):
    button_search_player = tk.Button(root, text="Back", command=back_to_filtered, width=5, height=1)
    button_search_player.place(x=20, y=20)

    random_player_text = tk.Label(root, text=f"{fake_logic_backend.get_fake_search_player(name)}")
    random_player_text.place(x=190, y=40)


if __name__ == "__main__":
    root = create_root()
    draw_login_page()
    root.mainloop()
