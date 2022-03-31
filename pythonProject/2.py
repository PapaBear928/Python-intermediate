import smtplib
import functools
def SendMail(user,password,mailFrom,mailTo,mailSubject,mailBody):
	message =
	'''From:zdobekzdobylski@gmail.com Subject:{}{}'''.format(mailFrom,mailSubject,mailBody)



	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(user,password)
		server.sendmail(user,mailTo,message)
		server.close()
		print('mail sent')
		return True
	except:
		print('something is no yes')
		return False


mailFrom = "Mail wysłany z Pythona"
mailTo = ['karolft86@gmail.com, karol.pilka@alumni.uj.edu.pl']
mailSubject =['Temat naszego maila']
mailBody = ''' Treść naszego maila Se jest tutaj No elo Mołdo.Wysłałem to przez Python '''
user = 'karolft86@gmail.com'
password = 'fru'

SendMail(user,password,mailFrom,mailTo,mailSubject,mailBody)