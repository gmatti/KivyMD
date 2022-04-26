from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd. uix.button import MDRectangleFlatButton
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.image import Image
#from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from kivy.lang import Builder

from AppAssets import AppPagesAssets

#from AppAssets import coachNameTextField
#from AppAssets import teamXNameLabel
#from AppAssets import notRegisteredHintLabel

import psycopg2

class MainPage(Screen):
	pass

class RegisterPage(Screen):
	pass

class LogInPage(Screen):
	pass

class ViewPage(Screen):
	pass

smanager = ScreenManager()
smanager.add_widget(MainPage(name = 'TeamX'))
smanager.add_widget(RegisterPage(name = 'Registering...'))
smanager.add_widget(LogInPage(name = 'LogIn'))
smanager.add_widget(ViewPage(name = 'Viewing'))

class TeamXApp(MDApp):
	def build(self):
		Window.size = [500, 800]
		screen = Builder.load_string(AppPagesAssets)
		
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Blue"
		self.theme_cls.primary_hue = "A700"


		'''
		screen = Screen()
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Blue"
		self.theme_cls.primary_hue = "A700"

		#soccerImage = Image(source = "soccerball.gif")

		teamXLabel = Builder.load_string(teamXNameLabel)
		self.coachName = Builder.load_string(coachNameTextField)
		notRegisteredLabel = Builder.load_string(notRegisteredHintLabel)

		#registerButton = MDRectangleFlatButton(text = "Register Here!",
		#										pos_hint = {'center_x':0.5, 'center_y':0.1},
		#										on_release = self.show_data)

		
		screen.add_widget(teamXLabel)
		screen.add_widget(self.coachName)
		screen.add_widget(notRegisteredLabel)
		screen.add_widget(registerButton)
		#screen.add_widget(soccerImage)
		'''

		#define the database
		DB_HOST = "/tmp"
		DB_NAME = "moonica"
		DB_USER = "moonica"
		DB_PASS = "0010"
		DB_PORT = "8888"

		conn = psycopg2.connect(
			host = DB_HOST,
			database = DB_NAME,
			user = DB_USER,
			password = DB_PASS,
			port = DB_PORT,
			)

		
		#create a cursor
		c = conn.cursor()

		#create a table
		#c.execute("""CREATE TABLE if not exists register (
		#	name VARCHAR(50), 
		#	teamName VARCHAR(50), 
		#	teamID INTEGER, 
		#	coachID SERIAL PRIMARY KEY);""")

		#c.execute("""CREATE TABLE if not exists register 
		#	(name TEXT);""")

		conn.commit()
		conn.close()
			
		return screen
	
	def submit(self):
		#define the database
		DB_HOST = "/tmp"
		DB_NAME = "moonica"
		DB_USER = "moonica"
		DB_PASS = "0010"
		DB_PORT = "8888"

		#create a database or connect to one
		conn = psycopg2.connect(
			host = DB_HOST,
			database = DB_NAME,
			user = DB_USER,
			password = DB_PASS,
			port = DB_PORT,
			)

		#create a cursor
		c = conn.cursor()

		#add a record
		#sql_command = "INSERT INTO register (name,teamName,teamID,coachID) Values(%s)" 
		sql_command = "INSERT INTO COACH Values(%s, %s, %s)" 
		coachID = (self.root.ids.registration_scr.ids.coachIDTextField.text)
		name1 = (self.root.ids.registration_scr.ids.nameTextField.text,)
		teamID = (self.root.ids.registration_scr.ids.teamIDTextField.text)
		varrrs = [coachID, name1, teamID]


		#execute postsql command
		#c.execute(sql_command, name, teamName, teamID, coachID)
		c.execute(sql_command, varrrs)

		#viewINFO in the registertion page
		self.root.ids.registration_scr.ids.viewINFO_label.text = f'{self.root.ids.registration_scr.ids.nameTextField.text} Added'

		#clear the input box
		self.root.ids.registration_scr.ids.nameTextField.text = ''
		#self.root.ids.teamTextField.text = ''
		#self.root.ids.teamIDTextField.text = ''
		#Sself.root.ids.coachIDTextField.text = ''

		# Commit our changes
		conn.commit()

		# Close our connection
		conn.close()

	def showRecords(self):
		#define the database
		DB_HOST = "/tmp"
		DB_NAME = "moonica"
		DB_USER = "moonica"
		DB_PASS = "0010"
		DB_PORT = "8888"

		#create a database or connect to one
		conn = psycopg2.connect(
			host = DB_HOST,
			database = DB_NAME,
			user = DB_USER,
			password = DB_PASS,
			port = DB_PORT,
			)
		
		#create a cursor
		c = conn.cursor()

		# Grab records from database
		c.execute("SELECT * FROM COACH")
		records = c.fetchall()
		
		word = ''
		# Loop thru records
		for record in records:
			word = f'{word}\n{record[0]}'
			self.root.ids.registration_scr.ids.viewINFO_label.text = f'{word}'

		# Commit our changes
		conn.commit()

		# Close our connection
		conn.close()


if __name__ == '__main__':
	TeamXApp().run()
