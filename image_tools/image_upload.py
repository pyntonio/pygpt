import os
from fastapi import HTTPException, UploadFile
from uuid import uuid4

class ImageUploader:
    def __init__(self, upload_path: str = "uploaded_images/"):
        """
        Inizializza la classe ImageUploader con una directory predefinita per i file caricati.
        :param upload_path: Directory dove salvare le immagini caricate.
        """
        self.upload_path = upload_path
        os.makedirs(self.upload_path, exist_ok=True)

    async def upload_image(self, file: UploadFile):
        """
        Carica un'immagine e la salva nella directory configurata.
        :param file: Il file immagine caricato.
        :return: Percorso del file caricato.
        """
        try:
            # Controlla il tipo di file
            valid_content_types = ["image/jpeg", "image/png", "image/gif"]
            if file.content_type not in valid_content_types:
                raise HTTPException(
                    status_code=400,
                    detail=f"Formato non supportato: {file.content_type}. Usa solo JPEG, PNG o GIF."
                )

            # Genera un nome univoco per il file
            file_extension = file.filename.split(".")[-1]
            unique_filename = f"{uuid4()}.{file_extension}"
            file_path = os.path.join(self.upload_path, unique_filename)

            # Salva il file
            with open(file_path, "wb") as image_file:
                content = await file.read()
                image_file.write(content)

            return {
                "message": "File caricato con successo",
                "file_path": file_path
            }

        except HTTPException as e:
            # Errore gestito (es. formato non valido)
            raise e
        except Exception as e:
            # Errore generico
            raise HTTPException(status_code=500, detail=f"Errore durante il caricamento: {str(e)}")
