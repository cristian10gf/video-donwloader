import customtkinter as ctk
from pytube import YouTube 

# System settings   
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("720x480")
root.title("YouTube Downloader")

frame_principal = ctk.CTkFrame(master=root) 
frame_principal.pack(fill="both", expand=True, padx=60, pady=20)

label = ctk.CTkLabel(master=frame_principal, text="Hello World!", font=("roboto", 24))
label.pack(padx=10, pady=12)

entry = ctk.CTkEntry(master=frame_principal, placeholder_text="username")
entry.pack(padx=10, pady=12)

button = ctk.CTkButton(master=frame_principal, text="Click me!", command=lambda: print("Hello World!"))
button.pack(padx=10, pady=12)

checkbox = ctk.CTkCheckBox(master=frame_principal, text="Check me!")
checkbox.pack(padx=10, pady=12)


if __name__ == "__main__":
    root.mainloop()