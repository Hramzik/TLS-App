# TLS App

В этом проекте приводится пример приложения на защищенном TLS с использованием библиотеки Python `ssl`

## Требования

- Python 3.x
- OpenSSL (опционально)

## Запуск
### Генерация сертификата и ключа (опционально)
```sh
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -nodes -subj "/CN=localhost"
```

### Запуск сервера
```sh
python server.py <cert_path> <key_path>
```

### Запуск клиента
```sh
python client.py <cert_path>
```

### Запись трафика
Используйте Wireshark для записи сетевой трассы.

Для расшифровки сообщений укажите файл `ssl_logs.txt` в настройках Wireshark для расшифровки TLS трафика.
