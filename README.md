# Yonagi.com
<b>Hosting:</b> S3

<b>Content Delivery:</b> Cloudflare

<b>SSL:</b> Amazon Certificate Manager

<b>CSS Library:</b> Bootstrap 4

<b>Live Site:</b> https://www.yonagi.com

<b>Original Author:</b> Yona Gidalevitz (aka: funkechild)

<b>Python Instructions below:</b> 
    
        1. Make sure you have python installed, just run python in command line
        2. If running "python" doesn't return a shell, you need to install it, google it
        3. Note, "python3" may also be installed
        4. Run "python3 -m venv ./venv/." in the root directory, *or python if it's python --version is 3.xx.xx, what you want is python version 3, not 2
        5. Run "source venv/bin/activate" from the root directory, this initializes the virtual environment
        6. Run "pip install -r requirements.txt", hit yes to everything
        7. Run "flask run", the webserver will startup and show you the localhost port it's running on, check it out in your browser
