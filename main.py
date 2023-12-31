import customtkinter as ctk
from pytube import YouTube 

# Functions
yt_object = None
def starDownload():
    finish_label.configure(text="", text_color="white")
    try:
        global yt_object
        if yt_object == None:
            yt_object = YouTube(url.get(), on_progress_callback=on_progress)
            lista = [stream.resolution for stream in yt_object.streams.filter(file_extension="mp4") if stream.resolution is not None]
            resolutions.configure(values=lista)
            resolutions.set(lista[0])
            resolutions.pack(padx=10, pady=10)
            title.configure(text=yt_object.title , text_color="white", font= ("roboto", 14)) 
            title.update()
            donwload_button.configure(True,text="Download", command=starDownload)
        else:
            donwload()
    except Exception as e:
        print(e)
        finish_label.configure(text="Error, try again", text_color="red")
    
def donwload():
    global yt_object
    video = yt_object.streams.filter(file_extension="mp4", resolution=resolutions.get()).first()
    finish_label.configure(text="Downloading...", text_color="blue")
    finish_label.update()
    video.download()
    finish_label.configure(text="Download finished", text_color="green")
    finish_label.update()
    yt_object = None
    donwload_button.configure(True,text="upload", command=starDownload)

def on_progress(stream, chunk, bytes_remaining):
    progress_bar = round((1 - bytes_remaining / stream.filesize) * 100)
    progress.set(float(progress_bar / 100))
    pPercentege.configure(text=f"{progress_bar}%", text_color="white")
    pPercentege.update()
    progress.update()


# System settings   
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("720x480")
root.title("YouTube Downloader")
root.grid_columnconfigure(0, weight=1)

# add widgets here
frame_principal = ctk.CTkFrame(master=root) 
frame_principal.pack(fill="both", expand=True, padx=60, pady=20)

title = ctk.CTkLabel(master=frame_principal, text="Insert a YouTube link", font=("roboto", 24))
title.pack(padx=10, pady=10)

url = ctk.StringVar()
link = ctk.CTkEntry(master=frame_principal, placeholder_text="link to video", width=350, height=40, textvariable=url)
link.pack(padx=10, pady=12)

donwload_button = ctk.CTkButton(master=frame_principal, text="upload", command=starDownload)
donwload_button.pack(padx=10, pady=12)

finish_label = ctk.CTkLabel(master=frame_principal, text="", font=("roboto", 14))
finish_label.pack(padx=10, pady=10)

pPercentege = ctk.CTkLabel(master=frame_principal, text="0%", font=("roboto", 20))
pPercentege.pack(padx=10, pady=10)

progress = ctk.CTkProgressBar(master=frame_principal, width=400, height=20)
progress.set(0)
progress.pack(padx=10, pady=10)

resolutions = ctk.CTkComboBox(master=frame_principal, 
                              width=400, height=40, 
                              corner_radius=10,
                              justify="center", font=("roboto", 14), 
                              button_color="blue")

# start the app
if __name__ == "__main__":
    root.mainloop()