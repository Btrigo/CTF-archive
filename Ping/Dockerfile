FROM php:apache AS RUNTIME
ARG DEBIAN_FRONTEND=noninteractive
ARG FLAG

WORKDIR /var/www/html
COPY app/index.php /var/www/html/
RUN apt update && \
    apt install -yq \
    iputils-ping && \
    rm -rf /var/lib/apt/lists/* && \
    echo "${FLAG}" > /flag.txt && \
    chown root:www-data /flag.txt && \
    chmod 644 /flag.txt

EXPOSE 80
