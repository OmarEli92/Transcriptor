import tkinter as tk
from tkinter import filedialog, messagebox
from transcriptor import transcribe_video
""" This simple GUI allows you toi select manually the video and the destination folder 
with a simple yet intuitive user interface"""
root = tk.Tk()
root.title("From video to Text")
root.geometry("500x300")
selected_video = tk.StringVar()
selected_output_dir = tk.StringVar()


def choose_video():
    path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.mkv;*.mov;*.avi")])
    if path:
        selected_video.set(path)


def choose_output_dir():
    path = filedialog.askdirectory()
    if path:
        selected_output_dir.set(path)


def transcribe():
    video = selected_video.get()
    output_dir = selected_output_dir.get()
    if not video or not output_dir:
        messagebox.showerror("Error", "Select the video to transcribe and the destination folder.")
        return
    success, log_lines = transcribe_video(video, output_dir)

    for line in log_lines:
        log.insert(tk.END, line + "\n")
    root.update()

    if success:
        messagebox.showinfo("Done!", "Transcription completed!")
    else:
        messagebox.showerror("Error", "There was a mistake during the transcription process.")


# GUI Layout
tk.Label(root, text="Select the video:").pack(pady=5)
tk.Button(root, text="Select Video", command=choose_video).pack()
tk.Label(root, textvariable=selected_video, wraplength=480, fg="blue").pack()

tk.Label(root, text="Choose the destination folder:").pack(pady=10)
tk.Button(root, text="Choose Folder", command=choose_output_dir).pack()
tk.Label(root, textvariable=selected_output_dir, wraplength=480, fg="green").pack()

tk.Button(root, text="Start Transcription", command=transcribe, bg="orange").pack(pady=15)

log = tk.Text(root, height=6, width=60)
log.pack(padx=10)

root.mainloop()
