#usage ./ipinfo <ip-address> <the-category>
curl http://ip-api.com/json/$1 | jq --arg foo $2 '.[$foo]'
