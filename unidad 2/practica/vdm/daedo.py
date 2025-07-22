import sys
from PyQt6.QtWidgets import (
    QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QColor, QPalette

class TaekwondoScoreSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema Profesional de Puntuación - Taekwondo")
        self.showFullScreen()

        # Variables
        self.red_score = 0
        self.blue_score = 0
        self.round = 1
        self.red_gj = 0
        self.blue_gj = 0
        self.time_left = 60
        self.timer_running = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.init_ui()

    def init_ui(self):
        font_large = QFont("Arial", 100, QFont.Weight.Bold)
        font_medium = QFont("Arial", 40, QFont.Weight.Bold)
        font_small = QFont("Arial", 24, QFont.Weight.Medium)

        # Layouts principales
        main_layout = QVBoxLayout()
        score_layout = QHBoxLayout()
        control_layout = QHBoxLayout()
        button_layout = QGridLayout()

        # Marcadores
        self.lbl_red = QLabel("0")
        self.lbl_red.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_red.setFont(font_large)
        self.lbl_red.setStyleSheet("background-color: red; color: white; border-radius: 20px;")
        score_layout.addWidget(self.lbl_red)

        self.lbl_round = QLabel(f"RONDA {self.round}")
        self.lbl_round.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_round.setFont(font_medium)
        score_layout.addWidget(self.lbl_round)

        self.lbl_blue = QLabel("0")
        self.lbl_blue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_blue.setFont(font_large)
        self.lbl_blue.setStyleSheet("background-color: blue; color: white; border-radius: 20px;")
        score_layout.addWidget(self.lbl_blue)

        # Temporizador
        self.lbl_timer = QLabel("01:00")
        self.lbl_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_timer.setFont(font_large)
        main_layout.addLayout(score_layout)
        main_layout.addWidget(self.lbl_timer)

        # Gam-jeoms
        self.lbl_red_gj = QLabel("GJ: 0")
        self.lbl_red_gj.setFont(font_small)
        self.lbl_red_gj.setStyleSheet("color: red;")
        self.lbl_blue_gj = QLabel("GJ: 0")
        self.lbl_blue_gj.setFont(font_small)
        self.lbl_blue_gj.setStyleSheet("color: blue;")

        gj_layout = QHBoxLayout()
        gj_layout.addWidget(self.lbl_red_gj)
        gj_layout.addStretch()
        gj_layout.addWidget(self.lbl_blue_gj)
        main_layout.addLayout(gj_layout)

        # Botones de puntuación
        for i in range(1, 5):
            btn_red = QPushButton(f"Rojo +{i}")
            btn_red.setFont(font_small)
            btn_red.clicked.connect(lambda _, p=i: self.add_score("red", p))
            button_layout.addWidget(btn_red, 0, i-1)

            btn_blue = QPushButton(f"Azul +{i}")
            btn_blue.setFont(font_small)
            btn_blue.clicked.connect(lambda _, p=i: self.add_score("blue", p))
            button_layout.addWidget(btn_blue, 1, i-1)

        # Botones Gam-jeom
        btn_gj_red = QPushButton("Gam Rojo")
        btn_gj_red.setFont(font_small)
        btn_gj_red.clicked.connect(lambda: self.add_gamjeom("red"))
        button_layout.addWidget(btn_gj_red, 2, 0)

        btn_gj_blue = QPushButton("Gam Azul")
        btn_gj_blue.setFont(font_small)
        btn_gj_blue.clicked.connect(lambda: self.add_gamjeom("blue"))
        button_layout.addWidget(btn_gj_blue, 2, 1)

        # Botones de control
        btn_start = QPushButton("Iniciar")
        btn_start.setFont(font_small)
        btn_start.clicked.connect(self.start_timer)
        control_layout.addWidget(btn_start)

        btn_next = QPushButton("Siguiente Ronda")
        btn_next.setFont(font_small)
        btn_next.clicked.connect(self.next_round)
        control_layout.addWidget(btn_next)

        btn_reset = QPushButton("Reset")
        btn_reset.setFont(font_small)
        btn_reset.clicked.connect(self.reset)
        control_layout.addWidget(btn_reset)

        main_layout.addLayout(button_layout)
        main_layout.addLayout(control_layout)
        self.setLayout(main_layout)

    def add_score(self, color, points):
        if color == "red":
            self.red_score += points
            self.lbl_red.setText(str(self.red_score))
        else:
            self.blue_score += points
            self.lbl_blue.setText(str(self.blue_score))

    def add_gamjeom(self, color):
        if color == "red":
            self.red_gj += 1
            self.lbl_red_gj.setText(f"GJ: {self.red_gj}")
            self.add_score("blue", 1)
        else:
            self.blue_gj += 1
            self.lbl_blue_gj.setText(f"GJ: {self.blue_gj}")
            self.add_score("red", 1)

    def start_timer(self):
        if not self.timer_running:
            self.timer.start(1000)
            self.timer_running = True

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            mins = self.time_left // 60
            secs = self.time_left % 60
            self.lbl_timer.setText(f"{mins:02}:{secs:02}")
        else:
            self.timer.stop()
            self.timer_running = False
            self.lbl_timer.setText("00:00")

    def next_round(self):
        self.round += 1
        self.lbl_round.setText(f"RONDA {self.round}")
        self.time_left = 60
        self.lbl_timer.setText("01:00")
        self.timer_running = False

    def reset(self):
        self.red_score = 0
        self.blue_score = 0
        self.red_gj = 0
        self.blue_gj = 0
        self.round = 1
        self.time_left = 60
        self.timer.stop()
        self.timer_running = False
        self.lbl_red.setText("0")
        self.lbl_blue.setText("0")
        self.lbl_red_gj.setText("GJ: 0")
        self.lbl_blue_gj.setText("GJ: 0")
        self.lbl_round.setText("RONDA 1")
        self.lbl_timer.setText("01:00")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaekwondoScoreSystem()
    window.show()
    sys.exit(app.exec())
