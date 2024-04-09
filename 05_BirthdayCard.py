import tkinter as tk
from PIL import Image, ImageTk

class BirthdayCard:
    def __init__(self, root):
        self.root = root
        self.root.title("Birthday Card")
        self.root.geometry("1000x800")

        # Load the background image
        background_image = Image.open("background.png")
        self.background_photo = ImageTk.PhotoImage(background_image)

        # Create a label to display the background image
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)


        # TODO:
        # in the intergrated terminal, run the following command:
        # pip install pillow
        # 
        # Task 1:
        # 
        # Add a birthday message label called self.message_label
        # Reference: https://www.geeksforgeeks.org/python-display-text-to-tkinter-text-widget/
        # Place the message label on the card using pack()

        self.message_label = tk.Label(root, text="Happy Birthday!")
        self.message_label.pack()

        # Task 2:
        #
        # Add a button to close the card called self.close_button
        # Reference: https://www.geeksforgeeks.org/python-add-button-to-tkinter-frame/
        # Place the button on the card using pack()
        
        self.close_button = tk.Button(root, text="Close" )
        self.close_button.pack()

def main():
    root = tk.Tk()
    app = BirthdayCard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
