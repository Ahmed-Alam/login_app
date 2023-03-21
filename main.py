from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
import json

# Window.size = (340, 600)

user = {
    'user_name':'Ahmed Alam',
    'email':'ahmed',
    'password':'123456'
}

users = json.dumps(user)

class SM(MDScreenManager):
    pass

class Login(MDScreen):
    def log_in(self):
        try:
            if self.ids.usr_email.text == user['email'] and self.ids.usr_password.text == user['password'] and user['email'] != '':
                self.parent.get_screen('profile').ids.profile_usr.text = f'User Name: \n{user["user_name"]}'
                self.parent.get_screen('profile').ids.profile_email.text = f'Email: \n{user["email"].split()[0]}'
                self.parent.get_screen('profile').ids.profile_password.text = f'Password: \n{user["password"]}'
                self.parent.current = 'profile'

                # Snackbar(text=f'Welcome {user["user_name"]}',pos_hint= {'center_x': 0.5,'y': 0},duration= 1).open()
                
        except:
            # Snackbar(text='Enter your email and password').open()
            return False

class SignUp(MDScreen):
    def sign_up(self):
        # print(self.ids.name.text)
        try:
            user['user_name'] = self.ids.name.text
            user['email'] = self.ids.email.text
            if self.ids.password.text == self.ids.password_confirm.text:
                user['password'] = self.ids.password.text
                self.manager.current = 'log in'
                self.manager.transition.direction = 'left'
            else:
                return True
                # Snackbar(text='Password doesn\'t match').open()
        except:
            if self.ids.name.text == '' or self.ids.email.text == '':
                # Snackbar(text='Please enter user name/email')
                return False

class Profile(MDScreen):
    pass

class MainApp(MDApp):
    def build(self):
        return Builder.load_file('main.kv')
    

MainApp().run()
