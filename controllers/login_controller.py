from controllers.main_controller import *
from model.login import LoginController

class Login():
    
    def __init__(self,app,login,main):
        self.login_controller = LoginController(login,main,app)
        login.log_in.clicked.connect(self.login_controller.gui_login)
        login.log_in_1.clicked.connect(lambda: self.login_controller.show_page_2(list()))
        login.show()
        app.exec()