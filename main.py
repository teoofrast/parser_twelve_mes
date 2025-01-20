import requests

cookies = {
    'zonePopoverVisible': 'false',
    's': '41q0xtp14cvl05haiavies0i',
    'customer': 'fdb1762e-9c35-40bc-896c-44b7b9f9376f',
    'advs': '%7b%22d%22%3a%222025-01-20T08%3a20%3a02.3184448%2b05%3a00%22%2c%22u%22%3a%22https%3a%2f%2f12.kz%2f%22%2c%22h%22%3a%220acf0f5b68cf118b8da495630e9c0576%22%2c%22i%22%3a%2295.141.143.46%22%7d',
    'f': 'o1Hs4Dn0JBLhsfIKIUceWQXOlo9z5Eaw5qQC7QZedPDim74aCEsQoAcaQ5U9AZaZmlm9WFRU7VutIsfAWxZkhNN07nA1',
    'Currency': 'KZT',
    'ipzone': '83%3b209%3b17422%3b%d0%92%d0%be%d1%81%d1%82%d0%be%d1%87%d0%bd%d0%be-%d0%9a%d0%b0%d0%b7%d0%b0%d1%85%d1%81%d1%82%d0%b0%d0%bd%d1%81%d0%ba%d0%b0%d1%8f+%d0%be%d0%b1%d0%bb%d0%b0%d1%81%d1%82%d1%8c%3b%d0%a1%d0%b5%d0%bc%d0%b5%d0%b9%3b%3b',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'ru-RU,ru;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'zonePopoverVisible=false; s=41q0xtp14cvl05haiavies0i; customer=fdb1762e-9c35-40bc-896c-44b7b9f9376f; advs=%7b%22d%22%3a%222025-01-20T08%3a20%3a02.3184448%2b05%3a00%22%2c%22u%22%3a%22https%3a%2f%2f12.kz%2f%22%2c%22h%22%3a%220acf0f5b68cf118b8da495630e9c0576%22%2c%22i%22%3a%2295.141.143.46%22%7d; f=o1Hs4Dn0JBLhsfIKIUceWQXOlo9z5Eaw5qQC7QZedPDim74aCEsQoAcaQ5U9AZaZmlm9WFRU7VutIsfAWxZkhNN07nA1; Currency=KZT; ipzone=83%3b209%3b17422%3b%d0%92%d0%be%d1%81%d1%82%d0%be%d1%87%d0%bd%d0%be-%d0%9a%d0%b0%d0%b7%d0%b0%d1%85%d1%81%d1%82%d0%b0%d0%bd%d1%81%d0%ba%d0%b0%d1%8f+%d0%be%d0%b1%d0%bb%d0%b0%d1%81%d1%82%d1%8c%3b%d0%a1%d0%b5%d0%bc%d0%b5%d0%b9%3b%3b',
    'priority': 'u=0, i',
    'referer': 'https://12.kz/categories/vodoemulsii',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Brave";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}


# URL страницы
url = 'https://12.kz/categories/vodoemulsii'

# Цикл от 1 до 16
for page in range(1, 17):
    params = {'page': str(page)}  # Изменяем параметр page
    try:
        # Выполняем запрос
        response = requests.get(url, params=params, cookies=cookies, headers=headers)
        response.raise_for_status()  # Проверяем на ошибки

        # Сохраняем HTML в файл
        file_name = f"vodoemulsii_semey_{page}.html"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"Страница {page} успешно сохранена в файл '{file_name}'")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке страницы {page}: {e}")
