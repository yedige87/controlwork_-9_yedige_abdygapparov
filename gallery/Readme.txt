
1. Скачать проект из GitHub

2. Создать в PgAdmin базу данных

3. В settings.py в разделе DATABASES в пункте NAME указать имя созданной БД

4. Установить имеющиеся зависимости командой: 
	
	pip install -r requirements.txt

5. Сделать миграцию командами:

	python3 manage.py makemigrations
	python3 manage.py migrate	

6. Загрузить из фикстур данные в БД командами:

	python3 manage.py loaddata fixtures/auth.json
	python3 manage.py loaddata fixtures/photo.json

7. Запустить проект командой: 

	python3 manage.py runserver

8. Войти в систему под любым из имен пользователей:

	логины: admin; hazbik; abdurozik; stalik
	password: root (у всех пользователей)



