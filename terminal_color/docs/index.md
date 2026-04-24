
# Подробная установка с самого нуля в приложении IDLE PYTHON, VS-CODE, PYCHARM ...

## Установка

Создание виртуального окружения:

```
python3 -m venv venv
```

Активация:

```
source env/bin/activate
```

Установка пакета:

```
pip install --index-url https://test.pypi.org/simple/ terminal-color-tool==0.1.2 --no-cache-dir
```

## Проверка

```
terminal-color --list
```

## Использование

Цвет текста:

```
eval "$(terminal-color red)"
```

Цвет фона:

```
eval "$(terminal-color bg_green)"
```

Сброс:

```
eval "$(terminal-color --reset)"
```

Без eval (временный вывод):

```
terminal-color blue
echo "текст"
terminal-color --reset
```

## Деактивация окружения

```
deactivate
```
```

## Ссылки

- [Исходный код на GitHub](https://github.com/platonzhuman/FOSSDEV)
- [Пакет на Test PyPI](https://test.pypi.org/project/terminal-color-tool/)
- Автор: NoName ^_^ (77pl77@inbox.ru)
```
