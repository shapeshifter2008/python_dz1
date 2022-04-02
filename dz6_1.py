import requests

url_data = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(url_data).text
response = response.split('\n')
spam_ip_log = {}

for row in response:
    data = row.split(' - - ')
    ip = data[0]

    spam_ip_log.setdefault(ip, 0)
    spam_ip_log[ip] = spam_ip_log[ip]+1

spam_ip, spam_requests = sorted(spam_ip_log.items(), key=lambda item: item[1], reverse=True)[0]
print('Spamer is:', spam_ip, spam_requests)