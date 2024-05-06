from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from telegram import Bot
import asyncio
import re
import urllib.parse
import os

TOKEN = '5558634309:AAGC9BY28ru907q3hmhWwdS83F31cIjHuiQ'
chat_ids = ['815189312']

async def send_Error(chat_id, text, error):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=chat_id, text="Hubo un error al obtener los productos: " + str(text) + ". " + str(error))

async def send_message(chat_id, imagen, descripcion, precio_normal, precio_oferta, descuento, enlace):
    urlUnida = "https://guatemaladigital.com" + enlace
    message = f'<b>◄❖🌟【ＰＲＯＤＵＣＴＯ】🌟❖► </b>\n' \
            f'-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶\n' \
            f'<i>{descripcion}</i>\n' \
            f'-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶-̶ \n' \
            f'<b>❌ <s>Antes: Q. {precio_normal}0</s></b>\n ' \
            f'<b>✅  Ahora: Q.{precio_oferta}0  ς(ˆڡˆς) {descuento}% 🏷️ </b>\n' \
            f'-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷  \n' \
            f'<a href="{urlUnida}">   🔗 ɪʀ ᴀ ᴠᴇʀ ᴇʟ ᴘʀᴏᴅᴜᴄᴛᴏ 🔗</a>' \
            f'-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷  \nㅤ　'

    bot = Bot(token=TOKEN)
    await bot.send_photo(chat_id=chat_id, photo=imagen, caption=message, parse_mode='HTML')

async def ejecutar_codigo(chat_id):
    driver = None

    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        chrome_driver_path = os.path.join(current_directory, 'libs', 'chrome-win64', 'chrome.exe')
        options = Options()
        options.binary_location = chrome_driver_path
        # options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-extensions')

        driver = webdriver.Chrome(options)

        url = 'https://guatemaladigital.com'
        driver.get(url)

        contenido_html = driver.page_source
        soup = BeautifulSoup(contenido_html, 'html.parser')

        bloques = soup.find_all('div', class_='bloque--oferta marco--oferta--item mx-0')

        productos_procesados = set()

        for bloque in bloques:
            descripcion = bloque.find('p', class_='cort_not_h').text.strip()

            if descripcion in productos_procesados:
                continue

            try:
                precio_normal = bloque.find('span', class_='precio').text.strip()
                precio_oferta = bloque.find('div', class_='oferta--boton2').text.strip()

                img_src = bloque.find('img')['src']
                img_src = img_src.replace('/_next/image?url=', '')
                img_src = urllib.parse.unquote(img_src)
                img_src = img_src.split('&w=')[0]
                img_src = re.sub(r'\.\w+_(?=\.)', '', img_src)

                enlace = bloque.find('a', class_='product--a-oferta')['href']

                precio_normal = float(precio_normal[1:])
                precio_oferta = float(precio_oferta[1:])

                descuento = int(((precio_normal - precio_oferta) / precio_normal) * 100)

                if descuento > 50:
                    await send_message(chat_id, img_src, descripcion, precio_normal, precio_oferta, descuento, enlace)
                    productos_procesados.add(descripcion)

            except ValueError:
                await send_Error("1", ValueError)
                pass

        if not productos_procesados:
            await send_Error(chat_id, "No se encontraron productos con descuento", None)

    except Exception as e:
        await send_Error(chat_id, "Error al obtener productos2", e)

    finally:
         if driver is not None:
            driver.quit()

MAX_INTENTOS = 1
ESPERA_ENTRE_INTENTOS = 120

async def enviar_mensaje(chat_id, texto):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=chat_id, text=texto)

async def ejecutar_codigo_con_reintentos(chat_id):
    intentos = 0
    exitoso = False
    ultimo_error = None

    # await enviar_mensaje(chat_id, "Cargando Ofertas... ⏳")
    while intentos < MAX_INTENTOS and not exitoso:
        try:
            await ejecutar_codigo(chat_id)
            exitoso = True
        except Exception as e:
            ultimo_error = str(e)
            await enviar_mensaje(chat_id, f"Hubo un error al obtener los productos. Intento {intentos + 1}.")
            intentos += 1
            await asyncio.sleep(ESPERA_ENTRE_INTENTOS)

    if not exitoso:
        await enviar_mensaje(chat_id, f"Se agotaron los intentos. No se pudo completar la ejecución.\n\nÚltimo error: {ultimo_error}")
        print(f"Último error: {ultimo_error}")

for chat_id in chat_ids:
    asyncio.run(ejecutar_codigo_con_reintentos(chat_id))
