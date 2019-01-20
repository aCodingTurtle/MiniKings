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
    
root = tk.Tk()
TitleScreen = titleScreen(root)
root.mainloop()

class gameScreen():
  
  def __init__(self, window):
    self.window = window
    window.title("MiniKings")

    
    self.Header = tk.Frame(window).pack(side="top")
    
    self.TitleLabel = tk.Label(Header, text='miniKings')
    self.TitleLabel.grid()
    
    self.[N] = tk.[Type]([Frame], text='')
    self.[N].grid()
    
    self.[N] = tk.[Type]([Frame], text='')
    self.[N].grid()
    
    self.[N] = tk.[Type]([Frame], text='')
    self.[N].grid()
    
    
    self.Board = tk.Frame(window).pack(side="left")
    
    for x in range(25):
      
      self.("Square" + str(x)) = tk.Button(Board, text='').grid((x % 5), (x / 5))
      
    