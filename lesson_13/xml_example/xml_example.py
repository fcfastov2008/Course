import xml.etree.ElementTree as ET
import logging

# Налаштовуємо логер
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



def find_incoming_by_number(file_path, number):
    tree = ET.parse(file_path)
    root = tree.getroot()


    for group in root.findall('group'):
        group_number = group.find('number')


        if group_number is not None and group_number.text == str(number):
            timing_exbytes = group.find('timingExbytes')


            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')

                if incoming is not None:
                    logger.info(f"incoming: {incoming.text}")
                    return incoming.text

    logger.info("Значення не знайдено")
    return None


find_incoming_by_number('groups.xml',2)