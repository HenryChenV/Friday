all: help

help:
	@echo ""
	@echo "Help for Friday --- A Chatter Robot"
	@echo ""
	@echo "    install        install dependence of project"
	@echo "    dev            development mode"
	@echo ""

install:
	@pip3 install -r requirements

dev:
	@python3 manage.py
