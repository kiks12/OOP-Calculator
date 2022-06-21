
class DrawingEngine():

    def __init__(self):
        pass

    def drawRectangle(self, canvas, x1, x2, y1, y2, borderFill,  **kwargs):
        points = [x1, y2, x1, y1, x2, y1, x2, y2]

        canvas.create_polygon(points, **kwargs)
        self.drawBorders(canvas, x1, y1, x2, y2, borderFill)

    def drawBorders(self, canvas, x, y, w, h, fill):
        canvas.create_line(x  , y,   x+w  , y    , fill=fill, width=2)
        canvas.create_line(x  , y+h, x+w  , y+h  , fill=fill)
        canvas.create_line(x,   y  , x,     y+h  , fill=fill)
        canvas.create_line(x+w, y  , x+w,   y+h  , fill=fill)


    def drawRoundedRectangle(self, canvas, x, y, w, h, c):
        canvas.create_arc(x,   y,   x+2*c,   y+2*c,   start= 90, extent=90, style="arc")
        canvas.create_arc(x+w-2*c, y+h-2*c, x+w, y+h, start=270, extent=90, style="arc")
        canvas.create_arc(x+w-2*c, y,   x+w, y+2*c,   start=  0, extent=90, style="arc")
        canvas.create_arc(x,   y+h-2*c, x+2*c,   y+h, start=180, extent=90, style="arc")
        canvas.create_line(x+c, y,   x+w-c, y    )
        canvas.create_line(x+c, y+h, x+w-c, y+h  )
        canvas.create_line(x,   y+c, x,     y+h-c)
        canvas.create_line(x+w, y+c, x+w,   y+h-c)
