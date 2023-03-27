'''
專案在學習grid的編排
'''

import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')
        ttkStyle.configure('red.TFrame', background='#ff0000')
        ttkStyle.configure('white.TFrame', background='#ffffff')
        ttkStyle.configure('yellow.TFrame', background='yellow')
        ttkStyle.configure('white.TLabel', background='#ffffff')
        ttkStyle.configure('gridLabel.TLabel', font=(
            'Helvetica', 16), foreground='#555555')
        ttkStyle.configure('gridEntry.TEntry', font=('Helvetica', 16))

        mainFrame = ttk.Frame(self)
        mainFrame.pack(expand=True, fill=tk.BOTH, padx=30, pady=30)

        topFrame = ttk.Frame(mainFrame, height=100)
        topFrame.pack(fill=tk.X)

        ttk.Label(topFrame, text="BMI試算", font=(
            'Helvetica', '20')).pack(pady=20)

        bottomFrame = ttk.Frame(mainFrame)
        bottomFrame.pack(expand=True, fill=tk.BOTH)
        bottomFrame.columnconfigure(0, weight=3, pad=20)
        bottomFrame.columnconfigure(1, weight=5, pad=20)
        bottomFrame.rowconfigure([0, 3, 4, 5, 6], weight=1, pad=20)

        ttk.Label(bottomFrame, text="姓名:", style='gridLabel.TLabel').grid(
            column=0, row=0, sticky=tk.E)
        self.nameEntry = ttk.Entry(bottomFrame, style='gridEntry.TEntry')
        self.nameEntry.grid(column=1, row=0, sticky=tk.W, padx=10)
        ttk.Label(bottomFrame, text="出生年月日:", style='gridLabel.TLabel').grid(
            column=0, row=1, sticky=tk.E)
        ttk.Label(bottomFrame, text="(2000/03/01)",
                  style='gridLabel.TLabel').grid(column=0, row=2, sticky=tk.E)
        self.birthEntry = ttk.Entry(bottomFrame, style='gridEntry.TEntry')
        self.birthEntry.grid(column=1, row=1, rowspan=2, sticky=tk.W, padx=10)

        ttk.Label(bottomFrame, text="身高(cm):", style='gridLabel.TLabel').grid(
            column=0, row=3, sticky=tk.E)
        self.heightEntry = ttk.Entry(bottomFrame, style='gridEntry.TEntry')
        self.heightEntry.grid(column=1, row=3, sticky=tk.W, padx=10)

        ttk.Label(bottomFrame, text="體重(kg):", style='gridLabel.TLabel').grid(
            column=0, row=4, sticky=tk.E)
        self.weightEntry = ttk.Entry(bottomFrame, style='gridEntry.TEntry')
        self.weightEntry.grid(column=1, row=4, sticky=tk.W, padx=10)

        self.messageText = tk.Text(
            bottomFrame, height=5, width=35, state=tk.DISABLED)
        self.messageText.grid(column=0, row=5, sticky=tk.N+tk.S, columnspan=2)

        commitBtn = ttk.Button(bottomFrame, text="計算", command=self.bmi_value)
        commitBtn.grid(column=1, row=6, sticky=tk.W)

    def bmi_value(self):
        name = self.nameEntry.get()
        height = float(self.heightEntry.get())
        weight = float(self.weightEntry.get())

    # 計算 BMI 值
        bmi = weight / ((height / 100) ** 2)

    # 將 BMI 值轉換為字串
        bmi_str = "{:.2f}".format(bmi)

    # 將結果顯示在 self.messageText 中
        self.messageText.configure(state=tk.NORMAL)
        self.messageText.delete(1.0, tk.END)
        self.messageText.insert(tk.END, f"{name} 的 BMI 值為 {bmi_str}")
        self.messageText.configure(state=tk.DISABLED)


def main():
    '''
    這是程式的執行點
    '''
    window = Window()
    window.title("BMI計算")
    # window.geometry("400x500")
    window.mainloop()


if __name__ == "__main__":
    main()