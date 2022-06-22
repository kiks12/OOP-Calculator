
import tkinter
from widgets.KButton import KButton
from calculatorService import CalculatorService

class CalculatorGUI():

    def __init__(self, service):
        self.service = service

        self.normalButtonColor = "#e8e8e8"
        self.normalButtonAccentColor = "#d6d6d6"
        self.utilityButtonColor = "#cfe3dd"
        self.utilityButtonAccentColor = "#b9c9c5"
        self.operationButtonColor = "#00d498"
        self.operationButtonAccentColor = "#00c48d"
        self.operationButtonClickedColor = "#03ab7c"
        self.equalButtonColor = "#02ad7d"
        self.equalButtonAccentColor = "#01946a"

        self.setupWindow()
        self.root.update()

        self.buttonHeight = self.root.winfo_height() * 0.166666666
        self.buttonWidth = self.root.winfo_width() * 0.25

        self.calculatorText = tkinter.StringVar()
        self.calculatorText.set('0')
        self.service.calculatorTextVariable = self.calculatorText
        self.setupEntry()

        self.setupFirstRowButtons()
        self.setupSecondRowButtons()
        self.setupThirdRowButtons()
        self.setupFourthRowButtons()
        self.setupFifthRowButtons()

        self.root.mainloop()

    def setupWindow(self):
        self.root = tkinter.Tk()
        self.root.title("Calculator")
        self.root.geometry("280x420")
        self.root.resizable(False, False)
        self.root.config(bg=self.normalButtonAccentColor)

    def setupEntry(self):
        self.inputFrame = tkinter.ttk.Frame(
            self.root,
            height=self.buttonHeight,
            width=self.root.winfo_width(),
        )

        self.calculatorInput = tkinter.Entry(
            self.inputFrame,
            textvariable=self.calculatorText,
            justify=tkinter.RIGHT,
            state=tkinter.DISABLED,
            font=("Arial", 40),
            relief=tkinter.FLAT,
            insertborderwidth=0,
            selectborderwidth=0,
            borderwidth=0,
        )
        self.calculatorInput.place(
            height=self.buttonHeight,
            width=self.root.winfo_width()
        )
        self.inputFrame.grid(column=0, row=0)

    def setupFirstRowButtons(self):
        self.firstFrame = tkinter.ttk.Frame(
            self.root,
            height=self.root.winfo_height() * 0.169,
            width=self.root.winfo_width(),
        )

        self.clearButton = KButton(
            self.firstFrame,
            text="AC",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.utilityButtonColor,
            onHoverBackground=self.utilityButtonAccentColor,
            onClick=self.service.clear,
            column=0,
            row=0
        )
        self.backspaceButton = KButton(
            self.firstFrame,
            text="⌫",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.utilityButtonColor,
            onHoverBackground=self.utilityButtonAccentColor,
            onClick=self.service.backspace,
            column=1,
            row=0
        )
        self.percentageButton = KButton(
            self.firstFrame,
            text="%",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.utilityButtonColor,
            onHoverBackground=self.utilityButtonAccentColor,
            onClick=self.service.percentage,
            column=2,
            row=0
        )
        self.divisionButton = KButton(
            self.firstFrame,
            text="÷",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.operationButtonColor,
            onHoverBackground=self.operationButtonAccentColor,
            column=3,
            row=0
        )
        self.divisionButton.onClick = lambda : self.service.setOperator(
            "DIVISION",
            self.divisionButton,
            self.operationButtonClickedColor,
        )

        self.firstFrame.grid(column=0, row=1)

    def setupSecondRowButtons(self):
        self.secondFrame = tkinter.ttk.Frame(
            self.root,
            height=self.buttonHeight,
            width=self.root.winfo_width(),
        )

        self.sevenButton = KButton(
            self.secondFrame,
            text="7",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=0,
            row=0
        )
        self.eightButton = KButton(
            self.secondFrame,
            text="8",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=1,
            row=0
        )
        self.nineButton = KButton(
            self.secondFrame,
            text="9",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=2,
            row=0
        )
        self.multiplicationButton = KButton(
            self.secondFrame,
            text="×",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.operationButtonColor,
            onHoverBackground=self.operationButtonAccentColor,
            column=3,
            row=0
        )
        self.multiplicationButton.onClick = lambda : self.service.setOperator(
            "MULTIPLICATION",
            self.multiplicationButton,
            self.operationButtonClickedColor
        )

        self.secondFrame.grid(column=0, row=2)


    def setupThirdRowButtons(self):
        self.thirdFrame = tkinter.ttk.Frame(
            self.root,
            height=self.buttonHeight,
            width=self.root.winfo_width(),
        )

        self.fourButton = KButton(
            self.thirdFrame,
            text="4",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=0,
            row=0
        )
        self.fiveButton = KButton(
            self.thirdFrame,
            text="5",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=1,
            row=0
        )
        self.sixButton = KButton(
            self.thirdFrame,
            text="6",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=2,
            row=0
        )
        self.subtractionButton = KButton(
            self.thirdFrame,
            text="-",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.operationButtonColor,
            onHoverBackground=self.operationButtonAccentColor,
            column=3,
            row=0
        )
        self.subtractionButton.onClick = lambda : self.service.setOperator(
            "SUBTRACTION",
            self.subtractionButton,
            self.operationButtonClickedColor
        )

        self.thirdFrame.grid(column=0, row=3)

    def setupFourthRowButtons(self):
        self.fourthFrame = tkinter.ttk.Frame(
            self.root,
            height=self.buttonHeight,
            width=self.root.winfo_width(),
        )

        self.oneButton = KButton(
            self.fourthFrame,
            text="1",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=0,
            row=0
        )
        self.twoButton = KButton(
            self.fourthFrame,
            text="2",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=1,
            row=0
        )
        self.threeButton= KButton(
            self.fourthFrame,
            text="3",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=2,
            row=0
        )
        self.additionButton = KButton(
            self.fourthFrame,
            text="+",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.operationButtonColor,
            onHoverBackground=self.operationButtonAccentColor,
            column=3,
            row=0
        )
        self.additionButton.onClick = lambda : self.service.setOperator(
            "ADDITION",
            self.additionButton,
            self.operationButtonClickedColor
        )

        self.fourthFrame.grid(column=0, row=4)


    def setupFifthRowButtons(self):
        self.fifthFrame = tkinter.ttk.Frame(
            self.root,
            height=self.buttonHeight,
            width=self.root.winfo_width(),
        )

        self.zeroButton = KButton(
            self.fifthFrame,
            text="0",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=0,
            row=0,
        )
        self.positiveNegativeButton = KButton(
            self.fifthFrame,
            text="+/-",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick=self.service.positiveNegative,
            column=1,
            row=0
        )
        self.decimalButton = KButton(
            self.fifthFrame,
            text=".",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick=self.service.decimal,
            column=2,
            row=0
        )
        self.equalButton = KButton(
            self.fifthFrame,
            text="=",
            height=self.buttonHeight,
            width=self.buttonWidth,
            background=self.equalButtonColor,
            onHoverBackground=self.equalButtonAccentColor,
            onClick=self.service.evaluate,
            column=3,
            row=0
        )

        self.fifthFrame.grid(column=0, row=5)



if __name__ == '__main__':
    CalculatorGUI(CalculatorService())
