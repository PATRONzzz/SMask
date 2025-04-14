# SMask
Smart task management system with analytics


sudo apt install postgresql postgresql-contrib -y 

sudo -u postgres psql 



CREATE DATABASE SMask;
# При успешном создании вернется CREATE DATABASE 

-- Создайте пользователя SMask_user и придумайте свой пароль, посложнее, чем в примере
CREATE USER SMask_user WITH ENCRYPTED PASSWORD 'xxxyyyzzz'; 
-- дайте пользователю SMask_user все права при работе с базой yatube 
GRANT ALL PRIVILEGES ON DATABASE SMask TO SMask_user;  



# ...директория_проекта/SMask/.env
# Укажите имя созданной базы данных
POSTGRES_DB=smask
# Укажите имя пользователя
POSTGRES_USER=smask_user
# Укажите пароль для пользователя
POSTGRES_PASSWORD=xxxyyyzzz
# Укажите localhost
DB_POSTGRES_SERVER=127.0.0.1
# Укажите порт для подключения к базе
POSTGRES_PORT=5432



