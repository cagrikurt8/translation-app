from azure.cognitiveservices.speech import SpeechConfig, AudioConfig, SpeechSynthesizer, ResultReason
from azure.cognitiveservices.speech.translation import TranslationRecognizer, SpeechTranslationConfig

SPEECH_KEY = "1410a78745054fd2a85ef2a031b02434"
SPEECH_REGION = "westeurope"


class Translator:
    def __init__(self, source_language: str, target_language: str):
        self.source_language = source_language
        self.target_language = target_language

        self.translator = self.get_translator()
        self.synthesizer = self.get_synthesizer()


    def get_translator(self):
        translation_config = SpeechTranslationConfig(SPEECH_KEY, SPEECH_REGION)
        translation_config.speech_recognition_language = self.source_language
        translation_config.add_target_language(self.target_language)
    
        translator = TranslationRecognizer(translation_config)

        return translator
    

    def get_synthesizer(self):
        voices = {"en": "en-GB-LibbyNeural", "ru": "ru-RU-DmitryNeural"}

        audio_config = AudioConfig(use_default_microphone=True)
        speech_config = SpeechConfig(SPEECH_KEY, SPEECH_REGION)
        speech_config.speech_synthesis_voice_name = voices[self.target_language]

        synthesizer = SpeechSynthesizer(speech_config, audio_config)

        return synthesizer
        
    
    def translate(self):
        result = self.translator.recognize_once_async().get()
    
        if result.reason == ResultReason.TranslatedSpeech:
            print(f"Recognized speech: {result.text}")

            translation = result.translations[self.target_language]
            print(translation)
            return translation
        
        return f"Konuşma algılanamadı.\n{result.reason}"
    

    def synthesize(self, text):
        self.synthesizer.speak_text_async(text).get()