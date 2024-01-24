from tkinter import *

class UserDialog:
    _Ip = ''
    _port = 0
    _nickname = ''

    def __init__(self):
        pass

    @classmethod
    def show_error_box(cls, msg):
        master = Tk()
        Label(master, text=msg).grid(row=0)
        Button(master, text='OK', command=master.destroy).grid(row=1, pady=4)
        master.mainloop()

    @classmethod
    def getUserNickName(cls):
        def getUserNickNameInner():
            nickname = e1.get().strip()
            if not nickname:
                error_label.config(text="Please enter a nickname", fg="red")
            else:
                cls._nickname = nickname
                ClientWindow.destroy()

        ClientWindow = Tk()
        ClientWindow.title("Nickname Input")
        window_width = 300
        window_height = 120
        ClientWindow.geometry(f"{window_width}x{window_height}")
        ClientWindow.resizable(False, False)
        Label(ClientWindow, text='Please enter a nickname').grid(row=0)
        Label(ClientWindow, text='nickname:').grid(row=1)
        e1 = Entry(ClientWindow)
        e1.grid(row=1, column=1)
        error_label = Label(ClientWindow, text="", fg="red")
        error_label.grid(row=2, columnspan=2)

        def on_ok_clicked():
            getUserNickNameInner()

        button = Button(ClientWindow, text='OK', command=on_ok_clicked)
        button.grid(row=3, column=0, columnspan=2, pady=10)

        ClientWindow.mainloop()


if __name__ == '__main__':
    UserDialog.getUserInputIp()
