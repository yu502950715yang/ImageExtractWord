import imghdr
import os

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QDialog, QPushButton, QTableWidgetItem, QAbstractItemView, QFileDialog, \
    QMessageBox
from aip import AipOcr

import ui_imageExtractWord


class ImageExtractWord(QDialog, ui_imageExtractWord.Ui_ImageToWord):
    def __init__(self):
        super(ImageExtractWord, self).__init__()

        self.setupUi(self)
        # 允许拖拽
        self.setAcceptDrops(True)
        # 设置表格数据为只读
        self.tableWidget_image.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_image.setColumnWidth(0, 100)
        self.tableWidget_image.setColumnWidth(1, 256)
        self.tableWidget_image.setColumnWidth(2, 50)

        # 按钮图标
        self.setWindowIcon(QIcon("resource/icon/格式转换.png"))
        self.pushButton_choosePath.setIcon(QIcon("resource/icon/打开_操作.png"))
        self.pushButton_imageExtract.setIcon(QIcon("resource/icon/转换_操作.png"))
        self.pushButton_cleanTable.setIcon(QIcon("resource/icon/关闭_操作.png"))

        # 按钮绑定事件
        self.pushButton_cleanTable.clicked.connect(self.clean_table)
        self.pushButton_choosePath.clicked.connect(self.choose_path)
        self.pushButton_imageExtract.clicked.connect(self.image_extract)

        # 记录文件路径
        self.paths = set()

    # 鼠标拖入事件
    def dragEnterEvent(self, event):
        for file in event.mimeData().urls():
            # ==> 获取文件路径
            file_path = file.toLocalFile()
            # ==> 去重显示
            if file_path not in self.paths:
                file_type = imghdr.what(file_path)
                # 判断文件是否为图片
                if file_type == "png" or file_type == "jpeg":
                    self.paths.add(file_path)
                    file_name = os.path.basename(file_path)
                    file_info = [file_name, file_path]
                    self.add_table_item(file_info)
        # 鼠标放开函数事件
        event.accept()

    def add_table_item(self, file):
        # 重新设置行数
        row_count = self.tableWidget_image.rowCount()
        self.tableWidget_image.setRowCount(row_count + 1)
        # 实例化操作按钮
        del_button = QPushButton()

        del_button.setIcon(QIcon("resource/icon/关闭_操作.png"))
        del_button.clicked.connect(self.del_button_click)
        for i in range(3):
            if i == 2:
                self.tableWidget_image.setCellWidget(row_count, i, del_button)
            else:
                self.tableWidget_image.setItem(row_count, i, QTableWidgetItem(file[i]))

    def del_button_click(self):
        row_count = self.tableWidget_image.currentRow()
        file_path = self.tableWidget_image.item(row_count, 1).text()
        self.paths.remove(file_path)
        self.tableWidget_image.removeRow(row_count)

    def clean_table(self):
        self.tableWidget_image.clearContents()
        self.tableWidget_image.setRowCount(0)
        self.paths.clear()

    def choose_path(self):
        out_path = QFileDialog.getExistingDirectory(self, "生成目录")
        self.lineEdit_outPath.setText(out_path)

    def image_extract(self):
        out_path = self.lineEdit_outPath.text()
        if len(out_path) == 0:
            QMessageBox.warning(self, "错误", "请选择生成的目录！")
            return
        extract_type = self.comboBox_imageType.currentText()
        if extract_type == "办公文档图片":
            create_file_num = 0
            for file_path in self.paths:
                create_file_num += 1
                file_name = os.path.basename(file_path)
                transition_office(file_path, out_path + "/" + file_name)
                if create_file_num == len(self.paths):
                    QMessageBox.information(self, "信息", "图片转换完毕")
                    return
        elif extract_type == "手写文字图片":
            create_file_num = 0
            for file_path in self.paths:
                create_file_num += 1
                file_name = os.path.basename(file_path)
                transition_hand(file_path, out_path + "/" + file_name)
                if create_file_num == len(self.paths):
                    QMessageBox.information(self, "信息", "图片转换完毕")
                    return


# 配置百度API连接信息：AppId、API key、Secret Key
config = {
    "appId": "",
    "apiKey": "",
    "secretKey": ""
}
# 创建AipOcr对象 调用识别方法
client = AipOcr(**config)


def get_image(path):
    """
    读取图片
    :param path: 图片路径
    :return: 图片
    """
    with open(path, 'rb') as f:
        return f.read()


def transition_office(file_path, out_path):
    """
    办公软件图片转换
    输出图片同路径docx文件
    :return: None
    """
    img_str = None
    img = get_image(file_path)
    result = client.doc_analysis_office(img)
    if "results" in result:
        img_str = '\n'.join(word['words']['word'] for word in result['results'])

    doc_path = out_path + ".docx"
    f = open(doc_path, "w", encoding="UTF-8")
    if img_str is not None:
        f.write(img_str)
    f.close()


def transition_hand(file_path, out_path):
    """
    手写图片转换
    输出图片同路径docx文件
    :return: None
    """
    img_str = None
    img = get_image(file_path)
    result = client.handwriting(img)
    if "words_result" in result:
        img_str = '\n'.join(word['words'] for word in result['words_result'])

    doc_path = out_path + ".docx"
    f = open(doc_path, "w", encoding="UTF-8")
    if img_str is not None:
        f.write(img_str)
    f.close()


def main():
    app = QApplication([])
    image_extract_word = ImageExtractWord()
    image_extract_word.show()
    app.exec_()


if __name__ == "__main__":
    main()
