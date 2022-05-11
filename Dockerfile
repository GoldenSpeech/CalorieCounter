FROM python:3

EXPOSE 1942

WORKDIR /usr/kaguled/Desktop/csci3081/hw1_api

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "/usr/kaguled/Desktop/csci3081/hw1_api/Calorie.py" ]
