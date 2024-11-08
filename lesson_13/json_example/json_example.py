import json
import logging


logging.basicConfig(filename='json__result.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


file_paths = ['swagger.json', 'localizations_ru.json', 'localizations_en.json','login.json']

def validate_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
        print(f"{file_path} - Валідний JSON")
    except json.JSONDecodeError as e:
        logger.error(f"{file_path} - Невалідний JSON: {e}")
        print(f"{file_path} - Невалідний JSON")


for file_path in file_paths:
    validate_json(file_path)