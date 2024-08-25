import requests
import config

class ConvertTextAduioAPI:
    
    def __init__(self, text, filename) -> None:
        self.URL = "http://api.voicerss.org"

        self.API_KEY = config.API_KEY
        self.LENGUAJE = 'es-es'
        self.text = text
        self.filename=f'{filename}.mp3'
    
    def convert_audio(self):
        parameters = {
    'key': self.API_KEY,
    'hl': self.LENGUAJE,
    'src': self.text,
    'r': '0',
    'c': 'mp3',
    'f': '44khz_16bit_stereo'
}

        response=requests.get(url=self.URL, params=parameters)
        response.raise_for_status()

        #Guarda el audio en un archivo .mp3
        with open(self.filename, 'wb') as audio_file:
            audio_file.write(response.content)
            
        print(f"Audio guardado en {self.filename}")
