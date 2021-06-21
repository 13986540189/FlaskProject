FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --upgrade pip
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]