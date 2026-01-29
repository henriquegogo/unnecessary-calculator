printf "Serving in http://localhost:8000/"
busybox httpd -f -p 8000 -h frontend
