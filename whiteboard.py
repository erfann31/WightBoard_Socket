from tkinter import *
from tkinter import colorchooser


class WhiteBoard:
    drawing_tool = "line"
    line_width = 2

    def draw_line(self, msgLst):
        print("drawww line")
        startX, startY, endX, endY = int(msgLst[1]), int(msgLst[2]), int(msgLst[3]), int(msgLst[4])
        color = msgLst[5]
        self.drawing_area.create_line(startX, startY, endX, endY, fill=color, width=self.line_width)

    def draw_mouse(self, msgLst):
        client_id = msgLst[4]
        if client_id in self.client_mouse.keys():
            self.delete_object(self.client_mouse[client_id][0])
            self.delete_object(self.client_mouse[client_id][1])
        startX, startY = int(msgLst[1]), int(msgLst[2])
        color = msgLst[3]

        rectangle_id = self.drawing_area.create_rectangle(startX, startY, startX + 5, startY + 5, fill=color)
        text_id = self.drawing_area.create_text(startX, startY - 20, text=client_id, fill=color, width=0, font=18)

        self.client_mouse[client_id] = (rectangle_id, text_id)

    def delete_object(self, object_id):
        self.drawing_area.delete(object_id)

    def draw_from_msg(self, msg):
        msgLst = msg.split()
        draw_type = msgLst[0]
        print(draw_type)
        if draw_type == 'D':
            self.draw_line(msgLst)
        if draw_type == 'M':
            self.draw_mouse(msgLst)
        else:
            pass

    def __init__(self):
        self.color = '#6f78d2'
        self.init_whiteboard()
        self._init_color_button()
        self.init_drawing_area()
        self.client_mouse = dict()

    def show_window(self):
        self.myWhiteBoard.mainloop()

    def init_drawing_area(self):
        self.drawing_area = Canvas(self.myWhiteBoard, width=1000, height=700, bg='white')
        self.drawing_area.place(y=0)

    def init_whiteboard(self):
        self.myWhiteBoard = Tk()
        self.myWhiteBoard.geometry('1080x720')

    def set_color(self, color):
        self.color = color

    def get_text_from_user(self):
        pass

    def _init_color_button(self):
        Button(self.myWhiteBoard, text="Pick Color", command=self.pick_color).place(x=1010, y=50)

    def pick_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.set_color(color)
            print(color)


if __name__ == '__main__':
    wb = WhiteBoard()
