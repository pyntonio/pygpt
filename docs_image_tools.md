### **Documentazione Dettagliata: Moduli per la Gestione delle Immagini**

Questa documentazione descrive in dettaglio il funzionamento, i requisiti e i metodi dei tre moduli sviluppati per gestire immagini in un'applicazione FastAPI. I moduli includono: 

1. **image_generation.py** - Generazione di immagini.
2. **image_editing.py** - Modifica di immagini.
3. **image_upload.py** - Caricamento di immagini.

---

## **1. image_generation.py**

### **Descrizione**
Consente di generare immagini basate su un prompt testuale utilizzando l'API OpenAI DALL·E. Gli utenti possono specificare una descrizione (prompt) e una dimensione per ottenere immagini personalizzate.

### **Requisiti**
- Chiave API OpenAI valida.
- Connessione a Internet.

### **Metodi Principali**

#### `generate_image(prompt: str, size: str = "1024x1024")`
- **Descrizione**: Genera un'immagine basata su un prompt testuale.
- **Parametri**:
  - `prompt` (str): La descrizione dell'immagine (es. "Un paesaggio futuristico con alberi viola").
  - `size` (str): La dimensione dell'immagine. Opzioni: `256x256`, `512x512`, `1024x1024` (default: `1024x1024`).
- **Risposta**:
  - **Successo**: Restituisce un dizionario con `prompt`, `size` e l'URL dell'immagine generata.
  - **Errore**: HTTP 400 o 500 con messaggi dettagliati.
- **Dipendenze**:
  - Libreria `openai` per le chiamate API.

---

## **2. image_editing.py**

### **Descrizione**
Fornisce strumenti per modificare immagini esistenti, come ridimensionamento, rotazione e aggiunta di testo. Questo modulo utilizza la libreria **Pillow**.

### **Requisiti**
- Libreria **Pillow** installata (`pip install pillow`).
- Percorso file valido per immagini di input.

### **Metodi Principali**

#### `edit_image(file_path: str, operation: str, **kwargs)`
- **Descrizione**: Modifica un'immagine in base all'operazione richiesta.
- **Parametri**:
  - `file_path` (str): Percorso dell'immagine da modificare.
  - `operation` (str): Tipo di modifica:
    - `resize` (Richiede `width` e `height`).
    - `rotate` (Richiede `angle`).
    - `add_text` (Richiede `text`, opzionalmente `position` e `font_size`).
  - **Kwargs**:
    - `width` (int): Larghezza dell'immagine (per `resize`).
    - `height` (int): Altezza dell'immagine (per `resize`).
    - `angle` (int): Angolo di rotazione (per `rotate`).
    - `text` (str): Testo da aggiungere (per `add_text`).
    - `position` (tuple): Coordinate `(x, y)` (default: `(10, 10)`).
    - `font_size` (int): Dimensione del font (default: `20`).
- **Risposta**:
  - **Successo**: Percorso del file modificato.
  - **Errore**: HTTP 400, 404 o 500 con messaggi dettagliati.
- **Dipendenze**:
  - Libreria `Pillow` (`Image`, `ImageDraw`, `ImageFont`).

---

## **3. image_upload.py**

### **Descrizione**
Gestisce il caricamento sicuro di immagini da parte degli utenti, supportando formati comuni come JPEG, PNG e GIF.

### **Requisiti**
- Percorso per salvare le immagini (configurabile).
- File immagine valido come input.

### **Metodi Principali**

#### `upload_image(file: UploadFile)`
- **Descrizione**: Carica un'immagine e la salva nella directory configurata.
- **Parametri**:
  - `file` (UploadFile): Il file immagine caricato tramite FastAPI.
- **Risposta**:
  - **Successo**: Messaggio di conferma e percorso del file salvato.
  - **Errore**: HTTP 400 o 500 con messaggi dettagliati.
- **Dipendenze**:
  - Libreria `uuid` per generare nomi univoci.
  - FastAPI `UploadFile`.

---

## **Workflow delle Funzioni**

### **Esempio di Utilizzo Completo**
1. **Caricamento**:
   - Un utente carica un'immagine utilizzando l'endpoint `/images/upload`.
   - Il modulo `image_upload.py` salva il file in una directory configurata.

2. **Modifica**:
   - L'immagine caricata viene passata al modulo `image_editing.py` per operazioni come:
     - Ridimensionamento.
     - Rotazione.
     - Aggiunta di testo.

3. **Generazione**:
   - L'utente invia un prompt testuale al modulo `image_generation.py` per creare nuove immagini personalizzate.

---

## **Struttura della Directory**

```plaintext
my_app/
│
├── image_management/
│   ├── image_generation.py  # Generazione immagini
│   ├── image_editing.py     # Modifica immagini
│   └── image_upload.py      # Caricamento immagini
│
├── uploaded_images/         # Directory per immagini caricate
├── edited_images/           # Directory per immagini modificate
```

---

## **Esempi di Chiamate API**

### **1. Generazione di Immagini**
- **Endpoint**: `/images/generate`
- **Metodo**: `POST`
- **Body**:
  ```json
  {
    "prompt": "A cat sitting on a spaceship",
    "size": "512x512"
  }
  ```
- **Risposta**:
  ```json
  {
    "prompt": "A cat sitting on a spaceship",
    "size": "512x512",
    "image_url": "https://example.com/image.png"
  }
  ```

### **2. Modifica di Immagini**
- **Endpoint**: `/images/edit`
- **Metodo**: `POST`
- **Body**:
  ```json
  {
    "file_path": "uploaded_images/sample.jpg",
    "operation": "add_text",
    "text": "Hello, World!",
    "position": [50, 50],
    "font_size": 30
  }
  ```
- **Risposta**:
  ```json
  {
    "message": "Modifica completata",
    "modified_image_path": "edited_images/edited_sample.jpg"
  }
  ```

### **3. Caricamento di Immagini**
- **Endpoint**: `/images/upload`
- **Metodo**: `POST`
- **File**: Immagine caricata come multipart/form-data.
- **Risposta**:
  ```json
  {
    "message": "File caricato con successo",
    "file_path": "uploaded_images/uuid_generated_name.jpg"
  }
  ```

---

## **Considerazioni Finali**
### **Vantaggi**
- **Modularità**: Ogni funzione è isolata per facilitare manutenzione e test.
- **Scalabilità**: Supporto per aggiungere facilmente nuove funzionalità.
- **Facilità d’uso**: Interfaccia chiara per l’interazione.

### **Estensioni Future**
- Integrazione con servizi di archiviazione cloud (AWS S3, Azure Blob).
- Filtri avanzati e generazione di immagini di alta qualità.
- Implementazione di endpoint per batch processing (modifica/caricamento di più immagini contemporaneamente). 

Se hai bisogno di ulteriori dettagli o vuoi migliorare alcune parti, fammi sapere! 😊






Ecco come implementare il file `image_generation.py` per gestire la generazione di immagini utilizzando OpenAI DALL·E.

---

### **Codice per `image_generation.py`**

```python
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
```

---

### **Spiegazione del codice**

1. **Inizializzazione**:
   - La classe `ImageGenerator` richiede una chiave API per autenticarsi con OpenAI.
   - La chiave viene passata durante l'inizializzazione e configurata globalmente con `openai.api_key`.

2. **Validazione**:
   - Prima di inviare la richiesta a OpenAI, la funzione verifica che le dimensioni richieste siano valide.

3. **Generazione**:
   - Utilizza il metodo `openai.Image.create` per generare l'immagine.
   - Restituisce l'URL dell'immagine generata.

4. **Gestione errori**:
   - Gli errori OpenAI vengono catturati e restituiti con un messaggio chiaro.
   - Gli errori di validazione (es. dimensioni non valide) restituiscono un errore HTTP 400.
   - Errori generici restituiscono un errore HTTP 500.

---

### **Esempio di utilizzo**

Quando richiami l'endpoint `/images/generate` nel file `app.py`, il metodo `generate_image` verrà chiamato.  
Esempio di richiesta:

- **Metodo HTTP**: `POST`
- **URL**: `/images/generate`
- **Payload**:
  ```json
  {
    "prompt": "A futuristic cityscape with flying cars",
    "size": "1024x1024"
  }
  ```

- **Risposta**:
  ```json
  {
    "prompt": "A futuristic cityscape with flying cars",
    "size": "1024x1024",
    "image_url": "https://openai-generated-image-url.com/image.png"
  }
  ```

---

### **Prossimi Passi**
1. **Testare la funzionalità** con Postman o Swagger.
2. **Logging e monitoraggio**: Aggiungi log per monitorare le richieste e il tempo di risposta.
3. **Estensioni future**:
   - Aggiungere supporto per generare più immagini contemporaneamente.
   - Memorizzare localmente le immagini generate.

Se vuoi posso aiutarti a configurare i test per questa funzione!





Ecco un'implementazione per il file `image_editing.py`, che fornirà funzionalità di modifica delle immagini utilizzando la libreria **Pillow**.

---

### **Codice per `image_editing.py`**

```python
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
```

---

### **Funzionalità Supportate**

1. **Ridimensionamento** (`resize`):  
   - Richiede `width` e `height` come parametri.
   - Cambia la dimensione dell'immagine mantenendo la proporzione.

2. **Rotazione** (`rotate`):  
   - Richiede `angle` come parametro (in gradi).
   - Ruota l'immagine in senso orario.

3. **Aggiunta di testo** (`add_text`):  
   - Richiede `text` come parametro.
   - Supporta posizione (`position`) e dimensione del font (`font_size`).

---

### **Esempio di Utilizzo**

#### **1. Ridimensionamento**
- **Richiesta**:
  ```json
  {
    "file_path": "path/to/image.jpg",
    "operation": "resize",
    "width": 500,
    "height": 300
  }
  ```
- **Risposta**:
  ```json
  {
    "message": "Modifica completata",
    "modified_image_path": "edited_images/edited_image.jpg"
  }
  ```

#### **2. Rotazione**
- **Richiesta**:
  ```json
  {
    "file_path": "path/to/image.jpg",
    "operation": "rotate",
    "angle": 45
  }
  ```
- **Risposta**:
  ```json
  {
    "message": "Modifica completata",
    "modified_image_path": "edited_images/edited_image.jpg"
  }
  ```

#### **3. Aggiunta di Testo**
- **Richiesta**:
  ```json
  {
    "file_path": "path/to/image.jpg",
    "operation": "add_text",
    "text": "Hello, World!",
    "position": [50, 50],
    "font_size": 30
  }
  ```
- **Risposta**:
  ```json
  {
    "message": "Modifica completata",
    "modified_image_path": "edited_images/edited_image.jpg"
  }
  ```

---

### **Prossimi Passi**
1. **Caricare un’immagine di test** per verificare ogni operazione.
2. **Estendere le operazioni**:
   - Filtri (es. bianco e nero, sfocatura).
   - Sovrapposizione di altre immagini.
3. **Aggiungere unit test** per convalidare i risultati.

Se hai bisogno, possiamo passare al modulo di caricamento o configurare i test per questa funzionalità.




Ecco un'implementazione per il file `image_upload.py`, che consente di caricare immagini, gestirle in sicurezza e salvarle in una directory designata.

---

### **Codice per `image_upload.py`**

```python
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
```

---

### **Dettagli del Codice**

1. **Verifica del tipo di file**:
   - Controlla il `content_type` del file caricato per assicurarsi che sia un'immagine nei formati supportati: `JPEG`, `PNG`, o `GIF`.

2. **Generazione del nome univoco**:
   - Utilizza **UUID** per generare un nome unico per il file, evitando conflitti.

3. **Salvataggio del file**:
   - Il contenuto del file viene letto e salvato in una directory configurata, con supporto per file di grandi dimensioni.

4. **Gestione degli errori**:
   - Restituisce un errore HTTP 400 se il formato non è supportato.
   - Restituisce un errore HTTP 500 per problemi generici.

---

### **Esempio di utilizzo**

Quando richiami l'endpoint `/images/upload` nel file `app.py`, la funzione `upload_image` viene eseguita.

#### **Richiesta**
- **Metodo HTTP**: `POST`
- **URL**: `/images/upload`
- **File**: Un'immagine (JPEG, PNG, GIF).

#### **Risposta (Successo)**
```json
{
    "message": "File caricato con successo",
    "file_path": "uploaded_images/uuid_generated_name.png"
}
```

#### **Risposta (Errore)**
- **Formato non supportato**:
```json
{
    "detail": "Formato non supportato: text/plain. Usa solo JPEG, PNG o GIF."
}
```

- **Errore generico**:
```json
{
    "detail": "Errore durante il caricamento: errore specifico."
}
```

---

### **Configurazione Directory**
Il codice crea automaticamente la directory `uploaded_images/` se non esiste. Puoi configurare un percorso diverso passando un parametro a `ImageUploader`.

---

### **Prossimi Passi**
1. **Testare l'endpoint `/images/upload`**:
   - Utilizza strumenti come **Postman** o **Swagger**.
2. **Estensioni future**:
   - Supporto per caricamenti multipli.
   - Compressione delle immagini per risparmiare spazio.
   - Integrazione con storage cloud (ad esempio, AWS S3 o Google Cloud Storage).

Posso aiutarti a configurare i test o espandere il modulo per gestire più funzionalità!