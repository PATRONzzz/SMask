# SMask
Smart task management system with analytics

CREATE DATABASE yatube;
# При успешном создании вернется CREATE DATABASE 

-- Создайте пользователя SMask_user и придумайте свой пароль, посложнее, чем в примере
CREATE USER SMask_user WITH ENCRYPTED PASSWORD 'xxxyyyzzz'; 
-- дайте пользователю SMask_user все права при работе с базой yatube 
GRANT ALL PRIVILEGES ON DATABASE SMask TO SMask_user;  



# ...директория_проекта/yatube/yatube/.env
# Укажите, что используете postgresql
DB_ENGINE=django.db.backends.postgresql
# Укажите имя созданной базы данных
DB_NAME=SMask
# Укажите имя пользователя
POSTGRES_USER=SMask_user
# Укажите пароль для пользователя
POSTGRES_PASSWORD=xxxyyyzzz
# Укажите localhost
DB_HOST=127.0.0.1
# Укажите порт для подключения к базе
DB_PORT=5432



no