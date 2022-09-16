FROM postgres:latest
ENV POSTGRES_HOST=localhost
ENV POSTGRES_USER=akash.kareliya
ENV POSTGRES_PASSWORD=123

EXPOSE 54321

COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql

