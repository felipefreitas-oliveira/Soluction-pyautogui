import pyautogui
import time
from tkinter import Tk

city = {1288: 86, 1429: 99, 1274: 97, 1249: 122, 1270: 98, 910: 101, 1272: 103, 1295: 104, 1300: 105,
        969: 106, 1355: 107, 1363: 108, 1390: 109, 1410: 111, 1409: 110, 1458: 115, 1067: 116, 909: 128}

i = 1

while i <= 3:
    pyautogui.doubleClick(x=943, y=301)
    time.sleep(2)
    pyautogui.click(x=254, y=253)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')

    root = Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    copy = root.clipboard_get()
    root.destroy()  # Destroi a janela do Tkinter

    try:
        copy = int(copy)
    except ValueError:
        print("O conteúdo da área de transferência não é um número válido.")
        continue


    for cidade, destino in city.items():

        if cidade == copy:

            pyautogui.click(x=722, y=201)
            time.sleep(1)
            pyautogui.click(x=729, y=264)
            time.sleep(2)
            pyautogui.click(x=541, y=271)
            pyautogui.hotkey('ctrl','a')
            pyautogui.write(str(destino))
            pyautogui.click(x=649, y=424)
            time.sleep(0.5)
            pyautogui.write('REALIZAR SERVICO.')
            time.sleep(0.5)
            pyautogui.click(x=158, y=206)
            time.sleep(2)


    pyautogui.click(x=1812, y=169)
    time.sleep(6)

    i += 1

pyautogui.alert('DISTRIBUIÇÃO CONCLUIDA!')