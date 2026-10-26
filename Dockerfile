FROM python:3.12-slim

WORKDIR /app

# Install dependencies first (cached unless requirements change)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/

# Run as a non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "2", "src.app:app"]
