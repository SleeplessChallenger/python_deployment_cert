<h2>How to generate keys and what do they mean?</h2>

- There are 2 types: public and private keys to create SSL certificate<br>
	and enable https (http over TLS)
- You can check in more detail my notes. Look at **22** :<br>
	<a href="https://github.com/SleeplessChallenger/SystemsExpert.git">Here</a>

<h3>Ways to generate keys</h3>

<ins>Let's use Flask for this purpose</ins>

1. Automcatic way of generating: `app.run(ssl_context="adhoc")` which is not safe.
	- you also need to isntall: `pip install pyopenssl`

2. By hands: `app.run(ssl_context=('cert.pem', 'key.pem'))`. But here we need to generate them:
	<ul>
		<li>openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365</li>
		<li>Better: openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout nginx.key -out nginx.crt</li>
		<li>Check this link to get better idea: <a href="https://www.digicert.com/kb/ssl-support/openssl-quick-reference-guide.htm">Click</a>
		<li> cert is public key & key is private key

3. If you want to use `Gunicorn`: `gunicorn --certfile cert.pem --keyfile key.pem -b 0.0.0.0:8000 wsgi:app`

<h3>And if you want to use NGINX without gunicorn</h3>

- Scheme: we have incoming request on some port and **nginx** will handle/reroute it to **<ins>unexposed</ins>** inner port of the **app**. This app will handle the<br>
	endpoint and return answer or error.

<h4>Notes about deployment via Nginx</h4>

- no need to **EXPOSE** in `Dockerfile` if you use `run` with **port**
- put this **port** from `run` into `nginx.conf/location`
- in the same `config` file put listen as the `port` exposed to `docker-compose` for **nginx**
- in `docker-compose` pay attention to **volumes**. Especially, to `.crt` and `.key`. We create folder inside `nginx` where we put generated certs and in **volumes**<br>
	we match our ones to the root folder of `nginx`

<h4>Make requests</h4>

- `curl -k -X GET https://localhost/health`
- `curl -k -X GET https://localhost/`
- `curl -k -X POST https://localhost/predict`

PS: you don't need to specify **443** as **https** includes it already as **http** by default includes **80**


<h4>Ways to prevent response without correct cert</h4>

- There is such a thing: `.pem` file which includes private & public key. It's used to enable verification
- We want to create a so-called **fence** which won't return response withour certificate

<ol>
	<li>curl -k --cert  nginx.pem  -X GET https://localhost/ is a request</li>
		<ul>
			<li>-k is to remove errors as we use self-signed certs</li>
			<li>--cert is to include the very certification</li>
			<li>nginx.pem is that file which includes</li>
		</ul>
</ol>

- Links to visit:
	1. https://smallstep.com/hello-mtls/doc/client/curl
	2. https://support.f5.com/csp/article/K18050039
	3. https://habr.com/en/post/213741/
