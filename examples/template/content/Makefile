.PHONY: install test run docker-build

install:
	python3 -m pip install -r requirements.txt

test:
	pytest -q

run:
	uvicorn src.main:app --host 0.0.0.0 --port ${{ values.port }}

docker-build:
	docker build -t ${{ values.serviceName }}:local .
