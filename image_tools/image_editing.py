from PIL import Image, ImageDraw, ImageFont
import os
from fastapi import HTTPException

class ImageEditor:
    def __init__(self, storage_path: str = "edited_images/"):
        """
        Inizializza la classe ImageEditor con un percorso di archiviazione predefinito.
        :param storage_path: Directory dove salvare le immagini modificate.
        """
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)

    async def edit_image(self, file_path: str, operation: str, **kwargs):
        """
        Modifica un'immagine in base all'operazione specificata.
        :param file_path: Percorso dell'immagine da modificare.
        :param operation: Tipo di operazione da applicare ("resize", "rotate", "add_text").
        :param kwargs: Parametri aggiuntivi per l'operazione.
        :return: Percorso dell'immagine modificata.
        """
        try:
            # Carica l'immagine dal file_path
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"L'immagine non esiste: {file_path}")
            image = Image.open(file_path)

            # Operazioni supportate
            if operation == "resize":
                width = kwargs.get("width")
                height = kwargs.get("height")
                if not width or not height:
                    raise ValueError("Sono richiesti 'width' e 'height' per ridimensionare l'immagine.")
                new_image = image.resize((width, height))

            elif operation == "rotate":
                angle = kwargs.get("angle")
                if angle is None:
                    raise ValueError("È richiesto 'angle' per ruotare l'immagine.")
                new_image = image.rotate(angle, expand=True)

            elif operation == "add_text":
                text = kwargs.get("text")
                position = kwargs.get("position", (10, 10))  # Posizione predefinita
                font_size = kwargs.get("font_size", 20)
                if not text:
                    raise ValueError("È richiesto 'text' per aggiungere del testo all'immagine.")

                # Aggiungi il testo all'immagine
                draw = ImageDraw.Draw(image)
                try:
                    font = ImageFont.truetype("arial.ttf", font_size)
                except IOError:
                    font = ImageFont.load_default()
                draw.text(position, text, fill="white", font=font)
                new_image = image

            else:
                raise ValueError(f"Operazione non supportata: {operation}")

            # Salva l'immagine modificata
            modified_file_path = os.path.join(self.storage_path, f"edited_{os.path.basename(file_path)}")
            new_image.save(modified_file_path)
            return {"message": "Modifica completata", "modified_image_path": modified_file_path}

        except FileNotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Errore durante la modifica dell'immagine: {str(e)}")
