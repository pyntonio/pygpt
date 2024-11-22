import openai
from fastapi import HTTPException

class ImageGenerator:
    def __init__(self, api_key: str):
        """
        Inizializza la classe ImageGenerator con la chiave API di OpenAI.
        :param api_key: La chiave API per autenticarsi con OpenAI.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    async def generate_image(self, prompt: str, size: str = "1024x1024"):
        """
        Genera un'immagine basata su un prompt testuale utilizzando OpenAI DALL·E.
        :param prompt: La descrizione dell'immagine da generare.
        :param size: Dimensioni dell'immagine (opzioni: "256x256", "512x512", "1024x1024").
        :return: URL dell'immagine generata.
        """
        try:
            # Validazione dimensioni
            valid_sizes = ["256x256", "512x512", "1024x1024"]
            if size not in valid_sizes:
                raise ValueError(f"Dimensione non valida. Usa una delle seguenti: {', '.join(valid_sizes)}")

            # Chiamata API OpenAI per generare l'immagine
            response = openai.Image.create(
                prompt=prompt,
                n=1,  # Numero di immagini da generare
                size=size
            )

            # Estrarre l'URL dell'immagine generata
            image_url = response["data"][0]["url"]
            return {
                "prompt": prompt,
                "size": size,
                "image_url": image_url
            }

        except openai.error.OpenAIError as e:
            # Gestione degli errori specifici di OpenAI
            raise HTTPException(status_code=500, detail=f"Errore OpenAI: {str(e)}")
        except ValueError as e:
            # Errori di validazione locale
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            # Errori generici
            raise HTTPException(status_code=500, detail=f"Errore nella generazione dell'immagine: {str(e)}")
