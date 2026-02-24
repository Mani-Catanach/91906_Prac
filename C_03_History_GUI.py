from tkinter import *
from functools import partial # To prevent unwanted windows

class Converter:
    """
    Temperature conversion tool (deg C to deg F or deg F to deg C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                     text="History / Export",
                                     bg="#004C99",
                                     fg="#FFFFFF",
                                     font=("Arial", 12, "bold"), width=12,
                                     command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        """
        Opens history dialogue box and disables history button
        (so that users can't create multiple history boxes).
        """
        DisplayHistory(self)

class DisplayHistory:

    def __init__(self, partner):
        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.history_box = Toplevel()

        # diable history button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, closes history and
        # 'releases' history button
        self.history_box.protocol("WM_DELETE_WINDOW",
                               partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box, width=300,
                                height=200)
        self.history_frame.grid()

        self.history_heading_label = Label(self.history_frame,
                                     text="History / Export",
                                      font=("Arial", 14, "bold"),)
        self.history_heading_label.grid(row=0)

        history_text1 = ("Below are your recent calculations - showing 3 / 3. "
                     "All calculations are shown to the nearest degree.")

        history_text2 = ("Please push <Export> to save your calculations in a text file. "
                         "If the filename already exists it will be overwritten!")

        self.history_text_label = Label(self.history_frame,
                                     text=history_text1, wraplength=350,
                                     justify="left")
        self.history_text_label.grid(row=1, padx=5, pady=5)

        self.history_text_label = Label(self.history_frame,
                                        text=history_text2, wraplength=350,
                                        justify="left")
        self.history_text_label.grid(row=2, padx=5, pady=5)

        # calculate, export, close buttons
        self.button_frame = Frame(self.history_frame)
        self.button_frame.grid()

        # button list ( button text | bg colour | command | row | column)
        button_details_list = [
            ["Calculations", "#99FF99", "", 0, 0],
            ["Export", "#004C99", "", 1, 0],
            ["Close", "#999999", partial(self.close_history, partner), 1, 1]
        ]

        # List to hold button once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#000000", font=("Arial", 12, "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # retrieve calculations, export, and close buttons
        self.calc_button = self.button_ref_list[1]
        self.export_button = self.button_ref_list[2]
        self.close_button = self.button_ref_list[3]

        # List and loop to set background colour on
        # everything except the buttons.
        recolour_list = [self.history_frame, self.history_heading_label,
                         self.history_text_label]

        for item in recolour_list:
            item.config(bg=background)


    def close_history(self, partner):
        """
        Closes history dialogue box and enables history button
        """
        # Put history button back to normal
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Conversion")
    Converter()
    root.mainloop()
