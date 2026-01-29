.PHONY: all run tests

all: run

run:
	@printf "Serving in http://localhost:8000/"
	@busybox httpd -f -p 8000 -h frontend

tests:
	@echo "Running tests..."
	@python3 -m unittest discover backend
