
import tkinter

class CalculatorService():

    def __init__(self):
        self.calculatorTextVariable = None
        self.operator = "DEFAULT"
        self.listOfOperatorButtons = []

    def __manageOperatorButtonBindings(self, operator, bg):
        for [op, val] in self.listOfOperatorButtons:
            if op == operator:
                val.canvas.itemconfig("Frame", fill=bg)
                val.canvas.unbind("<Leave>")
                val.canvas.unbind("<Enter>")
            else:
                val.canvas.bind("<Enter>", val.cache["onHover"])
                val.canvas.bind("<Leave>", val.cache["onLeave"])
                val.canvas.itemconfig("Frame", fill="#00d498")

    def setOperator(self, operator, button, bg):
        self.operator = operator
        operators = [op for [op, val] in self.listOfOperatorButtons]

        if operator not in operators:
            self.listOfOperatorButtons.append([operator, button])

        self.__manageOperatorButtonBindings(operator, bg)

    def clear(self):
        if self.operator != "DEFAULT":
            self.operator = "DEFAULT"
            self.__manageOperatorButtonBindings("DEFAULT", "")
            return

        self.calculatorTextVariable.set("0")

        print('Clicked: Clear')

    def backspace(self):
        print('Clicked: Backspace')

    def evaluate(self):
        print('Clicked: Evaluate')

    def percentage(self):
        print('Clicked: Percentage')

    def decimal(self):
        print('Clicked: Decimal')

    def positiveNegative(self):
        print('Clicked: Positive Negative')

    def numberClickSamting(self):
        pass
