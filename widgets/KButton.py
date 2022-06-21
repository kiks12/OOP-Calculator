
import tkinter
from tkinter import ttk
from engine import DrawingEngine

class KButton(ttk.Frame):

    def __init__(self, parent, text, background, onHoverBackground, onClick, column, row, columnspan=1, rowspan=1, *args, **kwargs):
        super().__init__(padding=0,*args, **kwargs)
        self.parent = parent
        self.text = text
        self.background = background
        self.onHoverBackground = onHoverBackground
        self.onClick = onClick
        self.column = column
        self.row = row
        self.columnspan = columnspan
        self.rowspan = rowspan

        self.draw()
        self.configureButtonInteractivity()
        self.grid(column=self.column, row=self.row)

    def __onHover(self, event):
        self.canvas.itemconfig("Frame", fill=self.onHoverBackground)

    def __onLeave(self, event):
        self.canvas.itemconfig("Frame", fill=self.background)

    def configureButtonInteractivity(self):
        self.canvas.bind("<Enter>", lambda e: self.__onHover(e))
        self.canvas.bind("<Leave>", lambda e: self.__onLeave(e))

    def draw(self):
        self.canvas = tkinter.Canvas(
            self.parent,
            height=self['height'],
            width=self['width'],
            bd=-3,
            cursor="hand2",
            relief=tkinter.FLAT
        )
        DrawingEngine().drawRectangle(
            canvas=self.canvas,
            x1=0,
            x2=self['width'],
            y1=0,
            y2=self['height'],
            borderFill=self.onHoverBackground,
            tags=("Frame"),
            fill=self.background
        )
        """
        DrawingEngine().drawRoundedRectangle(
            canvas=self.canvas,
            x=0,
            y=0,
            w=self['width'],
            h=self['height'],
            c=10,
        )
        """

        self.canvas.create_text(self['width'] * 0.5, self['height'] * 0.5, text=self.text, fill='black')
        self.canvas.grid(column=self.column, row=self.row, columnspan=self.columnspan, rowspan=self.rowspan)
