all :
	cd /home/pi/web/SmartHome && sudo git pull
	cd /home/pi/web/SmartHome && sudo python3 manage.py makemigrations
	cd /home/pi/web/SmartHome && sudo python3 manage.py migrate
	cd /home/pi/web/SmartHome && sudo python3 manage.py runserver 0.0.0.0:8000 &
	cd /home/pi/web/SmartHome && sudo redis-server & 
	sleep 1 
	cd /home/pi/web/SmartHome && sudo /home/pi/.local/bin/celery -A SmartHome worker -l info & 
	cd /home/pi/web/SmartHome && sudo /home/pi/.local/bin/celery -A SmartHome beat -l info &
	
