import openai

class CreativeComposition:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = self.api_key

    def create_creative_composition(self, description: str):
        """
        Crea una composizione creativa o surreale.
        :param description: Descrizione dell'immagine da generare.
        :return: URL dell'immagine generata.
        """
        response = openai.Image.create(
            prompt=description,
            n=1,
            size="1024x1024"
        )
        
        return {"image_url": response['data'][0]['url']}
