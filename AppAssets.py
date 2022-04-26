AppPagesAssets = """
ScreenManager:
	MainPage:
	RegisterPage:
		id: registration_scr
	LogInPage:
	ViewPage:

<MainPage>:
	name: 'TeamX'

	MDLabel:
		text: "Welcome to TeamX!"
		font_size: 30
		halign: 'center'
		pos_hint: {"center_x": .5, "center_y": 0.9}

	MDTextField:
		hint_text: "Enter Your Registered Coach ID Here"
		pos_hint: {'center_x':0.5, 'center_y':0.5}
		size_hint_x: None
		width: 300

	MDRectangleFlatButton:
		text: "LOG IN"
		pos_hint: {'center_x':0.5, 'center_y':0.4}
		on_press: root.manager.current = 'LogIn'

	MDLabel:
		text: "Not Registered?"
		halign: 'center'
		#theme_text_color: 'Hint'
		theme_text_color: 'Custom'
		text_color: (128,128,128)
		font_style: 'Caption'
		pos_hint: {"center_x": .5, "center_y": 0.15}

	MDRectangleFlatButton:
		text: "Register Now!"
		pos_hint: {'center_x':0.5, 'center_y':0.1}
		on_press: root.manager.current = 'Registering...'

	MDRectangleFlatButton:
		text: "View"
		pos_hint: {'center_x':0.5, 'center_y':0.8}
		on_press: root.manager.current = 'Viewing'



<RegisterPage>:
	name: 'Registering...'
	MDLabel:
		text: 'Coach ID: '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.6, 'center_y' : 0.6}	
	
	MDLabel:
		text: 'Your Name: '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.6, 'center_y' : 0.9}

	MDLabel:
		text: 'Team ID: '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.6, 'center_y' : 0.7}

	MDTextField:
		id: coachIDTextField
		pos_hint: {'center_x':0.62, 'center_y':0.6}
		font_size: 24
		size_hint_x: None
		width: 250

	MDTextField:
		id: nameTextField
		pos_hint: {'center_x':0.68, 'center_y':0.9}
		font_size: 24
		size_hint_x: None
		width: 250


	MDTextField:
		id: teamIDTextField
		pos_hint: {'center_x':0.62, 'center_y':0.7}
		font_size: 24
		size_hint_x: None
		width: 250



	MDRectangleFlatButton:
		text: "Submit"
		pos_hint: {'center_x':0.5, 'center_y':0.5}
		on_press: app.submit()

	MDRectangleFlatButton:
		text: "Confirm"
		pos_hint: {'center_x':0.5, 'center_y':0.4}
		on_press: app.showRecords()

	MDLabel:
		id: viewINFO_label
		text: '  '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.9, 'center_y' : 0.3}
		

	MDRectangleFlatButton:
		text: "Back"
		pos_hint: {'center_x':0.5, 'center_y':0.1}
		on_press: root.manager.current = 'TeamX'

<LogInPage>:
	name: 'LogIn'

	MDRectangleFlatButton:
		text: "Coach"
		pos_hint: {'center_x':0.5, 'center_y':0.8}
		on_press: root.manager.current = 'TeamX'

	MDRectangleFlatButton:
		text: "Players"
		pos_hint: {'center_x':0.5, 'center_y':0.6}
		on_press: root.manager.current = 'TeamX'

	MDRectangleFlatButton:
		text: "Team"
		pos_hint: {'center_x':0.5, 'center_y':0.4}
		on_press: root.manager.current = 'TeamX'

	MDRectangleFlatButton:
		text: "Back"
		pos_hint: {'center_x':0.5, 'center_y':0.1}
		on_press: root.manager.current = 'TeamX'

<ViewPage>:
	name: 'Viewing'

	MDRectangleFlatButton:
		text: "Back"
		pos_hint: {'center_x':0.5, 'center_y':0.1}
		on_press: root.manager.current = 'TeamX'


"""


'''
coachNameTextField = """
MDTextField:
	hint_text: "Enter Your Registered Name Here"
	pos_hint: {'center_x':0.5, 'center_y':0.5}
	size_hint_x: None
	width: 300
"""

teamXNameLabel = """
MDLabel:
	text: "Welcome to TeamX!"
	halign: 'center'
	pos_hint: {"center_x": .5, "center_y": 0.9}
"""

notRegisteredHintLabel = """
MDLabel:
	text: "Not Registered?"
	halign: 'center'
	#theme_text_color: 'Hint'
	theme_text_color: 'Custom'
	text_color: (128,128,128)
	font_style: 'Caption'
	pos_hint: {"center_x": .5, "center_y": 0.18}
"""
'''


