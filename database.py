from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty
import sqlite3

Builder.load_file('dbForm.kv')
Window.size = (500, 300)


class MyLayout(Widget):
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    email = ObjectProperty(None)

    def submit(self):
        first_name = self.first_name.text
        last_name = self.last_name.text
        email = self.email.text

        # create a connection
        conn = sqlite3.connect('form.db')
        # create a cursor
        c = conn.cursor()
        # create a record
        sql = ("""INSERT INTO clients(first_name, last_name, email) VALUES(?,?,?)""")
        myData = (first_name, last_name, email)
        c.execute(sql, myData)

        # commit changes
        conn.commit()

        # close db
        conn.close()

        self.first_name.text = ""
        self.last_name.text = ""
        self.email.text = ""


class DbFormApp(App):
    # create a connection to a db
    conn = sqlite3.connect('form.db')

    # create a cursor
    c = conn.cursor()

    # create a table
    c.execute(
        """ CREATE TABLE if not exists clients(first_name text, last_name text,email text)""")

    # commit changes
    conn.commit()
    # close db
    conn.close()

    def build(self):
        return MyLayout()


if __name__ == "__main__":
    DbFormApp().run()

