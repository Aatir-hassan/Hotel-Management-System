from tkinter import *
import check_in_ui
import check_out
import get_info
import customer_info

class Hotel:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        pad = 3
        self.root.title("HOTEL MANAGEMENT SYSTEM")

        # Set the window resolution to a higher value
        window_width = 1200
        window_height = 800
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def create_widgets(self):
        top_frame = self.create_frame(self.root, side="top", bg="#141E46")  # Dark Blue
        bottom_frame = self.create_frame(self.root, side="top", bg="#F3B95F")  # Light Orange

        self.display_welcome_message(top_frame, fg="white")  # Royal Blue text on Dark Blue background

        buttons = [
            ("CHECK IN", check_in_ui.check_in_ui_fun),
            ("CHECK OUT", check_out.check_out_ui),
            ("ROOM DETAILS", get_info.get_info_ui),
            ("CUSTOMER DETAILS", customer_info.customer_info_ui),
            ("EXIT", quit)
        ]

        for row, (text, command) in enumerate(buttons, start=1):
            self.create_button(bottom_frame, text, command, row, bg="#141E46")  # Dark Blue button

    def create_frame(self, parent, side, bg):
        frame = Frame(parent, bg=bg)
        frame.pack(side=side, fill="both", expand=True)
        return frame

    def display_welcome_message(self, frame, fg):
        font_style = ('Helvetica', 50, 'italic bold')  # Change the font style here
        label = Label(frame, font=font_style, text="WELCOME TO BlueOcean HOTEL", fg=fg, anchor="center", bg="#141E46")  # Dark Blue background
        label.pack(fill="both", expand=True)

    def create_button(self, frame, text, command, row, bg):
        font_style = ('Helvetica', 30, 'italic bold')  # Change the font style here
        button = Button(frame, text=text, font=font_style, bg=bg, relief=RIDGE, height=2,
                        width=30, fg="#FFFFFF", anchor="center", command=command)
        button.pack(pady=10)  # Use pack to center the buttons vertically

def home_ui():
    root = Tk()
    application = Hotel(root)
    root.mainloop()

if __name__ == '__main__':
    home_ui()
