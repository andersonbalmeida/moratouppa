import pyautogui
import time

pyautogui.PAUSE = 2

pyautogui.press('win')
pyautogui.write("firefox")
pyautogui.press('enter')

pyautogui.write('https://class005.github.io/upaa-franciscomoratosp/adotecaes.html')
pyautogui.press('enter')
time.sleep(3)
xa, ya, larguraa, alturaa = pyautogui.locateOnScreen('/home/anderson/Documentos/UPAA2/teste usabilidade/chamar.png')
time.sleep(3)
pyautogui.click(xa + larguraa/2, ya + alturaa/2)


pyautogui.write('https://api.whatsapp.com/send?phone=5511944971953')
pyautogui.press('enter')
time.sleep(3)

x, y, largura, altura = pyautogui.locateOnScreen('/home/anderson/Documentos/UPAA2/teste usabilidade/whats.png')
pyautogui.click(x + largura/2, y + altura/2)
time.sleep(3)