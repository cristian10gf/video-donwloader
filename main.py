import customtkinter as ctk
from pytube import YouTube 

def starDownload():
    try:
        yt_object = YouTube(url.get(), on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        title.config(text=yt_object.title , text_color="white") 
        finish_label.config(text="Downloading...", text_color="blue")
        video.download()
        finish_label.config(text="Download finished", text_color="green")
    except:
        finish_label.config(text="Error, try again", text_color="red")
    
def on_progress(stream, chunk, bytes_remaining):
    progress_bar = round((1 - bytes_remaining / stream.filesize) * 100)
    progress.set(float(progress_bar / 100))
    pPercentege.config(text=f"{progress_bar}%", text_color="white")


# System settings   
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("720x480")
root.title("YouTube Downloader")

# add widgets here
frame_principal = ctk.CTkFrame(master=root) 
frame_principal.pack(fill="both", expand=True, padx=60, pady=20)

title = ctk.CTkLabel(master=frame_principal, text="Insert a YouTube link", font=("roboto", 24))
title.pack(padx=10, pady=10)

url = ctk.StringVar()
link = ctk.CTkEntry(master=frame_principal, placeholder_text="link to video", width=350, height=40, textvariable=url)
link.pack(padx=10, pady=12)

donwload_button = ctk.CTkButton(master=frame_principal, text="Donwload", command=starDownload)
donwload_button.pack(padx=10, pady=12)

finish_label = ctk.CTkLabel(master=frame_principal, text="", font=("roboto", 14))
finish_label.pack(padx=10, pady=10)

pPercentege = ctk.CTkLabel(master=frame_principal, text="0%", font=("roboto", 14))
pPercentege.pack(padx=10, pady=10)

progress = ctk.CTkProgressBar(master=frame_principal, width=400, height=20)
progress.set(0)
progress.pack(padx=10, pady=10)

# start the app
if __name__ == "__main__":
    root.mainloop()