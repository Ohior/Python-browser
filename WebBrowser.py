# from tkinterweb import HtmlFrame #import the HTML browser
# try:
#   import tkinter as tk #python3
# except ImportError:
#   import Tkinter as tk #python2

# root = tk.Tk() #create the tkinter window
# frame = HtmlFrame(root) #create HTML browser

# # frame.load_website("http://tkhtml.tcl.tk/tkhtml.html") #load a website
# frame.load_website("http://192.168.43.1:8181/web") #load a website
# frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
# root.mainloop()

# # Import tkinter and webview libraries
# from tkinter import *
# import webview

# # define an instance of tkinter
# tk = Tk()

# # size of the window where we show our website
# tk.geometry("800x450")

# # Open website
# webview.create_window('Geeks for Geeks', 'https://geeksforgeeks.org')
# webview.start()

# import required library
import webbrowser
from tkinter import *

# creating root
root = Tk()

# setting GUI title
root.title("WebBrowsers")

# setting GUI geometry
root.geometry("660x660")

# call webbrowser.open() function.
webbrowser.open("http://192.168.43.1:8181/web")

