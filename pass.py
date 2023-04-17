import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QTextEdit, QFileDialog


class PasswordGenerator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口大小和位置
        self.setGeometry(300, 300, 400, 300)

        # 创建各个GUI控件
        self.password_label = QLabel('Password: ', self)
        self.password_text = QLineEdit(self)

        self.platform_label = QLabel('Platform: ', self)
        self.platform_box = QComboBox(self)
        self.platform_box.addItem('WeChat')
        self.platform_box.addItem('QQ')
        self.platform_box.addItem('Baidu')
        self.platform_box.addItem('Alibaba')
        self.platform_box.addItem('FoFa')

        self.username_label = QLabel('Username/Email: ', self)
        self.username_box = QComboBox(self)
        self.username_box.addItem('52725351@qq.com')
        self.username_box.addItem('hackfreedom@qq.com')
        self.username_box.addItem('dyhackers@qq.com')
        self.username_box.addItem('fofabot@foxmail.com')
        self.username_box.addItem('djzhp@foxmail.com')

        self.generate_button = QPushButton('Generate Password', self)
        self.generate_button.clicked.connect(self.generatePassword)

        self.save_button = QPushButton('Save', self)
        self.save_button.clicked.connect(self.saveFile)

        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(self.quit)

        self.text_edit = QTextEdit(self)

        # 创建水平布局和垂直布局，并在其中添加控件
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.password_label)
        hbox1.addWidget(self.password_text)
        hbox1.addWidget(self.platform_label)
        hbox1.addWidget(self.platform_box)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.username_label)
        hbox2.addWidget(self.username_box)
        hbox2.addWidget(self.save_button)
        hbox2.addWidget(self.quit_button)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.generate_button)
        vbox.addWidget(self.text_edit)

        # 设置主布局
        self.setLayout(vbox)

    def generatePassword(self):
        # 按照要求生成随机密码
        password = ""
        for i in range(16):
            password += chr(random.randint(33, 126))
        self.password_text.setText(password)

    def saveFile(self):
        # 将生成的密码和邮箱/用户名存储到txt文件中
        platform = self.platform_box.currentText()
        username = self.username_box.currentText()
        password = self.password_text.text()
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File')
        if filename != '':
            with open(filename, 'w') as f:
                f.write(f"Platform: {platform}\n")
                f.write(f"Username/Email: {username}\n")
                f.write(f"Password: {password}\n")
            self.text_edit.setText(f'Saved to file: {filename}')

    def quit(self):
        # 退出应用程序
        QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = PasswordGenerator()
    generator.show()
    sys.exit(app.exec_())
