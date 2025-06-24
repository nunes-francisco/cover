.PHONY: all install format lint sec test

all: install format lint sec test

install:
	# Instalando as diversas ferramenta de checagem e formatação
	@pip install isort~=5.10 blue prospector pip-audit --upgrade

	# Instalando a suíte de Testes Unitários
	@pip install pytest~=7.0 pytest-cov~=3.0 pytest-asyncio~=0.18 --upgrade

requirements:
	# Instala as demais biblitecas necessárias para a execução dos testes unitários
	@pip install -r requirements.dev --upgrade

format:
	@isort <PROJETO>
	@blue <PROJETO>

lint:
	@isort <PROJETO> --check
	@blue <PROJETO> --check
	@prospector <PROJETO> --no-autodetect

sec:
	@pip-audit

test:
	@pytest --cov=./<PROJETO> --cov-report html -p no:warnings
