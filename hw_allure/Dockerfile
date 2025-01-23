FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy application code
COPY . /app

# Install dependencies
RUN pip install pytest
RUN pip install psycopg2
RUN pip install allure-pytest

# Run tests
CMD ["pytest", "test_database_allure.py", "--alluredir=allure-results"]