import telebot
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 " \
             "Safari/537.36 "
# US english
LANGUAGE = "ru-RU,ru;q=0.5"
now1 = datetime.now()
t = now1.strftime("%H:%M")

bot = telebot.TeleBot('5634867467:AAHl2DC6VAf5jJT1QPDjEhlCR2ZGqFj1B1I')


def get_weather_data(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")
    result = {'region': soup.find("div", attrs={"id": "wob_loc"}).text,
              'temp_now': soup.find("span", attrs={"id": "wob_tm"}).text,
              # 'temperature_feels': soup.find("div", {"class": "iajBOd"}).text,
              'dayhour': soup.find("div", attrs={"id": "wob_dts"}).text,
              'weather_now': soup.find("span", attrs={"id": "wob_dc"}).text,
              'precipitation': soup.find("span", attrs={"id": "wob_pp"}).text,
              'humidity': soup.find("span", attrs={"id": "wob_hm"}).text,
              'wind': soup.find("span", attrs={"id": "wob_ws"}).text}

    next_days = []
    days = soup.find("div", attrs={"id": "wob_dp"})
    for day in days.findAll("div", attrs={"class": "wob_df"}):
        # نام روز را استخراج می کند
        day_name = day.findAll("div")[0].attrs['aria-label']
        # وضعیت آب و هوای آن روز را دریافت کنید
        weather = day.find("img").attrs["alt"]
        temp = day.findAll("span", {"class": "wob_t"})
        # maximum temparature in Celsius, use temp[1].text if you want fahrenheit
        max_temp = temp[0].text
        # minimum temparature in Celsius, use temp[3].text if you want fahrenheit
        min_temp = temp[2].text
        next_days.append({"name": day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
    # append to result
    result['next_days'] = next_days
    return result


city = input("Укажите свой город : ")

if __name__ == "__main__":
    URL = f"https://www.google.ru/search?q=weather+{city}"
    # import argparse
    #
    # parser = argparse.ArgumentParser(description="Quick Script for Extracting Weather data using Google Weather")
    # parser.add_argument("region", nargs="?", help="""Region to get weather for, must be available region.
    #                                     Default is your current location determined by your IP Address""", default="")
    # # parse arguments
    # args = parser.parse_args()
    # region = args.region
    # if region:
    #     region = region.replace(" ", "+")
    #     URL += f"+{region}"
    # get data
    data = get_weather_data(URL)
    # print data
    text = f"Погода в городе {data['region']}\n" \
           f"Сейчас: {t}\n" \
           f"Температура сейчас: {data['temp_now']}°C\n" \
           f"Описание: {data['weather_now']}\n" \
           f"осадки {data['precipitation']}\n" \
           f"Влажность: {data['humidity']}\n" \
           f"Ветер: {data['wind']}\n" \
           f"Следующие дни:" \
 \
    # print(text)
    text2 = ""
    for dayweather in data["next_days"]:

        text2 = text2 + f"{'+-' * 4} {dayweather['name']} {'-+' * 4} \n" \
                        f"Максимальная температура: {dayweather['max_temp']}°C\n" \
                        f"Минимальная температура: {dayweather['min_temp']}°C\n"

    # print(text2)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['tomorrow'])
def tomorrow(message):
    bot.send_message(message.chat.id, text2)


bot.polling(none_stop=True)
