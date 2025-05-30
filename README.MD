# Weather Forecast App 

Приложение на Django, которое показывает прогноз погоды по введённому городу.  
Использует API Open-Meteo и выводит прогноз в удобном формате карточек.

---

##  Функционал

✅ Ввод города и получение прогноза  
✅ Отображение карточек с погодой на 12 часа  
✅ Автодополнение (подсказки) при вводе города  
✅ Сохраняется последний просмотренный город (через cookie)  
✅ История поиска: API `api/city-stats/` показывает, сколько раз искали каждый город  
✅ Тесты для ключевых функций  
✅ Docker для быстрого развертывания

---

## ⚙️ Используемые технологии

- **Django**
- **Open-Meteo API** (Geocoding + Weather)
- **requests / pandas / numpy / requests-cache**
- **HTML, Javascript** 
- **Docker / Docker Compose** 

---

## 🐳 Запуск с Docker

1. Клонируй репозиторий:
```bash
git clone https://github.com/USERNAME/weather-forecast-django.git
cd weather-forecast-django
```
2. Собери и запусти контейнер:
```bash
docker-compose up --build
```

3. Открой приложение в браузере:
```bash
http://localhost:8000/
```

## Локальный запуск (без Docker)

1.  Установи зависимости:
```bash
pip install -r requirements.txt
```
2. Выполни миграции (если нужно):
```bash
python manage.py migrate
```
3. Запусти сервер:
```bash
python manage.py runserver
```
4. Открой в браузере:
```bash
http://127.0.0.1:8000/
```

## Тест
```bash
python manage.py test
```