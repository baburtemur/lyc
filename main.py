import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt, QDate, pyqtSignal, QRect
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QDialog, QInputDialog, QComboBox, \
    QDialogButtonBox, QVBoxLayout, QTableWidgetItem, QCalendarWidget
from PyQt6.QtGui import *
import requests

ll = [37.677751, 55.757718]
spn = [0.016457, 0.00619]
z = 12
size = [400, 400]
scale = 5
l = "map"
result = requests.get(f"https://static-maps.yandex.ru/1.x/"
                      f"?ll={ll[0]},{ll[1]}"
                      f"&spn={spn[0]},{spn[1]}"
                      f"&z={z}"
                      f"&size={size[0]},{size[1]}"
                      f"&scale={scale}"
                      f"&l={l}"
                      )
print(result.url)

if not result:
    print("Ошибка выполнения запроса:")
    print("Http статус:", result.status_code, "(", result.reason, ")")
    sys.exit(1)

class Map(QMainWindow):
    def __init__(self, pic):
        super().__init__()
        self.setGeometry(400, 400, 400, 400)
        self.place = QPixmap("map.png")
        self.image = QLabel(self)
        self.image.resize(400, 400)
        self.image.move(0, 0)
        self.image.setPixmap(self.place)


    #def keyPressEvent(self):


map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(result.content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map("map.png")
    ex.show()
    sys.exit(app.exec())
