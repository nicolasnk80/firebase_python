import pyrebase


class Account:
	def __init__(self):
		firebaseConfig = {
			"apiKey": "AIzaSyB6KPlQKWWfT5X6HAHSidp1VoaDuP4aZxs",
			"authDomain": "teste-ae6b7.firebaseapp.com",
			"projectId": "teste-ae6b7",
			"databaseURL": "https://teste-ae6b7.firebaseio.com",
			"storageBucket": "teste-ae6b7.appspot.com",
			"messagingSenderId": "657211805081",
			"appId": "1:657211805081:web:029f709003fa33a1665708",
			"measurementId": "G-660GMZK2R8"
		}

		firebase = pyrebase.initialize_app(firebaseConfig)
		self.auth = firebase.auth()
	
	def sing_in(self, email, password):	
		try:
			self.auth.sign_in_with_email_and_password(email, password)
			return True
		
		except:
			return False
	
	def sing_up(self, email, password):
		try:
			self.auth.create_user_with_email_and_password(email, password)
			return True
		
		except:
			return False
	
	def reset_password(self, email):
		try:
			self.auth.send_password_reset_email(email)
			return True
		
		except:
			return False

