all: help

help:
	@echo ""
	@echo "Help for Friday --- A Chatter Robot"
	@echo ""
	@echo "    install        install dependence of project"
	@echo "    dev            development mode"
	@echo ""

install:
	@pip install -r requirements

dev:
	@python3 manage.py
