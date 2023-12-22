from tkinter import *

class WhiteBoard:
    drawing_tool = "line"
    # Here we have the dictionary with the used colors to paint!
    Colors = {'b': 'blue', 'r': 'red', 'g': 'green', 'o': 'orange', 'y': 'yellow', 'c': 'cyan', 'p': 'purple1',
              'd': 'black', 's': 'snow'}
    line_width = 2

    def draw_line(self, msgLst):
        startX,startY,endX,endY = int(msgLst[1]),int(msgLst[2]),int(msgLst[3]),int(msgLst[4])
        color = msgLst[5]
        self.drawing_area.create_line(startX,startY,endX,endY,fill=self.Colors[color],width=self.line_width)

    def draw_from_msg(self,msg):
        msgLst = msg.split()
        draw_type = msgLst[0]
        if draw_type == 'D':
            self.draw_line(msgLst)
        else:
            pass

    def __init__(self):
        self.color = 'b'
        self.init_whiteboard()
        # self._init_item_button()
        self._init_color_button()
        self.init_drawing_area()

    def show_window(self):
        self.myWhiteBoard.mainloop()

    def init_drawing_area(self):
        self.drawing_area = Canvas(self.myWhiteBoard,width = 1000,height = 700,bg='white')
        self.drawing_area.place(y=0)

    def init_whiteboard(self):
        self.myWhiteBoard = Tk()
        self.myWhiteBoard.geometry('1080x720')

    # def set_drawing_tool(self,tool):
    #     print(tool)
    #     WhiteBoard.drawing_tool = tool
    def set_color(self,color):
        # print(color)
        self.color = color
    def get_text_from_user(self):
        pass


    # def _init_item_button(self):
    #     Button(self.myWhiteBoard, text='line', height=1, width=5, bg='dark goldenrod', font='Arial',
    #            command=lambda: self.set_drawing_tool('line')).place(x=70, y=0)
    #     Button(self.myWhiteBoard, text='rect', height=1, width=5, bg='saddle brown', font='Arial',
    #            command=lambda: self.set_drawing_tool('rectangle')).place(x=140, y=0)
    #     Button(self.myWhiteBoard, text='oval', height=1, width=5, bg='NavajoWhite4', font='Arial',
    #            command=lambda: self.set_drawing_tool('oval')).place(x=210, y=0)
    #     Button(self.myWhiteBoard, text='text', height=1, width=5, bg='SteelBlue4', font='Arial',
    #            command=self.get_text_from_user).place(x=280, y=0)
    #     Button(self.myWhiteBoard, text='pencil', height=1, width=5, bg='DeepSkyBlue2', font='Arial',
    #            command=lambda: self.set_drawing_tool('pencil')).place(x=350, y=0)
    #     Button(self.myWhiteBoard, text='circle', height=1, width=5, bg='Turquoise2', font='Arial',
    #            command=lambda: self.set_drawing_tool('circle')).place(x=420, y=0)
    #     Button(self.myWhiteBoard, text='square', height=1, width=5, bg='CadetBlue1', font='Arial',
    #            command=lambda: self.set_drawing_tool('square')).place(x=490, y=0)
    #     Button(self.myWhiteBoard, text='eraser', height=1, width=5, bg='purple1', font='Arial',
    #            command=lambda: self.set_drawing_tool('eraser')).place(x=560, y=0)
    #     Button(self.myWhiteBoard, text='drag', height=1, width=5, bg='green', font='Arial',
    #            command=lambda: self.set_drawing_tool('drag')).place(x=630, y=0)
    #     Button(self.myWhiteBoard,text='text',height=1,width=5,bg='brown',font='Arial',
    #            command=lambda :self.set_drawing_tool('text').place(x=700,y=0))
    def _init_color_button(self):

        Button(self.myWhiteBoard, height=1, width=5, bg='red',
               command=lambda: self.set_color('r')).place(x=1010,y=50)
        Button(self.myWhiteBoard, height=1, width=5, bg='orange',
               command=lambda: self.set_color('o')).place(x=1010, y=100)
        Button(self.myWhiteBoard, height=1, width=5, bg='yellow',
               command=lambda: self.set_color('y')).place(x=1010, y=150)
        Button(self.myWhiteBoard, height=1, width=5, bg='green',
               command=lambda: self.set_color('g')).place(x=1010, y=200)
        Button(self.myWhiteBoard, height=1, width=5, bg='cyan',
               command=lambda: self.set_color('c')).place(x=1010, y=250)
        Button(self.myWhiteBoard, height=1, width=5, bg='blue',
               command=lambda: self.set_color('b')).place(x=1010, y=300)
        Button(self.myWhiteBoard, height=1, width=5, bg='purple1',
               command=lambda: self.set_color('p')).place(x=1010, y=350)
        Button(self.myWhiteBoard, height=1, width=5, bg='black',
               command=lambda: self.set_color('d')).place(x=1010, y=400)
        Button(self.myWhiteBoard, height=1, width=5, bg='snow',
               command=lambda: self.set_color('s')).place(x=1010, y=450)



if __name__ == '__main__':
    wb = WhiteBoard()