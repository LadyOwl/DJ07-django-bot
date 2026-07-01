# 🤖 DJ07-django-bot

**Интеграция Django REST API с Telegram-ботом**

Профессиональный проект, демонстрирующий архитектуру клиент-серверного взаимодействия между Telegram-ботом и Django REST API. Бот регистрирует пользователей в базе данных Django и предоставляет информацию о них через команды.

---

## 🎯 О проекте

DJ07-django-bot — это учебный проект, созданный для демонстрации навыков работы с Django REST Framework, Telegram Bot API и построения распределённых систем. Проект реализует полноценную систему регистрации и управления пользователями Telegram через REST API.

### 💡 Ключевые особенности

- ✅ **REST API** — полноценный backend на Django REST Framework
- ✅ **Telegram Bot** — клиентское приложение на pyTelegramBotAPI
- ✅ **Модель данных** — хранение пользователей Telegram в базе данных
- ✅ **CRUD-операции** — создание и чтение записей пользователей
- ✅ **Архитектура клиент-сервер** — бот взаимодействует с API через HTTP
- ✅ **CORS** — настроен для безопасного взаимодействия
- ✅ **JSON API** — обмен данными в формате JSON

---

## 🏗️ Архитектура системы

```
┌─────────────────┐
│  Telegram User  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Telegram Bot   │  (telegram_bot.py)
│  - /start       │
│  - /myinfo      │
└────────┬────────┘
         │ HTTP Requests (JSON)
         ▼
┌─────────────────┐
│  Django REST    │  (Django + DRF)
│  API Server     │
│  - /api/register│
│  - /api/user    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  SQLite DB      │
│  (TelegramUser) │
└─────────────────┘
```

---

## 🛠️ Технический стек

| Категория | Технология |
|-----------|-----------|
| **Backend** | Python 3.x, Django 6.0.1 |
| **REST API** | Django REST Framework 3.16.1 |
| **Telegram Bot** | pyTelegramBotAPI 4.30.0 |
| **CORS** | django-cors-headers 4.9.0 |
| **Database** | SQLite |
| **HTTP Client** | requests 2.32.5 |
| **IDE** | PyCharm |

---

## 📂 Структура проекта

```
DJ07-django-bot/
│
├── myproject/                  # Конфигурация Django-проекта
│   ├── settings.py             # Настройки Django, DRF, CORS
│   ├── urls.py                 # Маршруты проекта
│   ├── wsgi.py                 # WSGI-конфигурация
│   └── asgi.py                 # ASGI-конфигурация
│
├── bot/                        # Django-приложение для API
│   ├── migrations/             # Миграции базы данных
│   ├── models.py               # Модель TelegramUser
│   ├── serializers.py          # DRF сериализаторы
│   ├── views.py                # API views (register, user info)
│   ├── urls.py                 # Маршруты API
│   └── admin.py                # Настройки админ-панели
│
├── telegram_bot.py             # Telegram-бот (клиент)
├── requirements.txt            # Зависимости проекта
├── db.sqlite3                  # База данных SQLite
├── manage.py                   # Утилита управления Django
└── README.md                   # Документация проекта
```

---

## 🚀 Быстрый старт

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/LadyOwl/DJ07-django-bot.git
cd DJ07-django-bot
```

### 2. Создайте виртуальное окружение

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

### 4. Примените миграции

```bash
python manage.py migrate
```

### 5. Настройте Telegram-бот

1. Откройте [@BotFather](https://t.me/BotFather) в Telegram
2. Отправьте команду `/newbot`
3. Следуйте инструкциям и получите токен бота
4. Откройте файл `telegram_bot.py` и замените `BOT_TOKEN` на ваш токен:

```python
BOT_TOKEN = 'ваш_токен_от_BotFather'
```

### 6. Запустите Django-сервер

Откройте **первый терминал** и выполните:

```bash
python manage.py runserver
```

Сервер запустится на `http://127.0.0.1:8000/`

### 7. Запустите Telegram-бот

Откройте **второй терминал** и выполните:

```bash
python telegram_bot.py
```

Бот начнёт опрашивать Telegram API.

### 8. Протестируйте бота

1. Откройте вашего бота в Telegram
2. Отправьте команду `/start` — вы будете зарегистрированы
3. Отправьте команду `/myinfo` — получите информацию о себе

---

## 📱 Команды бота

### `/start` — Регистрация пользователя

Регистрирует пользователя в базе данных Django.

**Пример:**
```
Пользователь: /start
Бот: ✅ Вы успешно зарегистрированы!
```

**Что происходит:**
1. Бот получает `telegram_id` и `username` пользователя
2. Отправляет POST-запрос на `/api/register/`
3. Django создаёт запись в модели `TelegramUser`
4. Бот подтверждает успешную регистрацию

### `/myinfo` — Получение информации

Показывает информацию о пользователе из базы данных.

**Пример:**
```
Пользователь: /myinfo
Бот: ID: 123456789
     Username: lady_owl
```

**Что происходит:**
1. Бот получает `telegram_id` пользователя
2. Отправляет GET-запрос на `/api/user/`
3. Django возвращает данные пользователя
4. Бот отображает информацию

---

## 💻 API Endpoints

### POST `/api/register/`

Регистрирует нового пользователя или обновляет существующего.

**Запрос:**
```json
{
  "telegram_id": 123456789,
  "username": "lady_owl"
}
```

**Ответ (201 Created):**
```json
{
  "telegram_id": 123456789,
  "username": "lady_owl"
}
```

**Ответ (200 OK — если пользователь уже существует):**
```json
{
  "telegram_id": 123456789,
  "username": "lady_owl"
}
```

### GET `/api/user/`

Получает информацию о пользователе по `telegram_id`.

**Запрос:**
```
GET /api/user/?telegram_id=123456789
```

**Ответ (200 OK):**
```json
{
  "telegram_id": 123456789,
  "username": "lady_owl"
}
```

**Ответ (404 Not Found):**
```json
{
  "error": "User not found"
}
```

---

## 🗄️ Модель данных

### TelegramUser

```python
class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.username} ({self.telegram_id})"
```

**Поля:**
- `telegram_id` — уникальный идентификатор пользователя в Telegram
- `username` — имя пользователя в Telegram

---

## 🔧 Ключевые фрагменты кода

### API View для регистрации (bot/views.py)

```python
@api_view(['POST'])
def register_user(request):
    telegram_id = request.data.get('telegram_id')
    username = request.data.get('username')
    
    if not telegram_id:
        return Response({'error': 'telegram_id is required'}, status=400)
    
    user, created = TelegramUser.objects.get_or_create(
        telegram_id=telegram_id,
        defaults={'username': username}
    )
    
    if not created and user.username != username:
        user.username = username
        user.save()
    
    serializer = TelegramUserSerializer(user)
    return Response(serializer.data, status=200 if not created else 201)
```

### Обработчик команды /start (telegram_bot.py)

```python
@bot.message_handler(commands=['start'])
def start_handler(message):
    user_id = message.from_user.id
    username = message.from_user.username or f"user_{user_id}"
    
    try:
        response = requests.post(
            f"{API_URL}/register/",
            json={'telegram_id': user_id, 'username': username},
            timeout=5
        )
        
        if response.status_code in (200, 201):
            bot.reply_to(message, "✅ Вы успешно зарегистрированы!")
        else:
            bot.reply_to(message, "❌ Ошибка регистрации.")
    except Exception:
        bot.reply_to(message, "❌ Не удалось подключиться к серверу.")
```

---

## 🎓 Чему я научилась в этом проекте

### ✅ Django REST Framework
- Создание API endpoints с `@api_view`
- Работа с сериализаторами `ModelSerializer`
- Обработка GET и POST запросов
- Возврат JSON-ответов с правильными HTTP-статусами

### ✅ Telegram Bot API
- Создание бота с `pyTelegramBotAPI`
- Обработка команд через `@bot.message_handler`
- Получение информации о пользователях
- Polling для получения обновлений

### ✅ Архитектура клиент-сервер
- Разделение логики на backend (Django) и client (бот)
- HTTP-запросы между компонентами
- Работа с JSON данными
- Обработка ошибок и таймаутов

### ✅ Работа с базой данных
- Создание моделей Django
- Миграции и управление схемой БД
- Методы `get_or_create`, `get`, `save`
- Уникальные поля и валидация

### ✅ CORS и безопасность
- Настройка `django-cors-headers`
- Разрешённые источники (allowed origins)
- Безопасное взаимодействие между клиентом и сервером

### ✅ Best Practices
- Разделение ответственности (SRP)
- Обработка исключений
- Таймауты для HTTP-запросов
- Чистая структура проекта

---

## 📸 Скриншоты

*(Здесь будут скриншоты вашего приложения)*

### Работа бота в Telegram
![Telegram Bot](screenshot1.png)

### Django Admin панель
![Django Admin](screenshot2.png)

### API ответы в Postman
![API Testing](screenshot3.png)

---

## 🔮 Возможные улучшения

Проект может быть расширен следующими функциями:

- [ ] **Аутентификация** — токены для доступа к API
- [ ] **Больше команд бота** — обновление профиля, удаление аккаунта
- [ ] **Дополнительные поля** — email, телефон, дата регистрации
- [ ] **Уведомления** — отправка сообщений пользователям
- [ ] **Статистика** — подсчёт пользователей, активности
- [ ] **PostgreSQL** — переход на production-базу данных
- [ ] **Docker** — контейнеризация приложения
- [ ] **Документация API** — Swagger/OpenAPI
- [ ] **Тесты** — unit-тесты для views и бота
- [ ] **Логирование** — запись действий в логи
- [ ] **Кэширование** — Redis для ускорения запросов
- [ ] **Веб-интерфейс** — админ-панель для управления пользователями

---

## 🧪 Тестирование API

### С помощью curl

**Регистрация пользователя:**
```bash
curl -X POST http://127.0.0.1:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"telegram_id": 123456789, "username": "test_user"}'
```

**Получение информации:**
```bash
curl http://127.0.0.1:8000/api/user/?telegram_id=123456789
```

### С помощью Postman

1. Создайте новый POST-запрос на `http://127.0.0.1:8000/api/register/`
2. В Body выберите `raw` и формат `JSON`
3. Добавьте данные:
   ```json
   {
     "telegram_id": 123456789,
     "username": "test_user"
   }
   ```
4. Отправьте запрос

---

## 📜 Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. файл [LICENSE](LICENSE).

---

## 👤 Автор

**Юлия (Джулия)** — [@LadyOwl](https://github.com/LadyOwl)

📧 Связаться со мной: [GitHub](https://github.com/LadyOwl)

---

## 🙏 Благодарности

- **Django Project** — отличный веб-фреймворк
- **Django REST Framework** — мощный инструмент для создания API
- **pyTelegramBotAPI** — удобная библиотека для работы с Telegram
- **Telegram** — отличная платформа для ботов

---

<div align="center">

**Если вам понравился этот проект, поставьте ⭐ на GitHub!**

*Сделано с ❤️, Django и Telegram*

</div>
