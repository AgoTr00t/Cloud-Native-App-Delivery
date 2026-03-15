# Étape 1: Utiliser une image légère Python 3.9 Alpine
FROM python:3.9-alpine

# Étape 2: Métadonnées
LABEL maintainer="ATG AKD AWA" \
      version="1.0" \
      description="Inventory Management Application"

# Étape 3: Variables d'environnement pour optimiser Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000 \
    # Éviter de créer des fichiers .pyc
    PYTHONPYCACHEPREFIX=/tmp/cache

# Étape 4: Créer un utilisateur non-root pour la sécurité
RUN addgroup -g 1000 -S appgroup && \
    adduser -u 1000 -S appuser -G appgroup

# Étape 5: Définir le répertoire de travail
WORKDIR /app

# Étape 6: Copier uniquement requirements.txt d'abord (optimisation du cache)
COPY app/requirements.txt .

# Étape 7: Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt && \
    # Nettoyer le cache pip pour réduire la taille
    rm -rf /root/.cache/pip

# Étape 8: Copier le reste du code
COPY app/ .

# Étape 9: Changer les permissions pour l'utilisateur non-root
RUN chown -R appuser:appgroup /app && \
    chmod -R 755 /app

# Étape 10: Passer à l'utilisateur non-root
USER appuser

# Étape 11: Exposer le port
EXPOSE 5000

# Étape 12: Commande de démarrage
CMD ["python", "app.py"]