from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window
from kivymd.uix.snackbar.snackbar import Snackbar
from kivy.uix.popup import Popup
import json

# Window.size = (340, 600)

user = {
    'user_name':'Ahmed Alam',
    'email':'ahmed',
    'password':'123456'
}

users = json.dumps(user)
Snackbar
class SM(MDScreenManager):
    pass

class Login(MDScreen):
    def log_in(self):
        try:
            if self.ids.usr_email.text == user['email'] and self.ids.usr_password.text == user['password'] and user['email'] != '':
                
                self.parent.current = 'profile'

                Popup(title=f'Welcome {user["user_name"]}',
                pos_hint={'center_x': 0.5,'center_y': 0.06},
                size_hint= (1, 0.1)).open()
            else:
                Popup(title='Enter your email and password',
                pos_hint={'center_x': 0.5,'center_y': 0.06},
                size_hint= (1, 0.1)).open()
        except:
            return False

class SignUp(MDScreen):
    def sign_up(self):
        # try:
        if self.ids.name.text == '' or self.ids.email.text == '' or self.ids.password.text == '':
            Popup(title='Please enter user name/email/password',
                pos_hint={'center_x': 0.5,'center_y': 0.06},
                size_hint= (1, 0.1)).open()
        else:
            user['user_name'] = self.ids.name.text
            user['email'] = self.ids.email.text
            if self.ids.password.text == self.ids.password_confirm.text:
                user['password'] = self.ids.password.text
                self.parent.current = 'log in'
            else:
                Popup(title='Passwords do not match',
                pos_hint={'center_x': 0.5,'center_y': 0.06},
                size_hint= (1, 0.1)).open()
            
class Profile(MDScreen):
    def on_size(self, *args, **kwargs):
        self.ids.profile_usr.text = f'[b]User Name[/b]: \n{user["user_name"]}'
        self.ids.profile_email.text = f'[b]Email[/b]: \n{user["email"].split()[0]}'
        self.ids.profile_password.text = f'[b]Password[/b]: \n{user["password"]}'

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('main.kv')

MainApp().run()
