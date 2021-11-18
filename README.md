<h2>How to generate keys and what do they mean?</h2>

- There are 2 types: public and private keys to create SSL certificate<br>
	and enable https (http over TLS)
- You can check in more detail my notes. Look at **22** :<br>
	<a href="git@github.com:SleeplessChallenger/SystemsExpert.git">Here</a>

<h3>Ways to generate keys</h3>

<ins>Let's use Flask to for this purpose</ins>

1. Automcatic way of generating: `app.run(ssl_context="adhoc")` which is not safe.
	- you also need to isntall: `pip install pyopenssl`

2. By hands: `app.run(ssl_context=('cert.pem', 'key.pem'))`. But here we need to generate them:
	<ul>
		<li>`openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`</li>
		<li>Check this link to get better idea: <a href="https://www.digicert.com/kb/ssl-support/openssl-quick-reference-guide.htm">Click</a>
		<li> **cert** is **public key** & **key** is **private key**

3. If you want to use `Gunicorn`: `gunicorn --certfile cert.pem --keyfile key.pem -b 0.0.0.0:8000 wsgi:app`

<h3>And if you want to use NGINX without gunicorn</h3>




