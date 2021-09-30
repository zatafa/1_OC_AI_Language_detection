# -*- coding: utf-8 -*-

# Text to be tested
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# french "L'alimentation industrielle convient parfaitement à la croissance du chiot et à l'adulte."
# russian "Занимает пятое место в диптихе автокефальных поместных церквей мира."
# english "He was a economics graduate from Elphinstone College, Mumbai. He was an industrialist in plastics business."
# spanish "Barilla est un'impresa murtinassionale italiana de su setore alimentàriu, lìdera mundiale in su mercadu de sos macarrones sicos, de sos sutzos prontos in Europa."
# indonesian "Kemunculan pertamanya adalah ketika mencium kakak kelasnya, Kyoko. Sejak Yuuki meminta agar Sakura merahasiakan hal tersebutlah keduanya menjadi akrab."
# chinese "胡赛尼本人和小说的主人公阿米尔一样，都是出生在阿富汗首都喀布尔，少年时代便离开了这个国家。胡赛尼直到2003年小说出版之后才首次回到已经离开27年的祖国。他在苏联入侵时离开了阿富汗"
# arabic "قبل عام بالضبط وبتاريخ 21/7/2012 أعلن البغدادي خطة هدم الأسوار وبتاريخ 21/7/2013"


# Import libraries
import os, requests, json


# Load API credentials (environment variables)
endpoint = os.environ["TEXT_ANALYTICS_ENDPOINT"]
subscription_key = os.environ["TEXT_ANALYTICS_SUBSCRIPTION_KEY"]

# Prepare request URL and headers
path = "/text/analytics/v2.1/languages"
detect_api_url = endpoint + path

headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Ocp-Apim-Subscription-Region": "westeurope",
    "Content-type": "application/json"}

# Set text body
text_body = {"documents": 
    [
        {"id":"1",
        "text": "胡赛尼本人和小说的主人公阿米尔一样，都是出生在阿富汗首都喀布尔，少年时代便离开了这个国家。胡赛尼直到2003年小说出版之后才首次回到已经离开27年的祖国。他在苏联入侵时离开了阿富汗"}
    ]
}

# Call POST request
response = requests.post(detect_api_url, headers=headers, json=text_body)
detected_language = response.json()

# Display the detected language and its confidence score (highest probability)
print(json.dumps(
    detected_language, 
    sort_keys=False, 
    indent=4, 
    ensure_ascii=False, 
    separators=(",", ": ")))