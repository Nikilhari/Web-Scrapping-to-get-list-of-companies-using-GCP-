from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
base_url = 'https://www.employbl.com/company-collections/google-cloud-platform'
html_text = requests.get(base_url).text
soup = BeautifulSoup(html_text, 'lxml')
total_area = soup.find('div', class_='mx-auto max-w-7xl items-center')
company_names = total_area.find_all('a', class_='underline hover:text-tangelo')
wb = Workbook()
ws = wb.active
ws.title = "Companies_and_Links"
# Write headers to the Excel sheet
ws.append(["Company Name", "Link"])

for company_name in company_names:
    company_name_text = company_name.text.strip()
    full_url = 'https://www.employbl.com' + company_name.get('href')

    url = requests.get(full_url).text
    new_soup = BeautifulSoup(url, 'lxml')

    target = new_soup.find('a',
                           class_='flex items-center justify-center text-base font-medium text-indigo-600 sm:justify-start')
    if target:
        href_value = target.get('href').replace("//", "")
        ws.append([company_name_text, href_value])

# Save the workbook to a file
wb.save("companies_and_links.xlsx")
