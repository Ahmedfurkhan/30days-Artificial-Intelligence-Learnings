import tkinter as tk
from PIL import Image, ImageTk
import cv2

class App:
    def __init__(self, master):
        self.cam = cv2.VideoCapture(0)  # Initialize camera with index 0
        if not self.cam.isOpened():
            raise RuntimeError("Failed to open camera.")
        
        self.master = master
        self.original_image = None
        self.hsv_image = None

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.grid()

        self.original_img_lbl = tk.Label(self.frame)
        self.original_img_lbl.grid(row=0, column=0)

        self.hsv_img_lbl = tk.Label(self.frame)
        self.hsv_img_lbl.grid(row=0, column=1)

        self.update_images()

    def update_images(self):
        ret, frame = self.cam.read()
        if ret:
            self.original_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            self.original_image = Image.fromarray(self.original_image)
            self.original_image = ImageTk.PhotoImage(self.original_image)
            self.original_img_lbl.config(image=self.original_image)

            self.hsv_image = Image.fromarray(self.hsv_image)
            self.hsv_image = ImageTk.PhotoImage(self.hsv_image)
            self.hsv_img_lbl.config(image=self.hsv_image)

        self.master.after(100, self.update_images)

def main():
    root = tk.Tk()
    root.title("Camera App")
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
