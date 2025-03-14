import cv2
import numpy as np
import pyautogui
import time
import threading
import tkinter as tk
from tkinter import ttk
import sys
import os

threshold = 0.8
champion = "Lee sin"
running = False
my_thread = None

def resource_path(relative_path):
    """ Obtenha o caminho absoluto para o recurso, lidando com pacotes PyInstaller. """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def aceitarPartida():
    image_to_detect = cv2.imread(resource_path('assets/images/accept.png'), cv2.IMREAD_GRAYSCALE)
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    if len(loc[0]) > 0:
        print("Partida aceita!")
        x, y = loc[::-1][0][0], loc[::-1][1][0]
        pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
        pyautogui.click()
        return

def buscarChampion():
    global champion
    buscarImage = cv2.imread(resource_path('assets\\images\\buscar.png'), cv2.IMREAD_GRAYSCALE)
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    resultBuscar = cv2.matchTemplate(screen_gray, buscarImage, cv2.TM_CCOEFF_NORMED)
    locBuscar = np.where(resultBuscar >= threshold)
    if len(locBuscar[0]) > 0:
        x, y = locBuscar[::-1][0][0], locBuscar[::-1][1][0]
        pyautogui.moveTo(x + (buscarImage.shape[1] // 2), y + (buscarImage.shape[0] // 2),duration=1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.typewrite(str(champion))
        return

def selecionarChampion():
    championImage = cv2.imread(resource_path(f'assets/images/champions/{champion}.png'), cv2.IMREAD_GRAYSCALE)
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    resultChampion = cv2.matchTemplate(screen_gray, championImage, cv2.TM_CCOEFF_NORMED)
    locChampion = np.where(resultChampion >= threshold)
    if len(locChampion[0]) > 0:
        print("Campeão Selecionado")
        x, y = locChampion[::-1][0][0], locChampion[::-1][1][0]
        pyautogui.moveTo(x + (championImage.shape[1] // 2), y + (championImage.shape[0] // 2),duration=1)
        pyautogui.click()
        return

def runa():
    global running
    image_to_detect = cv2.imread(resource_path('assets/images/runa.png'), cv2.IMREAD_GRAYSCALE)
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    if len(loc[0]) > 0:
        print("Runa Confirmada!")
        x, y = loc[::-1][0][0], loc[::-1][1][0]
        pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
        pyautogui.click()
        pyautogui.moveTo(x + 400, y - 200,duration=1)
        pyautogui.click()
        return
    
def fechar():
    global running
    image_to_detect = cv2.imread(resource_path('assets/images/fechar.png'), cv2.IMREAD_GRAYSCALE)
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    if len(loc[0]) > 0:
        x, y = loc[::-1][0][0], loc[::-1][1][0]
        pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
        pyautogui.click()
        return

def confirmar():
    image_to_detect = cv2.imread(resource_path('assets/images/confirm.png'), cv2.IMREAD_GRAYSCALE)
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    if len(loc[0]) > 0:
        print("Partida Confirmada!")
        x, y = loc[::-1][0][0], loc[::-1][1][0]
        pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
        pyautogui.click()
        return

def checkBan():
    global running
    image_to_detect = cv2.imread(resource_path('assets/images/banFlag.png'), cv2.IMREAD_GRAYSCALE)
    while running:
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        if len(loc[0]) > 0:
            break

def buscarBan():
    global running
    image_to_detect = cv2.imread(resource_path('assets/images/buscarBanir.png'), cv2.IMREAD_GRAYSCALE)
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    if len(loc[0]) > 0:
        print("Buscando banimento")
        x, y = loc[::-1][0][0], loc[::-1][1][0]
        pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.typewrite(str(ban))
        return

def banirChampion():
    global running
    banImage = cv2.imread(resource_path(f'assets/images/champions/{ban}.png'), cv2.IMREAD_GRAYSCALE)
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    resultChampion = cv2.matchTemplate(screen_gray, banImage, cv2.TM_CCOEFF_NORMED)
    locChampion = np.where(resultChampion >= threshold)
    if len(locChampion[0]) > 0:
        print("Banimento Selecionado")
        x, y = locChampion[::-1][0][0], locChampion[::-1][1][0]
        pyautogui.moveTo(x + (banImage.shape[1] // 2), y + (banImage.shape[0] // 2),duration=1)
        pyautogui.click()
        return

def banir():
    global running
    image_to_detect = cv2.imread(resource_path('assets/images/banir.png'), cv2.IMREAD_GRAYSCALE)
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    if len(loc[0]) > 0:
        print("Banimento confirmado")
        x, y = loc[::-1][0][0], loc[::-1][1][0]
        pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
        pyautogui.click()
        return

def main_loop():
    while running:
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        if aceitar_var.get(): 
            image_to_detect = cv2.imread(resource_path('assets/images/confirm.png'), cv2.IMREAD_GRAYSCALE)
            result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
            loc = np.where(result >= threshold)
            if len(loc[0]) > 0: aceitarPartida()
        else:
            if aceitar_var.get(): 
                image_to_detect = cv2.imread(resource_path('assets/images/confirm.png'), cv2.IMREAD_GRAYSCALE)
                result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
                loc = np.where(result >= threshold)
                if len(loc[0]) > 0: aceitarPartida()
            else:
                image_to_detect = cv2.imread(resource_path('assets/images/confirm.png'), cv2.IMREAD_GRAYSCALE)
                result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
                loc = np.where(result >= threshold)
                if len(loc[0]) > 0: 
                    aceitarPartida()
                image_to_detect = cv2.imread(resource_path('assets/images/banFlag.png'), cv2.IMREAD_GRAYSCALE)
                result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
                loc = np.where(result >= threshold)
                if Banimento_var.get() and len(loc[0]) > 0:
                    buscarBan()
                    banirChampion()
                    banir()
                image_to_detect = cv2.imread(resource_path('assets/images/selecione.png'), cv2.IMREAD_GRAYSCALE)
                result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
                loc = np.where(result >= threshold)
                if len(loc[0]) > 0:
                    buscarChampion()
                    selecionarChampion()
                    if runa_var.get(): 
                        runa()
                        fechar()
                    confirmar()
        time.sleep(1)

def start():
    global running
    global my_thread
    running = True
    if my_thread is None or not my_thread.is_alive():
        my_thread = threading.Thread(target=main_loop)
        my_thread.start()
        print("Criando nova Threading")
    else: print("A thread já está ativa.")

def stop():
    global running
    running = False

def update_champion():
    global champion
    champion = champion_var.get()
    print("Campeão atualizado para:", champion)
    
def update_ban():
    global ban
    ban = ban_var.get()
    print("Banimento atualizado para:", ban)

def on_closing():
    stop()
    root.destroy()

def filter_champions(event):
    typed_text = champion_var.get()
    if typed_text == '':
        champion_menu['values'] = champions
    else:
        filtered_champions = [champ for champ in champions if typed_text.lower() in champ.lower()]
        champion_menu['values'] = filtered_champions

def filter_bans(event):
    typed_text = ban_var.get()
    if typed_text == '':
        ban_menu['values'] = champions
    else:
        filtered_champions = [champ for champ in champions if typed_text.lower() in champ.lower()]
        ban_menu['values'] = filtered_champions

# Cria a interface gráfica
root = tk.Tk()
root.title("AutoSelect Champion")
root.iconbitmap(resource_path('assets/images/icon.ico'))
root.geometry("400x450")

# Advice
advice_label = tk.Label(root, text="Desenvolvido por vasco #dagam", font=("Arial", 10))
advice_label.pack()

# Ban button
ban_label = tk.Label(root, text="Banimento:", font=("Arial", 12))
ban_label.pack()
list = os.listdir(resource_path('assets/images/champions/'))
champions = []
for champ in list:
    champions += [champ[:-4]]
    
ban_var = tk.StringVar(root)

ban_menu = ttk.Combobox(root, textvariable=ban_var, values=champions)
ban_menu.pack()
ban_menu.bind('<KeyRelease>', filter_bans)

ban_button = tk.Button(root, text="Atualizar Banimento", command=update_ban)
ban_button.pack()

champion_label = tk.Label(root, text="Seu Campeão:", font=("Arial", 12))
champion_label.pack()
champion_var = tk.StringVar(root)

champion_menu = ttk.Combobox(root, textvariable=champion_var, values=champions)
champion_menu.pack()
champion_menu.bind('<KeyRelease>', filter_champions)

update_button = tk.Button(root, text="Atualizar Campeão", command=update_champion)
update_button.pack()

# Flag Runa
runa_var = tk.IntVar()  # Variável para armazenar o estado (0 ou 1)
runa_check = tk.Checkbutton(root, text="Runas Automáticas", variable=runa_var)
runa_check.pack()

# Flag Banimento
Banimento_var = tk.IntVar()  # Variável para armazenar o estado (0 ou 1)
Banimento_check = tk.Checkbutton(root, text="Banimento Automático", variable=Banimento_var)
Banimento_check.pack()

# Flag apenas aceitar partida
aceitar_var = tk.IntVar()  # Variável para armazenar o estado (0 ou 1)
aceitar_check = tk.Checkbutton(root, text="APENAS aceitar partida", variable=aceitar_var)
aceitar_check.pack()

start_button = tk.Button(root, text="Iniciar", command=start, width=10, height=2, font=("Arial",12), bg="#57B9FF")
start_button.pack()

stop_button = tk.Button(root, text="Parar", command=stop, width=10, height=2, font=("Arial",12), bg="#FA5053")
stop_button.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

# python -m PyInstaller --onefile --add-data "assets;assets" interface2.py