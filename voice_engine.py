import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import os
import logging

class VoiceEngine:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 400
        self.recognizer.pause_threshold = 0.8
        self._configure_voices()
        self.logger = logging.getLogger("AntaraVoice")

    def _configure_voices(self):
        """Configure both online and offline TTS engines"""
        # Online configuration
        self.tts_config = {
            'lang': 'en',
            'tld': 'co.uk',  # British English female
            'slow': False
        }
        
        # Offline configuration
        self.offline_engine = pyttsx3.init()
        voices = self.offline_engine.getProperty('voices')
        self.offline_engine.setProperty('voice', voices[1].id)  # Female voice

    def speak(self, text: str, use_online: bool = True):
        """Convert text to speech with fallback to offline engine"""
        try:
            if use_online:
                tts = gTTS(text=text, **self.tts_config)
                tts.save("response.mp3")
                os.system("mpg123 response.mp3")
                os.remove("response.mp3")
            else:
                self.offline_engine.say(text)
                self.offline_engine.runAndWait()
                
        except Exception as e:
            self.logger.error(f"Voice synthesis failed: {str(e)}")
            self.offline_engine.say(text)
            self.offline_engine.runAndWait()

    def listen(self) -> str:
        """Advanced voice recognition with noise handling"""
        with sr.Microphone() as source:
            try:
                self.logger.info("Calibrating ambient noise...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                self.logger.info("Listening for command...")
                audio = self.recognizer.listen(source, timeout=7)
                return self.recognizer.recognize_google(audio).lower()
                
            except sr.UnknownValueError:
                self.logger.warning("Could not understand audio")
                return ""
            except sr.RequestError as e:
                self.logger.error(f"API error: {str(e)}")
                return ""
            except Exception as e:
                self.logger.error(f"Recognition error: {str(e)}")
                return ""
