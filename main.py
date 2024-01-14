import customtkinter
from customtkinter import CTkTextbox
import tkinter.messagebox as messagebox
import selenium
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Movie Finder")
root.geometry("500x500")


def on_click():
    movieTitle = entryBox.get()
    ##### using OMDb API
    url = f"http://www.omdbapi.com/?t={movieTitle}&apikey=7f56c7e2"
    response = requests.get(url)
    data = response.json()

    text_widget.configure(state="normal")
    title = data.get('Title', 'No info')
    year = data.get('Year', 'No info')
    runtime = data.get('Runtime', 'No info')
    genre = data.get('Genre', 'No info')
    plot = data.get('Plot', 'No info')
    ratings = data.get('Ratings', [{'Value': 'No info'}])
    first_rating = ratings[0]['Value'] if ratings else 'No info'

    text_widget.delete('1.0', 'end')
    text_widget.insert('end', f"Title: {title}\n\nYear: {year}\n\nRuntime: {runtime}\n\nGenre: {genre}\n\nPlot: {plot}\n\nRatings: {first_rating}")
    text_widget.configure(state="disabled")
    
    if title=='No info':
        messagebox.showerror("Error", "This movie doesn't exist")
    else: 
        TrailerButton = customtkinter.CTkButton(master=frame, text="Open trailer", command=open_trailer)
        TrailerButton.pack(pady=12, padx=10)


    root.focus()

def on_enter(event):
    on_click()


def open_trailer():
    global title
    movieTitle = entryBox.get()
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)

    url = "https://www.imdb.com/"
    driver.get(url)

    time.sleep(1)

    find=driver.find_element(By.CLASS_NAME, "icb-btn")
    find.click()

    time.sleep(1)

    find=driver.find_element(By.ID, "suggestion-search")
    find.send_keys(movieTitle)
    time.sleep(2)
    find=driver.find_element(By.CLASS_NAME, "ipc-icon.ipc-icon--play-circle-outline-inline.ipc-lockup-overlay__icon")
    find.click()

    input()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=0, padx=0, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Finding information about movie or series", font=("TkTextFont", 20))
label.pack(pady=12, padx=10)

entryBox = customtkinter.CTkEntry(master=frame, placeholder_text="Enter movie or series name", font=("TkTextFont", 16), width=208, height=20)
entryBox.bind('<Return>', on_enter)
entryBox.pack(pady=12, padx=20)

button = customtkinter.CTkButton(master=frame, text="Find", command=on_click)
button.pack(pady=12, padx=10)

text_widget = CTkTextbox(master=frame, width=500, height=250)
text_widget.configure(state="disabled")
text_widget.pack(pady=12, padx=10)


### TO_DO: write info about movie in excel document to watch it later

root.mainloop()
