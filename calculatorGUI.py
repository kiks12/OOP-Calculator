
import tkinter
from widgets.KButton import KButton

class CalculatorGUI():

    def __init__(self):
        self.normalButtonColor = "#e8e8e8"
        self.normalButtonAccentColor = "#d6d6d6"
        self.operationButtonColor = "#00d498"
        self.operationButtonAccentColor = "#00c48d"
        self.equalButtonColor = "#02ad7d"
        self.equalButtonAccentColor = "#01946a"

        self.setupWindow()
        self.root.update()

        self.calculatorText = tkinter.StringVar()
        self.calculatorText.set('0')
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
        self.entryFrame = tkinter.ttk.Frame(
            self.root,
            height=self.root.winfo_height() * 0.169,
            width=self.root.winfo_width(),
        )
        self.calculatorInput = tkinter.Entry(
            self.entryFrame,
            textvariable=self.calculatorText,
            justify=tkinter.RIGHT,
            bd=-2,
            state=tkinter.DISABLED,
            font=("Arial", 40),
            relief=tkinter.FLAT,
            insertborderwidth=0,
            selectborderwidth=0,
            borderwidth=0,
        )
        self.calculatorInput.place(
            height=self.entryFrame['height'],
            width=self.entryFrame['width']
        )
        self.entryFrame.grid(column=0, row=0)

    def setupFirstRowButtons(self):
        self.firstFrame = tkinter.ttk.Frame(
            self.root,
            height=self.root.winfo_height() * 0.169,
            width=self.root.winfo_width(),
        )

        self.clearButton = KButton(
            self.firstFrame,
            text="AC",
            height=self.firstFrame['height'],
            width=self.firstFrame['width'] * 0.25,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=0,
            row=2
        )
        self.positiveNegativeButton = KButton(
            self.firstFrame,
            text="+/-",
            height=self.firstFrame['height'],
            width=self.firstFrame['width'] * 0.25,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=1,
            row=2
        )
        self.percentageButton = KButton(
            self.firstFrame,
            text="%",
            height=self.firstFrame['height'],
            width=self.firstFrame['width'] * 0.25,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=2,
            row=2
        )
        self.divisionButton = KButton(
            self.firstFrame,
            text="/",
            height=self.firstFrame['height'],
            width=self.firstFrame['width'] * 0.25,
            background=self.operationButtonColor,
            onHoverBackground=self.operationButtonAccentColor,
            onClick="",
            column=3,
            row=2
        )

        self.firstFrame.grid(column=0, row=1)


    def setupSecondRowButtons(self):
        self.secondFrame = tkinter.ttk.Frame(
            self.root,
            height=self.root.winfo_height() * 0.169,
            width=self.root.winfo_width(),
        )

        self.sevenButton = KButton(
            self.secondFrame,
            text="7",
            height=self.secondFrame['height'],
            width=self.secondFrame['width'] * 0.25,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=0,
            row=3
        )
        self.eightButton = KButton(
            self.secondFrame,
            text="8",
            height=self.secondFrame['height'],
            width=self.secondFrame['width'] * 0.25,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=1,
            row=3
        )
        self.nineButton = KButton(
            self.secondFrame,
            text="9",
            height=self.secondFrame['height'],
            width=self.secondFrame['width'] * 0.25,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=2,
            row=3
        )
        self.multiplicationButton = KButton(
            self.secondFrame,
            text="*",
            height=self.secondFrame['height'],
            width=self.secondFrame['width'] * 0.25,
            background=self.operationButtonColor,
            onHoverBackground=self.operationButtonAccentColor,
            onClick="",
            column=3,
            row=3
        )

        self.secondFrame.grid(column=0, row=2)


    def setupThirdRowButtons(self):
        self.thirdFrame = tkinter.ttk.Frame(
            self.root,
            height=self.root.winfo_height() * 0.169,
            width=self.root.winfo_width(),
        )

        self.fourButton = KButton(
            self.thirdFrame,
            text="4",
            height=self.thirdFrame['height'],
            width=self.thirdFrame['width'] * 0.25,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=0,
            row=4
        )
        self.fiveButton = KButton(
            self.thirdFrame,
            text="5",
            height=self.thirdFrame['height'],
            width=self.thirdFrame['width'] * 0.25,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=1,
            row=4
        )
        self.sixButton = KButton(
            self.thirdFrame,
            text="6",
            height=self.thirdFrame['height'],
            width=self.thirdFrame['width'] * 0.25,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=2,
            row=4
        )
        self.subtractionButton = KButton(
            self.thirdFrame,
            text="-",
            height=self.thirdFrame['height'],
            width=self.thirdFrame['width'] * 0.25,
            background=self.operationButtonColor,
            onHoverBackground=self.operationButtonAccentColor,
            onClick="",
            column=3,
            row=4
        )

        self.thirdFrame.grid(column=0, row=3)

    def setupFourthRowButtons(self):
        self.fourthFrame = tkinter.ttk.Frame(
            self.root,
            height=self.root.winfo_height() * 0.169,
            width=self.root.winfo_width(),
        )

        self.oneButton = KButton(
            self.fourthFrame,
            text="1",
            height=self.fourthFrame['height'],
            width=self.fourthFrame['width'] * 0.25,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=0,
            row=5
        )
        self.twoButton = KButton(
            self.fourthFrame,
            text="2",
            height=self.fourthFrame['height'],
            width=self.fourthFrame['width'] * 0.25,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=1,
            row=5
        )
        self.threeButton= KButton(
            self.fourthFrame,
            text="3",
            height=self.fourthFrame['height'],
            width=self.fourthFrame['width'] * 0.25,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=2,
            row=5
        )
        self.additionButton = KButton(
            self.fourthFrame,
            text="+",
            height=self.fourthFrame['height'],
            width=self.fourthFrame['width'] * 0.25,
            background=self.operationButtonColor,
            onHoverBackground=self.operationButtonAccentColor,
            onClick="",
            column=3,
            row=5
        )

        self.fourthFrame.grid(column=0, row=4)


    def setupFifthRowButtons(self):
        self.fifthFrame = tkinter.ttk.Frame(
            self.root,
            height=self.root.winfo_height() * 0.169,
            width=self.root.winfo_width(),
        )

        self.zeroButton = KButton(
            self.fifthFrame,
            text="0",
            height=self.fifthFrame['height'],
            width=self.fifthFrame['width'] * 0.50,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=0,
            row=6,
            columnspan=2
        )
        self.decimalButton = KButton(
            self.fifthFrame,
            text=".",
            height=self.fifthFrame['height'],
            width=self.fifthFrame['width'] * 0.25,
            background=self.normalButtonColor,
            onHoverBackground=self.normalButtonAccentColor,
            onClick="",
            column=2,
            row=6
        )
        self.equalButton = KButton(
            self.fifthFrame,
            text="=",
            height=self.fifthFrame['height'],
            width=self.fifthFrame['width'] * 0.25,
            background=self.equalButtonColor,
            onHoverBackground=self.equalButtonAccentColor,
            onClick="",
            column=3,
            row=6
        )

        self.fifthFrame.grid(column=0, row=5)



if __name__ == '__main__':
    CalculatorGUI()
