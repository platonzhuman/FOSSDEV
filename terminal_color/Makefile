.PHONY: help install test clean

PROJECT_NAME = terminal_color

help:
	@echo "! ! ! Вы в поддержке базовых учебных проектов ! ! !"
	@echo ""
	@echo "make install  ---> установить пакет локально"
	@echo "make test     ---> запустить тесты"
	@echo "make clean    ---> очистить мусор"

install:
	cd $(PROJECT_NAME) && pip install -e .

test:
	cd $(PROJECT_NAME) && pytest tests/ -v

clean:
	cd $(PROJECT_NAME) && rm -rf build/ dist/ *.egg-info .pytest_cache/
	find $(PROJECT_NAME) -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find $(PROJECT_NAME) -type f -name "*.pyc" -delete
	@echo ">>> Очищено!"