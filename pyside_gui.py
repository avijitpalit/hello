from PySide2.QtWidgets import QApplication, QDialog, QFormLayout, QLineEdit, QPushButton, QVBoxLayout

class InputDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Form")
        self.setGeometry(100, 100, 300, 150)

        # Create form layout
        layout = QFormLayout()

        # Create input fields
        self.first_input = QLineEdit()
        self.second_input = QLineEdit()

        # Add widgets to layout
        layout.addRow("First Input:", self.first_input)
        layout.addRow("Second Input:", self.second_input)

        # Create and add buttons
        button_layout = QVBoxLayout()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.accept)
        button_layout.addWidget(self.submit_button)

        layout.addRow(button_layout)

        self.setLayout(layout)

    def get_inputs(self):
        return self.first_input.text(), self.second_input.text()

def main():
    app = QApplication([])

    dialog = InputDialog()
    if dialog.exec_() == QDialog.Accepted:
        first_input, second_input = dialog.get_inputs()
        print(f"First Input: {first_input}")
        print(f"Second Input: {second_input}")

if __name__ == "__main__":
    main()
