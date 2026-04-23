# Terminal Color

Утилита для смены цвета терминала через ANSI-коды.

## Возможности

- Изменение цвета текста (8 цветов)
- Изменение цвета фона (8 цветов)
- Стили текста (жирный, подчёркнутый)
- Просмотр всех доступных цветов
- Сброс настроек

## Установка

```bash
pip install --index-url https://test.pypi.org/simple/ terminal-color-tool
```

## Использование

### Цвета текста

```bash
terminal-color red       # красный
terminal-color green     # зелёный
terminal-color blue      # синий
terminal-color yellow    # жёлтый
terminal-color cyan      # голубой
terminal-color magenta   # пурпурный
terminal-color white     # белый
terminal-color black     # чёрный
```

### Цвета фона

```bash
terminal-color bg_red     # красный фон
terminal-color bg_green   # зелёный фон
terminal-color bg_blue    # синий фон
terminal-color bg_yellow  # жёлтый фон
```

### Стили текста

```bash
terminal-color bold       # жирный
terminal-color underline  # подчёркнутый
```

### Специальные команды

```bash
terminal-color --list     # показать все доступные цвета
terminal-color --reset    # сбросить цвет к стандартному
```

### Пример использования

```bash
terminal-color red
echo "Этот текст красный"
terminal-color --reset
echo "Этот текст обычный"
```

## Документация

Подробная документация в файле [docs/index.md](docs/index.md)

## Разработка

```bash
# Клонирование репозитория
git clone https://github.com/platonzhuman/FOSSDEV
cd terminal_color

# Установка в режиме разработки
pip install -e .

# Запуск тестов
pytest tests/ -v
```

## Автор

NoName ^_^ - 77pl77@inbox.ru

## Ссылки

- [GitHub](https://github.com/platonzhuman/FOSSDEV)
- [Test PyPI](https://test.pypi.org/project/terminal-color-tool/)