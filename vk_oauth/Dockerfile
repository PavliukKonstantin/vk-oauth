#################
# BUILDER IMAGE #
#################

FROM python:3.8.4-alpine as BUILDER

# Install dependecies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
COPY requirements.txt /install/requirements.txt
RUN pip install --prefix=/install -r /install/requirements.txt


####################
# PRODUCTION IMAGE #
####################

FROM python:3.8.4-alpine

# Set enviroments variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create the app user
RUN addgroup -S app && adduser -S app -G app

# Change workdir
WORKDIR /home/app/web

# Install dependecies
COPY --from=builder /install /usr/local
RUN apk --no-cache add libpq

# Copy Django project
COPY . .

# Chown all files to the app user
RUN chown -R app:app .

# Run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
