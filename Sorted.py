from random import randint
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas)
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation


class MyMplCanvas(FigureCanvas):
    """Холст
    """
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(1, 1, 1)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)


class AnimationWidget(QtWidgets.QMainWindow):
    """Окно приложения
    """
    WIDHT = 600
    HEIGHT = 600
    ARR_LEN = 20
    MAX_ELEMENT = 200

    def __init__(self):
        super().__init__()
        self.resize(self.WIDHT, self.HEIGHT)
        self.setWindowTitle("Визуализация сортировки расчёской")
        self.__central_widget = QtWidgets.QWidget()

        self.__animation = None

        widget_height = 30

        # создание макетов для расположения элементов интерфейса
        hbox_info = QtWidgets.QHBoxLayout()
        hbox_input = QtWidgets.QHBoxLayout()
        hbox_control = QtWidgets.QHBoxLayout()
        vbox_canvas = QtWidgets.QVBoxLayout()

        # обалсть справки
        self.__help_button = QtWidgets.QPushButton("?", self)
        self.__help_button.setFixedSize(widget_height, widget_height)
        self.__help_button.pressed.connect(self.__help)

        # область для визуализации сорировки
        self.__canvas = MyMplCanvas(self, width=5, height=4, dpi=100)

        # область для инициализации и отображения массива
        self.__len_input = QtWidgets.QLineEdit()
        self.__len_input.setPlaceholderText("Длина массива")
        self.__len_input.setFixedSize(100, widget_height)

        self.__arr_output = QtWidgets.QLineEdit()
        self.__arr_output.setPlaceholderText("Массив")
        self.__arr_output.setFixedHeight(widget_height)
        self.__arr_output.setReadOnly(True)

        # область управления
        self.__start_button = QtWidgets.QPushButton("Старт", self)
        self.__start_button.setFixedHeight(widget_height)
        self.__start_button.clicked.connect(self.__on_start)

        # добавление элементов в соответствующие макеты
        hbox_info.setAlignment(QtCore.Qt.AlignRight)
        hbox_info.addWidget(self.__help_button)

        hbox_input.addWidget(self.__len_input)
        hbox_input.addWidget(self.__arr_output)

        vbox_canvas.addLayout(hbox_info)
        vbox_canvas.addWidget(self.__canvas)
        vbox_canvas.addLayout(hbox_input)
        vbox_canvas.addLayout(hbox_control)

        hbox_control.addWidget(self.__start_button)

        self.__central_widget.setLayout(vbox_canvas)
        self.setCentralWidget(self.__central_widget)

    def __help(self):
        """Отображение справки
        """
        msg = "Введите длину массива от 2 до 20 включительно в поле 'Длина массива'. После чего нажмите кнопку 'Старт'."
        QtWidgets.QMessageBox.information(self, "Информация", msg, QtWidgets.QMessageBox.Ok)

    def is_len_valid(self):
        """Провекра введенной длины массива
        """
        try:
            arr_len = int(self.__len_input.text())
            if arr_len < 2 or arr_len > self.ARR_LEN:
                msg = f"2 <= Длина массива <= {self.ARR_LEN}"
                QtWidgets.QMessageBox.warning(self, "Предупреждение", msg, QtWidgets.QMessageBox.Ok)
                return False

            self.N = arr_len
            return True
        except Exception as exp:
            msg = exp.__str__()
            QtWidgets.QMessageBox.warning(self, "Предупреждение", msg, QtWidgets.QMessageBox.Ok)
            return False

    def __sort(self, _):
        gap = self.N
        swaps = True
        while gap > 1 or swaps:
            gap = max(1, int(gap / 1.25))
            swaps = False
            for i in range(self.N - gap):
                j = i + gap
                if self.__y[i] > self.__y[j]:
                    self.__y[i], self.__y[j] = self.__y[j], self.__y[i]

                    # это нужно для отображения массива (в текстовом поле)
                    self.__arr_output.setText(str(self.__y))

                    # это нужно для визуализации сортировки
                    return self.__canvas.axes.bar(self.__x, self.__y, color="b")
                    swaps = True

        # это нужно для остоновки рисования
        self.__on_stop()
        return self.__canvas.axes.bar(self.__x, self.__y, color="b")

    def __on_start(self):
        """Запуска визуализации сортировки
        """
        if not self.__is_len_valid():
            return

        if self.__animation is not None:
            self.__on_stop()

        self.__x = [num for num in range(self.N)]
        self.__y = [randint(0, self.MAX_ELEMENT) for _ in range(self.N)]

        self.__arr_output.setText(str(self.__y))

        self.__animation = FuncAnimation(self.__canvas.figure, self.__sort, blit=True, interval=500)

    def __on_stop(self):
        """Прекращение сортировки
        """
        try:
            self.__animation.event_source.stop()
        except Exception as exp:
            msg = exp.__str__()
            QtWidgets.QMessageBox.warning(self, "Предупреждение", msg, QtWidgets.QMessageBox.Ok)