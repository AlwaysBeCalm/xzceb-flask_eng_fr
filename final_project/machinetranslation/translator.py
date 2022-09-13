import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ.get('apikey')
url = os.environ.get('url')

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """Method to translate from English to French"""

    if not english_text:
        return "you must enter English text to translate"

    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    translations = translation.get('translations')
    french_text = translations[0].get('translation')
    return french_text


def french_to_english(french_text):
    """Method to translate from French to English"""

    if not french_text:
        return "you must enter French text to translate"

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    translations = translation.get('translations')
    english_text = translations[0].get('translation')
    return english_text
