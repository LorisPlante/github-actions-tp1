FROM python:3.10-slim

# Définir le dossier de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code de l'application
COPY . .

# Lancer directement une prédiction avec un texte test
CMD ["python", "-c", "from model import predict_sentiment; print(predict_sentiment('I am happy to use Docker with GitHub Actions'))"]
