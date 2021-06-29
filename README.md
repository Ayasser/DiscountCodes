# Discount Codes
Basic service for create discount codes.

## Installation/deployment instructions

### 1. Prerequisites

* python v3.9
* pip 21.1.1 
* Django v3.2.4
* Virtualenv v20.0.30
* Mysql v8.0.25

### 2. Clone project


```sh
git clone https://github.com/Ayasser/DiscountCodes.git
```
    
### 3. Create Virtualenv

```sh
virtualenv env
 ```

### 4. Activate Virtualenv

```sh
source env/bin/activate
```

### 5. Install required packages inside virtualenv

```sh
pip install -r requirements.txt
```

### 6. create database
```bash
$ mysql -u {user_name} -p {password}
$ CREATE DATABASE discount_codes_database;
```
add USER and PASSWORD in discount/settings.py
```json
    "default" : {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'discount_codes_database',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
        }
```
### 7. Run migrate
```bash
  python manage.py makemigrations
  python manage.py migrate 
```
### 8. Run local server

```bash
python3 manage.py runserver
```

## Requests:

#### create discount code
```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"start_date":"2006-10-25 14:30:50","expire_date":"2006-10-25 14:30:59","customer_id":"67460e74-02e3-11e8-b443-00163e990bdb","created_by": "67460e74-02e3-11e8-b443-00163e990bew","modified_by": "65550e74-02e3-11e8-b443-00163e990bdb"}' \
  http://localhost:8000/discount-code/create/
```
#### get discount code
```
curl --header "Content-Type: application/json" \
  --request GET \
  http://localhost:8000/discount-code/65550e74-02e3-11e8-b443-00163e990bdb
```
