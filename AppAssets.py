AppPagesAssets = """
ScreenManager:
	MainPage:
	RegisterPage:
		id: registration_scr
	LogInPage:
	AddPlayers:
	CoachPage:
	TeamPage:
	PlayerPage:

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



<RegisterPage>:
	name: 'Registering...'
	
	MDLabel:
		text: 'Coach Name: '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.6, 'center_y' : 0.9}
	MDLabel:
		text: 'Coach Team ID: '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.6, 'center_y' : 0.85}
	MDLabel:
		text: 'Coach ID: '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.6, 'center_y' : 0.8}
	MDLabel:
		text: 'Team ID: '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.6, 'center_y' : 0.75}
	MDLabel:
		text: 'Team Name: '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.6, 'center_y' : 0.7}
	MDLabel:
		text: 'Team Coach ID: '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.6, 'center_y' : 0.65}
	MDLabel:
		text: 'Win-Loss: '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.6, 'center_y' : 0.6}
	MDTextField:
		id: nameTextField
		pos_hint: {'center_x':0.65, 'center_y':0.9}
		font_size: 24
		size_hint_x: None
		width: 250
	MDTextField:
		id: coachTeamIDTextField
		pos_hint: {'center_x':0.65, 'center_y':0.85}
		font_size: 24
		size_hint_x: None
		width: 250
	MDTextField:
		id: coachIDTextField
		pos_hint: {'center_x':0.65, 'center_y':0.8}
		font_size: 24
		size_hint_x: None
		width: 250
	MDTextField:
		id: teamIDTextField
		pos_hint: {'center_x':0.65, 'center_y':0.75}
		font_size: 24
		size_hint_x: None
		width: 250
	MDTextField:
		id: teamNameTextField
		pos_hint: {'center_x':0.65, 'center_y':0.7}
		font_size: 24
		size_hint_x: None
		width: 250
	MDTextField:
		id: teamCoachIDTextField
		pos_hint: {'center_x':0.65, 'center_y':0.65}
		font_size: 24
		size_hint_x: None
		width: 250
	MDTextField:
		id: winLossTextField
		pos_hint: {'center_x':0.65, 'center_y':0.6}
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
		pos_hint: {'center_x':0.1, 'center_y':0.1}
		on_press: root.manager.current = 'TeamX'


<LogInPage>:
	name: 'LogIn'

	MDRectangleFlatButton:
		text: "Add Players"
		pos_hint: {'center_x':0.5, 'center_y':0.9}
		on_press: root.manager.current = 'Add_Players'

	MDRectangleFlatButton:
		text: "View Coach Info"
		pos_hint: {'center_x':0.5, 'center_y':0.7}
		on_press: root.manager.current = 'Coach'

	MDRectangleFlatButton:
		text: "View Players Info"
		pos_hint: {'center_x':0.5, 'center_y':0.5}
		on_press: root.manager.current = 'Player'

	MDRectangleFlatButton:
		text: "View Team Info"
		pos_hint: {'center_x':0.5, 'center_y':0.3}
		on_press: root.manager.current = 'Team'

	MDRectangleFlatButton:
		text: "Back"
		pos_hint: {'center_x':0.1, 'center_y':0.1}
		on_press: root.manager.current = 'TeamX'




<CoachPage>:
	name: 'Coach'

	MDLabel:
		id: coachID_label
		text: '  '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.9, 'center_y' : 0.9}

	MDLabel:
		id: coachName_label
		text: '  '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.9, 'center_y' : 0.8}

	MDLabel:
		id: coachTeamID_label
		text: '  '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.9, 'center_y' : 0.7}

	MDRectangleFlatButton:
		text: "Back"
		pos_hint: {'center_x':0.1, 'center_y':0.1}
		on_press: root.manager.current = 'LogIn'


<TeamPage>:
	name: 'Team'

	MDLabel:
		id: teamID_label
		text: '  '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.9, 'center_y' : 0.9}

	MDLabel:
		id: teamName_label
		text: '  '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.9, 'center_y' : 0.8}

	MDLabel:
		id: teamCoachID_label
		text: '  '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.9, 'center_y' : 0.7}

	MDLabel:
		id: winLoss_label
		text: '  '
		font_size: 24
		halign: 'left'
		pos_hint:{'center_x' : 0.9, 'center_y' : 0.6}

	MDRectangleFlatButton:
		text: "Back"
		pos_hint: {'center_x':0.1, 'center_y':0.1}
		on_press: root.manager.current = 'LogIn'

<PlayerPage>:
	name: 'Player'

	MDLabel:
		id: playerID_label
		text: ' '
		font_size: 24
		halign: 'center'
		pos_hint:{'center_x' : 0.5, 'center_y' : 0.9}
		

	MDLabel:
		id: playName_label
		text: ' '
		font_size: 24
		halign: 'center'
		pos_hint:{'center_x' : 0.5, 'center_y' : 0.8}

	MDLabel:
		id: playerTeamID_label
		text: ' '
		font_size: 24
		halign: 'center'
		pos_hint:{'center_x' : 0.5, 'center_y' : 0.7}

	MDLabel:
		id: playerBirthday_label
		text: ' '
		font_size: 24
		halign: 'center'
		pos_hint:{'center_x' : 0.5, 'center_y' : 0.6}
