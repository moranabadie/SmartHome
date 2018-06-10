all :
	sudo cd /home/pi/web/SmartHome && sudo git pull
	sudo cd /home/pi/web/SmartHome && sudo python3 manage.py makemigrations
	sudo cd /home/pi/web/SmartHome && sudo python3 manage.py migrate
	sudo cd /home/pi/web/SmartHome && sudo python3 manage.py runserver 0.0.0.0:8000 &
	sudo cd /home/pi/web/SmartHome && sudo redis-server & 
	sleep 1 
	sudo cd /home/pi/web/SmartHome && sudo /home/pi/.local/bin/celery -A SmartHome worker -l info & 
	sudo cd /home/pi/web/SmartHome && sudo /home/pi/.local/bin/celery -A SmartHome beat -l info &
	
