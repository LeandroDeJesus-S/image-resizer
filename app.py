from base import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.Qt import QPixmap
from pathlib import Path
from threading import Timer


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainLabel.setText('Nenhuma imagem selecionada...')
        self.mainLabel.setDisabled(False)
        self.originalImage = None
        self.resizedImage = None
        self.hasNotImage = True
        self.searchFileButton.clicked.connect(self.get_image)
        self.resizeButton.clicked.connect(self.resize_image)
        self.saveButton.clicked.connect(self.save_new_image)

    def get_image(self):
        default_opening = str(Path.home())
        title = 'Escolher imagem'
        file_types = 'All files (*)\n*.png\n*.jpeg\n*.jpg\n*.webp\n*.bmp'
        image_path, ext = QFileDialog.getOpenFileName(self.centralwidget, title,
                                                      default_opening, filter=file_types)
        self.show_image(image_path)
        self.hasNotImage = self.mainLabel.pixmap().isNull()
        if self.hasNotImage:
            return

        self.inputFilePath.setText(f'{image_path}')

    def show_image(self, path: str):
        self.originalImage = QPixmap(path)
        self.mainLabel.setPixmap(self.originalImage)
        w = self.originalImage.size().width()
        h = self.originalImage.size().height()
        self.inputWidth.setText(str(w))
        self.inputHeight.setText(str(h))

    def resize_image(self):
        if self.hasNotImage:
            self.warnings.setText('Nada para redimensionar')
            self.clear_warnings()
            return
        new_w = self.inputWidth.text()
        new_h = self.inputHeight.text()
        new_w = self.try_input(new_w, 'x')
        new_h = self.try_input(new_h, 'y')
        if not new_w or not new_h:
            return
        self.resizedImage = self.originalImage.scaled(new_w, new_h)
        self.mainLabel.setPixmap(self.resizedImage)

    def save_new_image(self):
        if self.hasNotImage:
            self.warnings.setText('Nada para salvar')
            self.clear_warnings()
            return
        name, ext = QFileDialog.getSaveFileName(self.centralWidget(), 'Salvar',
                                                self.inputFilePath.text(),
                                                filter='All files (*)\n*.png\n*.jpeg\n*.webp\n*.bmp')
        if self.resizedImage.save(name, quality=72):
            self.warnings.setText(f'Imagem salva em: {name}')
            self.warnings.setStyleSheet('color: green; font-size: 13px; background: #1ce6b7;')

    def try_input(self, content: str, camp_name: str):
        if not content:
            self.warnings.setText(f'Campo "{camp_name}" não pode ser vazio')
            self.clear_warnings()
            return 0
        try:
            converted = int(content)
            if converted < 1:
                self.warnings.setText(f'{camp_name} não pode ser {content}')
                return
            return converted
        except ValueError:
            self.warnings.setText(f'Dado inválido: "{content}"')
            self.clear_warnings()
            return 0

    def clear_warnings(self):
        t = Timer(1, self.warnings.setText, args=('',))
        t.start()


if __name__ == '__main__':
    qt = QApplication([])
    app = App()
    app.show()
    qt.exec_()
