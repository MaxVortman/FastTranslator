import tkinter


class TranslationWindow(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.root = tkinter.Tk()
        self.root.overrideredirect(1)
        x, y = self.root.winfo_pointerxy()
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.configure(background='white')

        self.label_text = tkinter.StringVar()
        label = tkinter.Label(self.root, textvariable = self.label_text)
        label.pack()

    def set_label_text(self, str):
        self.label_text.set(str)

    def start_loop(self):
        self.root.mainloop()