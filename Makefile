.PHONY: all

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

test: venv/bin/activate
	( \
	./venv/bin/coverage run -m pytest -vv tests/; \
	./venv/bin/coverage report -m --omit='tests/test_*.py'; \
	)

run-triage: venv/bin/activate
	python app.py triage

freeze: venv/bin/pip
	./venv/bin/pip freeze > requirements.txt

clean:
	find . -type d -name __pycache__ -exec rm -rf {} \;
	rm -rf venv
	rm -rf .pytest_cache
	rm .coverage