#
#  MINIKINGS
#

import random
import tkinter as tk

class titleScreen():
  
  def __init__(self, window):
    self.window = window
    window.title("MiniKings - Title Screen")
    
    self.TitleLabel = tk.Label(window, text='miniKings')
    self.TitleLabel.pack()
    
    self.NewButton = tk.Button(window, text='New Game')
    self.NewButton.pack()
    
    self.LoadButton = tk.Button(window, text='Load Game')
    self.LoadButton.pack()
    
    self.SettingButton = tk.Button(window, text='Settings')
    self.SettingButton.pack()
    

class gameScreen():
  
  def __init__(self, window):
    self.window = window
    window.title("MiniKings")

    
    self.Header = tk.Frame(window)
    self.Header.grid(column=0,row=0)
    self.Header.grid_rowconfigure(0, weight=1)
    self.Header.grid_columnconfigure(0, weight=1)
    
    self.TitleLabel = tk.Label(self.Header, text='miniKings')
    self.TitleLabel.grid(row=0,column=0,columnspan=3,padx=5)
    
    self.SettingsButton = tk.Button(self.Header, text='Settings')
    self.SettingsButton.grid(row=0,column=3,padx=5)
    
    self.SaveButton = tk.Button(self.Header, text='Save Game')
    self.SaveButton.grid(row=0,column=4,padx=5)
    
    self.ExitButton = tk.Button(self.Header, text='Exit')
    self.ExitButton.grid(row=0,column=5,padx=5)
    

    self.Board = tk.Frame(window).grid(column=0,row=1)
    
    for x in range(25):
      ButtonName = ("Square" + str(x))
      self.ButtonName = tk.Button(self.Board, text=str(x)).grid(column=(x % 5), row=int((x / 5)))
      

root = tk.Tk()
root.grid_rowconfigure(1, weight=1,minsize=200)
root.grid_columnconfigure(0, weight=1)
CurrentScreen = gameScreen(root)
root.mainloop()
