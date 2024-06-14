import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QPushButton, QLabel, QLineEdit, QTextEdit, QDateTimeEdit, QMessageBox
from PyQt5.QtCore import Qt, QDateTime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DayTask")
        self.setGeometry(200, 200, 800, 600)


        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)


        self.task_list = QListWidget()
        main_layout.addWidget(self.task_list)

   
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout()
        buttons_widget.setLayout(buttons_layout)

        add_button = QPushButton("Adicionar Tarefa")
        add_button.clicked.connect(self.add_task)
        buttons_layout.addWidget(add_button)

        remove_button = QPushButton("Remover Tarefa")
        remove_button.clicked.connect(self.remove_task)
        buttons_layout.addWidget(remove_button)

        main_layout.addWidget(buttons_widget)


        form_widget = QWidget()
        form_layout = QVBoxLayout()
        form_widget.setLayout(form_layout)

        title_label = QLabel("Título:")
        self.title_edit = QLineEdit()
        form_layout.addWidget(title_label)
        form_layout.addWidget(self.title_edit)

        description_label = QLabel("Descrição:")
        self.description_edit = QTextEdit()
        form_layout.addWidget(description_label)
        form_layout.addWidget(self.description_edit)

        time_label = QLabel("Horário:")
        self.time_edit = QDateTimeEdit()
        self.time_edit.setDateTime(QDateTime.currentDateTime())
        form_layout.addWidget(time_label)
        form_layout.addWidget(self.time_edit)

        main_layout.addWidget(form_widget)

    def add_task(self):
        title = self.title_edit.text()
        description = self.description_edit.toPlainText()
        time = self.time_edit.dateTime().toPyDateTime()

      
        task_item = QListWidgetItem(f"{title} - {time}")
        task_item.setData(Qt.UserRole, time)  
        self.task_list.addItem(task_item)

        
        self.title_edit.clear()
        self.description_edit.clear()
        self.time_edit.setDateTime(QDateTime.currentDateTime())

    def remove_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            confirm = QMessageBox.question(self, 'Confirmar', 'Tem certeza que deseja excluir esta tarefa?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirm == QMessageBox.Yes:
                self.task_list.takeItem(self.task_list.row(selected_item))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())