FROM python:3.12-slim
# Logs visibles immédiatement dans "docker compose logs"
ENV PYTHONUNBUFFERED=1
WORKDIR /srv/app
COPY app.py ./
# DevSecOps : ne pas exécuter le service en root
RUN useradd --create-home --uid 10001 appuser
USER appuser
EXPOSE 8000
# Santé observable par Docker (docker compose ps affiche "healthy")
HEALTHCHECK --interval=10s --timeout=3s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2)"
CMD ["python", "app.py"]
