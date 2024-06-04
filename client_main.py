import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        """
        윈도우 창 생성, 크기 설정, 타이틀 설정
        """
        super().__init__()
        self.Login()
        # self.setWindowIcon(QIcon("AAA.png")) 아이콘 추가

    def Login(self):
        """
        로그인 함수(id, password, login_btn)
        """
        self.login_window = QDialog(self)
        self.login_window.setWindowTitle("로그인")
        self.login_window.setGeometry(400, 400, 300, 150)

        layout = QFormLayout()
        layout.setVerticalSpacing(20)

        LoginID = QLineEdit(self.login_window)
        LoginID.setPlaceholderText("사번 입력")
        LoginID.setFixedWidth(200)
        layout.addWidget(LoginID)

        LoginPW = QLineEdit(self.login_window)
        LoginPW.setPlaceholderText("비밀번호 입력")
        LoginPW.setFixedWidth(200)
        layout.addWidget(LoginPW)

        Loginbtn = QPushButton("로그인" ,self.login_window)
        Loginbtn.move(100, 100)
        Loginbtn.clicked.connect(self.check_login)

        self.login_window.setLayout(layout)
        self.login_window.exec_()

    def check_login(self):
        self.menu()
        # if True: # 아이디 패스워드 일치 검사 추가
        # else :
        #     # 아이디 혹은 pwd가 잘못되었습니다.
        #     self.loginfail_window = QDialog(self)
        #     self.loginfail_window.setGeometry(300,300,200,200)
        #     login_fail_cls_btn = QPushButton("X", self.loginfail_window)
        #     login_fail_cls_btn.move(200,200)

    def menu(self):
        """
        매뉴 창 생성(메뉴 쓰기 버튼, 메일 함 버튼, 휴지통 버튼)
        """
        self.menu_window = QDialog(self)
        self.menu_window.setWindowTitle("Mail_v0.0.0")
        self.menu_window.setGeometry(400, 400, 320, 300)

        layout = QVBoxLayout(self.menu_window)

        # 메일 쓰기
        write_btn = QPushButton("메일쓰기", self.menu_window)
        write_btn.move(10, 10)
        write_btn.clicked.connect(self.write_mail)

        # 메일 박스
        mailbox_btn = QPushButton("받은메일", self.menu_window)
        mailbox_btn.move(110, 10)
        mailbox_btn.clicked.connect(self.mailbox)

        # 휴지통
        trash_can_btn = QPushButton("휴지통", self.menu_window)
        trash_can_btn.move(210, 10)
        trash_can_btn.clicked.connect(self.trash_can)

        self.menu_window.setLayout(layout)
        self.menu_window.exec_()
        
    def write_mail(self):
        """
        메일 쓰기 창 생성 창 내부(받는 사람, 메일 제목, 첨부 파일, 메일 본문, 메일 전송)
        """
        self.write_window = QDialog(self)
        self.write_window.setWindowTitle("메일 쓰기")
        self.write_window.setGeometry(500, 500, 600, 400)

        layout = QVBoxLayout()

        receive_mail_address = QLineEdit(self.write_window)
        receive_mail_address.setPlaceholderText("받는 사람 이메일")
        layout.addWidget(receive_mail_address)

        subject = QLineEdit(self.write_window)
        subject.setPlaceholderText("메일 제목")
        layout.addWidget(subject)

        attach_file = QPushButton("첨부 파일", self.write_window)
        layout.addWidget(attach_file)

        mail_body = QTextEdit(self.write_window)
        mail_body.setPlaceholderText("메일 본문 작성")
        layout.addWidget(mail_body)

        send_btn = QPushButton("보내기", self.write_window)
        layout.addWidget(send_btn)

        self.write_window.setLayout(layout)
        self.write_window.exec_()

    def mailbox(self):
        """
        받은 메일 열람(db정보 불러오기(계정 이름 - 메시지 로그 불러오기))
        """
        
    def trash_can(self):
        """
        휴지통(삭제 후 30일까지 보관 후 폐기)
        """


# 기본 설정 코드
app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()
