import tkinter as tk
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Viewer")
        self.geometry("500x500")
        self.image = Image.open("images/will.jpg")
        self.image = self.image.resize((500, 500), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(self, image=self.photo)
        self.label.pack()
        self.button = tk.Button(self, text="Open Image", command=self.open_image)
        self.button.pack()

    def open_image(self):
        self.image = Image.open("images/image.jpg")
        self.image = self.image.resize((500, 500), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label.configure(image=self.photo)
        self.label.pack()


if __name__ == "__main__":
    window = App()
    window.mainloop()