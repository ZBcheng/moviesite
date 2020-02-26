# moviesite电影网站后台
### 使用方法：
#### clone项目
##### 1. git clone https://github.com/zbcheng/moviesite.git
##### 2. cd moviesite
##### 3. git clone https://github.com/high-quality-sausages/db_super_airdrop.git
#### 本地启动：
```
pip3 install -r requirements.txt
```
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
```
python3 manage.py runserver
```
#### docker：
```
docker-compose bulid
```
```
docker-compose run web python3 manage.py makemigrations
```
```
docker-compose run web python3 manage.py migrate
```
```
docker-compose up
```