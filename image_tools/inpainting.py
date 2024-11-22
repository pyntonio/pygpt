import openai

class Inpainting:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = self.api_key

    def inpaint_image(self, image_url: str, mask_url: str, description: str):
        """
        Applica modifiche specifiche a un'immagine esistente.
        :param image_url: URL dell'immagine da modificare.
        :param mask_url: URL della maschera da applicare all'immagine.
        :param description: Descrizione della modifica da apportare.
        :return: URL dell'immagine modificata.
        """
        response = openai.Image.create(
            prompt=description,
            n=1,
            size="1024x1024",
            image=image_url,
            mask=mask_url
        )
        
        return {"modified_image_url": response['data'][0]['url']}
