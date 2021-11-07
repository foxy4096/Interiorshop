# Blog
A Simple E-Commerce app made with Django


<h2>Instructions</h2>

<h4>Make sure you have <a href="https://python.org/downloads/"> python</a> installed</h4>

Step 1. Open a terminal

Step 2. Paste the given code in the terminal
```
git clone https://github.com/foxy4096/Interiorshop
```
Step 3. Now type this in the terminal
```
cd Interiorshop
```
Step 4. Now paste this in the terminal
```
python -m venv env
# and 
.\env\Scripts\activate
or for *nix system
source .\env\Scripts\activate
#and then type
pip install -r requirements.txt
```
Step 5. Now type
```
python manage.py makemigrations
# and
python manage.py migrate
```
Step 6. Now go type this command to create a new superuser
```
python manage.py createsuperuser
```
Step 7. After that type this and go to your web browser and go to <a href="http://localhost:8000">here</a>
```
python manage.py runserver
```
