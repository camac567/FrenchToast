#INSERT INTO User
#	(username, password, email)
#Values
#	('camac567', 'pass', 'camac567@gmail.com');
	
	
#INSERT INTO User
#	(username, password, email)
#Values
#	('hill1303', 'pass', 'hill1303@gmail.com');
	
	
#INSERT INTO User
#	(username, password, email)
#Values
#	('chirmas', 'pass', 'chirmas@gmail.com');
	

#INSERT INTO User
#	(username, password, email)
#Values
#	('ThatKid', 'pass', 'coyancm@gmail.com');
	
def add_dummy_data(request):	
	return HttpResponse("Creating official users")
	p = Posting(username='camac567', password='pass', email='camac567@gmail.com')
	p.save
	
	p = Posting(username='hill1303', password='pass', email='hill1303@gmail.com')
	p.save
	
	p = Posting(username='chirmas', password='pass', email='chirmas@gmail.com')
	p.save
	
	p = Posting(username='ThatKid', password='pass', email='coyancm@gmail.com')
	p.save
	return HttpResponse("User creation successful")