"""
Rreveals hidden users, mods and admins currently online
at https://chatroom2000.de, one of the largest chat
communities in Germany and provide direct links to their
personal profile pages.
"""
from time import sleep
import json
import sys
import os

import requests



# terminal colors
N = "\033[0m"  # neutral (default color)
R = "\033[31m"  # red
G = "\033[32m"  # green
Y = "\033[33m"  # yellow
B = "\033[34m"  # blue
C = "\033[36m"  # cyan


# target urls
website_url = "https://www.chatroom2000.de"
on_user_url = "https://www.chatroom2000.de/chat/?ReloaderUserOnline"
profile_url = "https://www.chatroom2000.de/chat/profile"


try:
    # read the session id str from file
    with open("session_id.txt", "r") as f:
        session_id = f.read()

    # set the session cookie
    cookies = {"PHPSESSID": session_id}

    # send get request
    response = requests.get(on_user_url, cookies=cookies)

    # read the content (json array) of 'userOnline' from the response
    usr_list = json.loads(response.text)["userOnline"]

except TypeError:
    # if the session id is wrong, print error message and exit
    print("[ERROR]: Der Wert zu 'PHPSESSID' scheint nicht korrekt.")
    sys.exit(0)

except FileNotFoundError:
    # if 'session_id.txt' is missing, print error message and exit
    print("[ERROR]: Die Datei 'session_id.txt' wurde nicht gefunden.\n")
    sys.exit(0)


levels = {
    "0": "Nick reserviert",
    "1": "Bronze",
    "2": "Silber",
    "3": "Gold",
    "4": "VIP",
    "5": "VIP+",
    "6": "Promi",
    "7": "Legende Bronze",
    "8": "Legende Silber",
    "9": "Legende Gold",
}


def usr_level(level):
    """
    Returns the level (value) of a user.
    """
    return levels.get(level)


def usr_sex(sex):
    """
    Returns the gender of a user.
    """
    return "männl" if sex == "m" else "weibl"


def usr_priv(status):
    """
    Translate `user_priv` into a readable string.
    """
    if status == "gast":
        return "Gast"
    if status == "user":
        return "Registrierter User"
    if status == "mod":
        return G + "Moderator" + N
    if status == "admin":
        return R + "Administrator" + N
    return ""


def visibility(status):
    """
    If user is invisible translate `user_simg` into a readable string.
    """
    return B + " -- UNSICHTBAR --   " + N if status == "status_invisible" else ""


def clear_screen():
    """
    Clear screen.
    """
    cmd = "cls" if sys.platform == "win32" else "clear"
    os.system(cmd)


def uncover_admins():
    """
    Show admins and/or mods online.
    """
    clear_screen()

    print(Y + "Admins und Mods\n" + N + "=" * 15, "\n")
    sleep(0.3)

    # display admins in red
    for i, value in enumerate(usr_list):
        if "admin" in usr_list[i]["user_priv"]:
            print(
                R
                + f'{usr_list[i]["user"]} '
                + N
                + (20 - len(usr_list[i]["user"])) * " ",
                f'({usr_sex(usr_list[i]["user_sex"])}) '
                f'{usr_priv(usr_list[i]["user_priv"])}/'
                f'{usr_level(usr_list[i]["user_level"])} '
                + (7 - len(usr_level(usr_list[i]["user_level"]))) * " ",
                Y + "Zum Profil:" + N,
                f'{visibility(usr_list[i]["user_simg"])}',
                "/".join([profile_url, usr_list[i]["user_id"]])
            )
            # prints the complete json array for each admin
            #print(json.dumps(value, indent=4))

        # display mods in green
        if "mod" in usr_list[i]["user_priv"]:
            print(
                G
                + f'{usr_list[i]["user"]} '
                + N
                + (20 - len(usr_list[i]["user"])) * " ",
                f'({usr_sex(usr_list[i]["user_sex"])}) '
                f'{usr_priv(usr_list[i]["user_priv"])}/'
                f'{usr_level(usr_list[i]["user_level"])} '
                + (7 - len(usr_level(usr_list[i]["user_level"]))) * " ",
                f'{visibility(usr_list[i]["user_simg"])}',
                Y + "Zum Profil:" + N,
                "/".join([profile_url, usr_list[i]["user_id"]])
            )
            # prints the complete json array for each mod
            #print(json.dumps(value, indent=4))


def uncover_users():
    """
    Show invisible users online.
    """
    print(Y + "\n\nUnsichtbare User\n" + N + "=" * 16, "\n")
    sleep(0.3)

    for i, value in enumerate(usr_list):
        if "status_invisible" in usr_list[i]["user_simg"] \
        and "user" in usr_list[i]["user_priv"]:
            print(
                C
                + f'{usr_list[i]["user"]} '
                + N
                + (20 - len(usr_list[i]["user"])) * " ",
                f'({usr_sex(usr_list[i]["user_sex"])}) '
                f'{usr_level(usr_list[i]["user_level"])} '
                + (15 - len(usr_level(usr_list[i]["user_level"]))) * " ",
                f'{visibility(usr_list[i]["user_simg"])}',
                Y + "Zum Profil:" + N,
                f'{profile_url}/{usr_list[i]["user_id"]}',
            )
            # prints the complete json array for each user
            #print(json.dumps(value, indent=4))

    sleep(0.5)


def loop():
    """
    Main loop.
    """
    selection = input(
        "\n\n\nDrücken Sie "
        + Y + " Enter "
        + N + " zum Aktualisieren oder "
        + Y + " Strg"
        + N + "+"
        + Y + "C "
        + N + " um zu beenden.\n"
    )

    if selection == "":
        uncover_admins()
        sleep(0.5)
        uncover_users()
        loop()


try:
    uncover_admins()
    uncover_users()
    loop()

except (KeyboardInterrupt, EOFError):
    print("\nProgramm beenden...\n")
    sleep(0.75)
    #clear_screen()
    sys.exit(0)
