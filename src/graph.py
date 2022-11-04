import tkinter as tk
import tkinter.filedialog as fd


class App:
    def __init__(self):
        self.heads = []
        self.values = [[]]
        self.main_win = tk.Tk()
        self.main_win.geometry("800x500")
        self.main_frame = tk.Frame(self.main_win)
        self.open_btn = tk.Button(self.main_frame, command=self.open_file)
        self.open_btn.pack()
        self.canv = tk.Canvas(self.main_frame)
        self.canv.pack()
        self.main_frame.pack()

    def open_file(self):
        file = fd.askopenfile()
        self.heads = list(file.readline().split(','))
        self.values.clear()
        for line in file.readlines():
            self.values.append(list(line.split(',')))
        self.draw_graphs()

    def run(self):
        self.main_win.mainloop()

    def draw_graphs(self):
        needed_values = [[]]
        s = {}
        for value in self.values:
            if type(value) == type(int):
                self.canv.create_line(value)



app = App()
app.run()
