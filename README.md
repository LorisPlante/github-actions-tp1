# MLOps GitHub Actions TP
![Build Status](https://github.com/LorisPlante/github-actions-tp1/actions/workflows/badge.yml/badge.svg)

## Qst 8

    Un workflow "Hello World" est déclenché et marqué Success

## Qst 10

    Un nouveau job "Run Tests" s'exécute et tes tests passent 

## Qst 11

    Le job "Run Tests" échoue

## Qst 14

    Trois jobs sont exécutés en parallèle avec les 3 versions renseignées

## Qst 16

    Le lint s'effectue et passe correctement

## Qst 18

    Les tests s'effectuent et un commentaire de github-actions s'affiche 

## Qst 21

    Le badge s'affiche sur le readme

## Qst 24

    Un nouveau workflow "Docker Build" se déclenche, il build l'image Docker il exécute le conteneur et affiche la sortie (predict_sentiment).

## Qst 27

    {
    "accuracy": 0.989,
    "precision": 0.857,
    "recall": 0.883,
    "f1_score": 0.9
    }

## Qst 30

    Model accuracy: 0.861
    ❌ Model accuracy below threshold (0.9)
    Error: Process completed with exit code 1.

    Model accuracy: 0.881
    ❌ Model accuracy below threshold (0.9)
    Error: Process completed with exit code 1.

## Qst 33

    Run echo "Running tests in dev environment"
    echo "Running tests in dev environment"
    shell: /usr/bin/bash -e {0}
    Running tests in dev environment

## Qst 36 

    il y a la release v1.0.1 (car j'ai raté la v1.0.0)
    avec deux fichiers compressés :
        Source code (zip)
        Source code (tar.gz)

## Qst 38

    contenu de la doc : 
        
        <a id="model"></a>

        # model

        <a id="model.predict_sentiment"></a>

        #### predict\_sentiment

        ```python
        def predict_sentiment(text: str) -> str
        ```

        Predicts the sentiment of a given text.

        Args:
            text (str): The input text to analyze.

        Returns:
            str: Sentiment label - "positive", "negative", or "neutral".
        
## Qst 40

    le temps du deuxième build est moins long que le premier car il utilise le cache mit en place par le premie buidl