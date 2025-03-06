from voice_engine import VoiceEngine
from command_handler import CommandHandler
import logging
import time

class AntaraAssistant:
    def __init__(self):
        self.voice = VoiceEngine()
        self.handler = CommandHandler()
        self._configure_logging()

    def _configure_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("antara.log"),
                logging.StreamHandler()
            ]
        )

    def _welcome_sequence(self):
        """Initial startup sequence"""
        self.voice.speak("Initializing Antara Voice Assistant systems")
        time.sleep(0.5)
        self.voice.speak("All systems nominal")
        time.sleep(0.3)
        self.voice.speak("Hello! I'm Antara, your personal AI assistant")

    def run(self):
        """Main interaction loop"""
        self._welcome_sequence()
        
        while True:
            try:
                command = self.voice.listen()
                if not command:
                    continue
                
                logging.info(f"User command: {command}")
                
                if "exit" in command or "quit" in command:
                    self.voice.speak("Shutting down systems. Goodbye!")
                    break
                
                response = self.handler.process_command(command)
                if response:
                    logging.info(f"Antara response: {response}")
                    self.voice.speak(response)
                    
            except KeyboardInterrupt:
                self.voice.speak("Emergency shutdown initiated")
                break
            except Exception as e:
                logging.error(f"Critical error: {str(e)}")
                self.voice.speak("I encountered an error. Rebooting systems")
                time.sleep(1)

if __name__ == "__main__":
    assistant = AntaraAssistant()
    assistant.run()
