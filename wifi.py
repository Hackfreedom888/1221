from tkinter import *

class WifiScanner:
    def __init__(self, master):
        self.master = master
        master.title("WiFi Scanner")

        # 创建GUI元素
        self.label = Label(master, text="请点击扫描按钮扫描WiFi并测试密码")
        self.label.pack()

        self.button = Button(master, text="扫描", command=self.scan_and_test)
        self.button.pack()

        self.text_box = Text(master)
        self.text_box.pack(fill=BOTH, expand=True)

    # 扫描WiFi并测试密码
    def scan_and_test(self):
        # 扫描WiFi的代码，自行定义...

        # 显示扫描结果
        self.text_box.delete("1.0", END) # 清空文本框
        for network in networks:
            self.text_box.insert(END, f"SSID: {network[0]}\n")
            self.text_box.insert(END, f"Signal level: {network[1]}\n")
            self.text_box.insert(END, f"Encryption: {network[2]}\n\n")
        self.label.config(text="扫描和测试已完成")

root = Tk()
wifi_scanner = WifiScanner(root)
root.mainloop()
