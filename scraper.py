import requests
from bs4 import BeautifulSoup

print('Hello')

url = 'https://www.toyota.bg/retailer-group/tm-auto/used-cars?location=dealerGroupId:00CDA-D3134-4FC3C-7B800-01360-1&brands=38&model=RA'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    cars = soup.find_all('article')

    cars_len = len(cars)
    print(f'Cars len is: {cars_len}')

    for car in cars:
          # Extract image URL
        image_tag = car.find('img', class_='ResultImageStyles__Image-sc-o1b61d-0')
        image_url = image_tag['src'] if image_tag else 'No image found'

        # Extract price
        price_tag = car.find('span', class_='CarResultPriceStyles__PriceCollection-sc-16sb9k5-0')
        price = price_tag.get_text(strip=True) if price_tag else 'No price found'

        # Extract year
        year_tag = car.find('div', class_='UsedCarResultStyles__SpecValue-sc-xeiqrk-11')
        year = year_tag.get_text(strip=True) if year_tag else 'No year found'

        # Extract mileage (km)
        mileage_tag = car.find('div', class_='UsedCarResultStyles__SpecValue-sc-xeiqrk-11')
        mileage = mileage_tag.get_text(strip=True) if mileage_tag else 'No mileage found'

        # Print the extracted information
        print(f'Image URL: {image_url}')
        print(f'Price: {price}')
        print(f'Year: {year}')
        print(f'Mileage: {mileage}')
        print('---')
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
