Module : 
	
	
	
	main_with_random.py :
	
		description :
		
			TODO
			
		requirements : 
		
			TODO
			
		other info :
		
			this module is a work in progress
			
	
	
	main_cheap.py :
	
		description :
		
			gets student's id
			formats it into an email address (eXXXXXXX@cmaisonneuve.qc.ca)
			sends the code of the key box to said email address
			
			this module is where the code of the key box is stored
		
		requirements :
			
			- "PAD" module
			- "mail" module
			
			- "time" library
			
	
	
	PAD.py :
			
		description : 
			
			configures digital inputs riquired for the numpad
			
			this module contains the function that converts digital inputsto usable strings
			
		requirements :
		
			- "time" library
			- "RPi.GPIO" library
			
		other info :
		
			the "RPi.GPIO" crashes the program when ran on something else than a Rasp
			
			
			
	mail.py :
	
		description :
		
			this module contains the function that sends an email 
			
		requirements :
		
			- "smtplib" library
			- "MIMEMultipart" section from the "email.mime.multipart" library
			- "MIMEText" section from the "email.mime.text" library
			
			
			
if you have any question, comments or complaints, 
please send us an email at noreply.wedontcare@gmail.com



Enjoy

