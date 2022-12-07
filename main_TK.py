from tkinter import *
from tkinter import ttk


class IsPrime:

    def __init__(self, root):

        root.title("判断质数")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # 结果
        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        self.meters = StringVar()
        # 按钮
        ttk.Button(mainframe, text="判断", command=self.Calculate).grid(column=3, row=3, sticky=W)
        # 文本框
        ttk.Label(mainframe, text="待检：").grid(column=1, row=1, sticky=W)
        # 输入框
        ttk.Label(mainframe, textvariable=self.meters).grid(column=3, row=1, sticky=(W, E))

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<Return>", self.Calculate)

    def Calculate(self, *args):
        try:
            value = int(self.feet.get())
            result = '是质数'
            for i in range(2, value):
                if value % i == 0:
                    result = '不是质数'
                    break
            self.meters.set(result)
        except ValueError:
            pass


root = Tk()
IsPrime(root)
root.mainloop()
