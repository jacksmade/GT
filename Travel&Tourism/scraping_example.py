# from bs4 import BeautifulSoup
# from selenium import webdriver
# import math
# import time

# def AutoScroll(driver):
#     z = 1000
#     previous_height = -math.inf
#     while True:
#         z += 1000
#         current_height = driver.execute_script("return document.documentElement.scrollHeight")
#         if current_height == previous_height:
#             break
#         previous_height = current_height
#         scroll = "window.scrollTo(0," + str(z) + ")"
#         driver.execute_script(scroll)
#         time.sleep(5)
#         z += 1000




# if __name__ == "__main__":
#     chrome_driver_path = 'C:/Users/WB/Downloads/chromedriver-114.0.5735.90-installer_2w-62V1.exe'

#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')  # Optional: run Chrome in headless mode
#     driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


#     urls =['https://www.tripadvisor.com/Attractions-g187768-Activities-Madrid.html',
#         'https://www.tripadvisor.com/Attractions-g187791-Activities-Barcelona_Catalonia.html',
#         'https://www.tripadvisor.com/Attractions-g293983-Activities-Dubai_Emirate_of_Dubai.html',
#         'https://www.tripadvisor.com/Attractions-g187147-Activities-Paris_Ile_de_France.html',
#         'https://www.tripadvisor.com/Attractions-g186338-Activities-London_England.html',
#         'https://www.tripadvisor.com/Attractions-g187497-Activities-Rome_Lazio.html',
#         'https://www.tripadvisor.com/Attractions-g274887-Activities-Prague_Bohemia.html',
#         'https://www.tripadvisor.com/Attractions-g187323-Activities-Berlin.html',
#         'https://www.tripadvisor.com/Attractions-g187497-Activities-Vatican_City_Lazio.html',
#         'https://www.tripadvisor.com/Attractions-g187275-Activities-Amsterdam_North_Holland_Province.html',
#         'https://www.tripadvisor.com/Attractions-g187331-Activities-Vienna.html',
#         'https://www.tripadvisor.com/Attractions-g187497-Activities-Sicily.html',
#         'https://www.tripadvisor.com/Attractions-g274707-Activities-Budapest_Central_Hungary.html',
#         'https://www.tripadvisor.com/Attractions-g187497-Activities-Sardinia.html',
#         'https://www.tripadvisor.com/Attractions-g274856-Activities-Warsaw_Mazovia_Province_Central_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274707-Activities-Budapest_Central_Hungary.html',
#         'https://www.tripadvisor.com/Attractions-g187497-Activities-Sardinia.html',
#         'https://www.tripadvisor.com/Attractions-g274856-Activities-Warsaw_Mazovia_Province_Central_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274872-Activities-Cracow_Lesser_Poland_Province_Southern_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274707-Activities-Budapest_Central_Hungary.html',
#         'https://www.tripadvisor.com/Attractions-g187497-Activities-Sardinia.html',
#         'https://www.tripadvisor.com/Attractions-g274856-Activities-Warsaw_Mazovia_Province_Central_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274872-Activities-Cracow_Lesser_Poland_Province_Southern_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274707-Activities-Budapest_Central_Hungary.html',
#         'https://www.tripadvisor.com/Attractions-g187497-Activities-Sardinia.html',
#         'https://www.tripadvisor.com/Attractions-g274856-Activities-Warsaw_Mazovia_Province_Central_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274872-Activities-Cracow_Lesser_Poland_Province_Southern_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274707-Activities-Budapest_Central_Hungary.html',
#         'https://www.tripadvisor.com/Attractions-g187497-Activities-Sardinia.html',
#         'https://www.tripadvisor.com/Attractions-g274856-Activities-Warsaw_Mazovia_Province_Central_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274872-Activities-Cracow_Lesser_Poland_Province_Southern_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274707-Activities-Budapest_Central_Hungary.html',
#         'https://www.tripadvisor.com/Attractions-g187497-Activities-Sardinia.html',
#         'https://www.tripadvisor.com/Attractions-g274856-Activities-Warsaw_Mazovia_Province_Central_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274872-Activities-Cracow_Lesser_Poland_Province_Southern_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274707-Activities-Budapest_Central_Hungary.html',
#         'https://www.tripadvisor.com/Attractions-g187497-Activities-Sardinia.html',
#         'https://www.tripadvisor.com/Attractions-g274856-Activities-Warsaw_Mazovia_Province_Central_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274872-Activities-Cracow_Lesser_Poland_Province_Southern_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274707-Activities-Budapest_Central_Hungary.html',
#         'https://www.tripadvisor.com/Attractions-g187497-Activities-Sardinia.html',
#         'https://www.tripadvisor.com/Attractions-g274856-Activities-Warsaw_Mazovia_Province_Central_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274872-Activities-Cracow_Lesser_Poland_Province_Southern_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274707-Activities-Budapest_Central_Hungary.html',
#         'https://www.tripadvisor.com/Attractions-g187497-Activities-Sardinia.html',
#         'https://www.tripadvisor.com/Attractions-g274856-Activities-Warsaw_Mazovia_Province_Central_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274872-Activities-Cracow_Lesser_Poland_Province_Southern_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274707-Activities-Budapest_Central_Hungary.html',
#         'https://www.tripadvisor.com/Attractions-g187497-Activities-Sardinia.html',
#         'https://www.tripadvisor.com/Attractions-g274856-Activities-Warsaw_Mazovia_Province_Central_Poland.html',
#         'https://www.tripadvisor.com/Attractions-g274872-Activities-Cracow_Lesser_Poland_Province_Southern_Poland.html'
#             ]
#     for index, url in enumerate(urls):
#         driver.get(url)
#         AutoScroll(driver)

#         content = driver.page_source
#         soup = BeautifulSoup(content, "html.parser")
#         titles = soup.find_all('a', class_='attraction_element_title')
#         titles_text = [title.text.strip() for title in titles]

#         filename = f"tour_travel_data_{index}.txt"
#         with open(filename, "w", encoding="utf-8") as txtfile:
#             for title in titles_text:
#                 txtfile.write(title + "\n")

#         print("Titles scraped from", url, "saved to", filename)

#     driver.quit()
