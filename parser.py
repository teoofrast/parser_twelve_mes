from bs4 import BeautifulSoup

for i in range(1, 17):
    # Функция для парсинга одной страницы
    with open(f'vodoemulsii_semey_{i}.html', "r", encoding="utf-8") as file:
        content = file.read()

    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(content, "html.parser")

    # Извлекаем название позиции
    positions = soup.find_all('div', class_='products-view-item text-static cs-br-1 js-products-view-item')

    for position in positions:
        # name = position.find('div', class_='products-view-name products-view-name-default').text.strip()
        # print(name)
        # price = position.find('div', class_='price').text.strip()
        # print(price)
        link = position.find('a')['href']
        print(link)
