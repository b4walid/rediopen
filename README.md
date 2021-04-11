<h3> About Rediopen</h3>
<p>Rediopn detect open redirection on main site like https://www.b4walid.com or multiple main site or multiple link with parameter like https://www.b4walid.com/index.php?url=//google.com</p>
<h3> ScreenShot </h3>
<img src="https://i.imgur.com/rBR1kZm.png">
<h3> Installation</h3>
<code>git clone https://github.com/b4walid/rediopen.git</code>
<h3> Examples</h3>
python3 rediopen.py -u https://www.google.com -f payloads2.txt<br>
scan main site.<br>
python3 rediopen.py -w site.txt -f payloads2.txt<br>
scan multiple web site.<br>
python3 rediopen.py -l link.txt -f payloads2.txt<br>
scan multiple link with parameter.<br>
