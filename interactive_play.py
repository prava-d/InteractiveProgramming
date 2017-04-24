import tkinter

class App:
    def __init__(self, root):
        def do_work(self):
            if self.mouse_pressed:
                self.Hover1.bind("<Enter>", lambda event, h=self.Hover1: h.configure(bg="red"))
                self.Hover1.bind("<Leave>", lambda event, h=self.Hover1: h.configure(bg="SystemButtonFace"))

                self.Hover2.bind("<Enter>", lambda event, h=self.Hover2: h.configure(bg="yellow"))
                self.Hover2.bind("<Leave>", lambda event, h=self.Hover2: h.configure(bg="SystemButtonFace"))
            else:
                self.Hover1.unbind("<Enter>")
                self.Hover1.unbind("<Leave>")
                self.Hover2.unbind("<Enter>")
                self.Hover2.unbind("<Leave>")



    def do_work(self):
        if self.mouse_pressed:
            self.Hover1.bind("<Enter>", lambda event, h=self.Hover1: h.configure(bg="red"))
            self.Hover1.bind("<Leave>", lambda event, h=self.Hover1: h.configure(bg="SystemButtonFace"))

            self.Hover2.bind("<Enter>", lambda event, h=self.Hover2: h.configure(bg="yellow"))
            self.Hover2.bind("<Leave>", lambda event, h=self.Hover2: h.configure(bg="SystemButtonFace"))

    def OnMouseDown(self, event):
        self.mouse_pressed = True
        self.do_work()

    def OnMouseUp(self, event):
        self.mouse_pressed = False
        self.do_work()

root=tkinter.Tk()
app = App(root)
root.mainloop()
