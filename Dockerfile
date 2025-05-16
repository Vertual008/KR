WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY tasklist.py .
EXPOSE 5000
CMD ["python", "tasklist.py"]
