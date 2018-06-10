all :
	cd /home/pi/web/SmartHome && git pull --no-edit
	cd /home/pi/web/SmartHome && python3 manage.py makemigrations
	cd /home/pi/web/SmartHome && python3 manage.py migrate
	cd /home/pi/web/SmartHome && python3 manage.py runserver 0.0.0.0:8000 &
	cd /home/pi/web/SmartHome && redis-server & 
	sleep 1 
	cd /home/pi/web/SmartHome && /home/pi/.local/bin/celery -A SmartHome worker -l info & 
	cd /home/pi/web/SmartHome && /home/pi/.local/bin/celery -A SmartHome beat -l info &
	
