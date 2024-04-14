# Инструкция для запуска автотестов задания 2

## 1. Склонировать репозиторий с GitHub

Склонировать репозиторий с GitHub с помощью команды git clone:
```
git clone git@github.com:Unga62/avito_testing.git
```

## 2. Создать и настроить вирутальное окружение

1. Создать виртуальное окружение (далее - venv) с помощью команды:
```
python -m venv venv
```

2. Активировать venv с помощью команды:
```
source venv/bin/activate 
```

3. Если потребуется обновить pip с помощью команды:
```
pip install --upgrade pip
```

4. Установить необходимые пакеты для работы автотестов из файла ***requirements.txt*** c помощью команды:
```
pip install -r requirements.txt
```

5. Установить браузеры для работы с playwright с помощью команды:
```
playwright install
```

## 3. Запуск автотестов

Автотесты запустить после перехода в директорию `unit_2` с помощью команды `pytest`

## Cтруктура проекта

```
avito_testing/     
├─ unit_1/
│  ├─ test_one.md       Ответ на задание 1
├─ unit_2/
│  ├─ output/           Каталог который хранит скриншоты по итогам автотестов
│  ├─ test_avito.py     Автотесты
│  ├─ TESTCASES.md      Описание тест кейсов
├─ README.md            Инструкция для запуска автотестов задания 2
├─ requirements.txt     Необходимые пакеты для корректной работы автотестов
```