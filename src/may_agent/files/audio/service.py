import speech_recognition as sr
from typing import Union

def transcribe_audio(audio_file: Union[str, bytes]) -> str:
    """
    Transcribes an audio file to text using Google's Speech Recognition API.

    Args:
        audio_file (Union[str, bytes]): Path to the audio file or file-like object.

    Returns:
        str: Transcribed text from the audio.

    Raises:
        ValueError: If the audio file is invalid or cannot be processed.
        sr.RequestError: If there is an issue with the API request.
        sr.UnknownValueError: If the speech is unintelligible.
    """
    r = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
            return r.recognize_google(audio)
    except FileNotFoundError:
        raise ValueError("The specified audio file was not found.")
    except sr.RequestError as e:
        raise RuntimeError(f"API request failed: {e}")
    except sr.UnknownValueError:
        raise ValueError("Unable to recognize speech in the audio file.")
