from flask import Flask, render_template, request
import pyautogui
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect', methods=['POST'])
def connect():
    ip = request.form['ip']
    username = request.form['username']
    password = request.form['password']

    pyautogui.hotkey('winleft', 'r')
    time.sleep(1)
    pyautogui.write('mstsc')
    pyautogui.press('enter')
    time.sleep(2)

    #pyautogui.click(873, 328)
    #pyautogui.click(973, 328)
    pyautogui.write(ip)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)

    # "Seçenekleri Göster" düğmesine tıkla
    pyautogui.click(810, 430)
    time.sleep(1)

    # "Başka bir hesap kullan" seçeneğine tıkla
    pyautogui.click(879, 550)
    time.sleep(1)

    # Microsoft hesap e-posta alanına tıkla ve e-posta adresini yaz
    pyautogui.click(797, 264)
    pyautogui.write(username)
    pyautogui.press('tab')
    time.sleep(1)

    # Microsoft hesap şifre alanına tıkla ve şifreyi yaz
    pyautogui.write(password)
    #pyautogui.press('tab')
    #pyautogui.press('tab')
    pyautogui.press('enter')

    return 'Connection Successful.'

if __name__ == '__main__':
    app.run(debug=True)
