# cài đặt packages version như sau
!pip install opendatasets
!pip install mysql-connector-python
!pip install pandas matplotlib
!apt-get update install mysql-server mysql-client -y
!service mysql start

# cài đặt môi trường mysql với thông số :
# host : localhost
# user : root
# pass : 12345678
# database : laptop
!mysql -u root -p -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '12345678';"
!mysql -u root -p -e "CREATE DATABASE laptop;"
!mysql -u root -p -e "SHOW DATABASES;"
!mysql -u root -p -e "GRANT ALL PRIVILEGES ON laptop.* TO 'root'@'localhost';"

1. Trực quan hóa dữ liệu ta dùng main.py
2. CRUD gía trị ta dùng index.py