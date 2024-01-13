import customtkinter
import selenium


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Movie Finder")
root.geometry("500x500")

def on_click():
    text = entryBox.get()
    label.configure(text=text)
    root.focus()
def on_enter(event):
    on_click()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=0, padx=0, fill="both", expand=True)

label =  customtkinter.CTkLabel(master=frame, text="Finding information about movie or series", font=("TkTextFont", 20))
label.pack(pady=12, padx=10)

entryBox = customtkinter.CTkEntry(master=frame, placeholder_text="Enter movie or series name", font=("TkTextFont", 16), width=208, height=20)
entryBox.bind('<Return>', on_enter)
entryBox.pack(pady=12, padx=20)


button = customtkinter.CTkButton(master=frame, text="Find", command=on_click)
button.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Film Information")
label.pack(pady=12, padx = 10)


root.mainloop()
