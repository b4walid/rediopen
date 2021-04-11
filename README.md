# About Rediopen
Detect open redirection bug

# Examples
python3 rediopen.py -u https://www.google.com -f payloads2.txt
scan main site
python3 rediopen.py -w site.txt -f payloads2.txt
scan multiple web site
python3 rediopen.py -l link.txt -f payloads2.txt
scan multiple link with parameter
