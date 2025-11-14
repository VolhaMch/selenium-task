FROM python:3.9-bullseye

WORKDIR /project

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    libnss3 \
    libgbm1 \
    fonts-liberation \
    xdg-utils \
    libx11-6 \
    libxext6 \
    libxrandr2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Добавляем официальный репозиторий Google Chrome и ставим Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
       > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Скачиваем фиксированную версию Chromedriver
RUN DRIVER_VERSION=142.0.7444.162 \
    && wget -q "https://storage.googleapis.com/chrome-for-testing-public/${DRIVER_VERSION}/linux64/chromedriver-linux64.zip" \
    && unzip chromedriver-linux64.zip \
    && mv chromedriver-linux64/chromedriver /usr/bin/chromedriver \
    && chmod +x /usr/bin/chromedriver \
    && rm -rf chromedriver-linux64 chromedriver-linux64.zip

# Устанавливаем Python-зависимости
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем проект
COPY . .

# Запуск тестов
CMD ["pytest", "tests"]
