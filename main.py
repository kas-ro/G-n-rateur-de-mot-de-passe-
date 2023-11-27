import random
import string

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast import toast
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen

class Generateur(MDBoxLayout):
    spacial_charaters = "!@#$%^&*_-,.;"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digit = "0123456789"
    size_carac = 0
    size_verified = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def generate_password(longueur, password):
        word_password = ""
        if longueur != 0:
            while int(longueur):
                word_password += random.choice(password)
                longueur -= 1
        return word_password

    @staticmethod
    def verified_length_password(password_len, password):
        if password_len != len(password):
            return toast("Verifier vos longueur !")
        else:
            return password

    @staticmethod
    def verified_number_characters(size_cara):
        if str(size_cara).isdigit():
            return size_cara
        else:
            size_cara = 0
            return size_cara

    @staticmethod
    def shuffle_password(password):
        password_new = ""
        elt = list(password)
        lenght_p = len(password)
        while lenght_p:
            new_password = random.choice(elt)
            password_new += new_password
            elt.remove(new_password)
            lenght_p -= 1
        return password_new

    def generate(self):
        password = ""
        if self.ids.length_password.text.isdigit():

            if self.ids.special_character_switch.active:
                self.size_carac = self.ids.number_special_character.text
                self.size_verified = int(self.verified_number_characters(self.size_carac))
                password += self.generate_password(self.size_verified, self.spacial_charaters)  

            if self.ids.uppercase_switch.active:
                self.size_carac = self.ids.number_character_uppercase.text
                self.size_verified = int(self.verified_number_characters(self.size_carac))
                password += self.generate_password(self.size_verified, self.uppercase)

            if self.ids.lowercase_switch.active:
                self.size_carac = self.ids.number_character_lowercase.text
                self.size_verified = int(self.verified_number_characters(self.size_carac))
                password += self.generate_password(self.size_verified, self.lowercase)

            if self.ids.digit_switch.active:
                self.size_carac = self.ids.number_character_digit.text
                self.size_verified = int(self.verified_number_characters(self.size_carac))
                password += self.generate_password(self.size_verified, self.digit)

            new_password = self.shuffle_password(password)
            p = self.verified_length_password(int(self.ids.length_password.text), new_password)
            self.ids.password_text.text = str(p)

        else:
            toast("La longueur du mot passe n'est pas definie !")


class MainApp(MDApp):
    def build(self):
        #     # self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        # return Builder.load_file("thelab.kv")


if __name__ == '__main__':
    MainApp().run()