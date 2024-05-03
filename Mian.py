import discord
import random
import datetime
from discord.ext import commands
import asyncio
from discord import Embed
import requests
import os
from googletrans import Translator
NEWS_API_KEY = '347bc1eebab34fd5b2cbe5f7d7b25184' 
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'



translator = Translator()

verification_state_file = "verification_state.txt"
prefix = "che"
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

channel_id = 1233018197398130780
role_id = 1233018196940816428  

image_filename = 'BIENVENIDO.png'
image_path = os.path.join(os.path.dirname(__file__), image_filename)

img_chau = "CHAU.png"
image_path1 = os.path.join(os.path.dirname(__file__), img_chau)


urlDB = "https://mercados.ambito.com//dolar/informal/variacion"
urlDN = "https://mercados.ambito.com//dolar/oficial/variacion"
urlDBN = "https://mercados.ambito.com//dolarnacion//variacion"
urlMEP = "https://mercados.ambito.com//dolarrava/mep/variacion"
urlEURO = "https://mercados.ambito.com//euro//variacion"
urlEB = "https://mercados.ambito.com//euro/informal/variacion"
urlDT = "https://mercados.ambito.com//dolarturista/variacion"
urlDM = "https://mercados.ambito.com//dolar/mayorista/variacion"
urlDC = "https://mercados.ambito.com//dolarcripto/variacion"
urlEuro = "https://mercados.ambito.com//euro//variacion"
urlEUROB = "https://mercados.ambito.com//euro/informal/variacion"

def get_dolar_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        compra = data.get("compra")
        venta = data.get("venta")
        variacion = data.get("variacion")  
        return compra, venta, variacion  
    else:
        return None, None, None

def create_combined_embed():
    compra_DBN, venta_DBN, variacion_DBN = get_dolar_data(urlDBN)
    compra_MEP, venta_MEP, variacion_MEP = get_dolar_data(urlMEP)
    compra_EURO, venta_EURO, variacion_EURO = get_dolar_data(urlEURO)
    compra_EB, venta_EB, variacion_EB = get_dolar_data(urlEB)
    compra_DT, venta_DT, variacion_DT = get_dolar_data(urlDT)
    compra_DM, venta_DM, variacion_DM = get_dolar_data(urlDM)
    compra_DC, venta_DC, variacion_DC = get_dolar_data(urlDC)
    compra_DN, venta_DN, variacion_DN = get_dolar_data(urlDN)
    compra_DB, venta_DB, variacion_DB = get_dolar_data(urlDB)

    if (compra_DB is None or venta_DB is None or compra_DN is None or venta_DN is None or 
        compra_DBN is None or venta_DBN is None or compra_DM is None or venta_DM is None or 
        compra_DC is None or venta_DC is None or compra_DT is None or venta_DT is None or 
        compra_EB is None or venta_EB is None or compra_EURO is None or venta_EURO is None or 
        compra_MEP is None or venta_MEP is None):
        return None

    embed = discord.Embed(
        title="Valores del dólar",
        description="💵 Aquí están los valores de compra y venta del dólar y Euro en tiempo real 💵:",
        color=0x3498db
    )
    embed.add_field(name="💵 Dólar Blue:",
                    value="💸 Valor de venta: {}\n💰 Valor de compra: {}\n📊 Variación: {}".format(venta_DB, compra_DB, variacion_DB), inline=False)
    embed.add_field(name="💵 Dólar Oficial:",
                    value="💸 Valor de venta: {}\n💰 Valor de compra: {}\n📊 Variación: {}".format(venta_DN, compra_DN, variacion_DN), inline=False)
    embed.add_field(name="💵 Dólar Banco Nacion:",
                    value="💸 Valor de venta: {}\n💰 Valor de compra: {}\n📊 Variación: {}".format(venta_DBN, compra_DBN, variacion_DBN), inline=False)
    embed.add_field(name="💵 Dólar MEP:",
                    value="💸 Valor de venta: {}\n💰 Valor de compra: {}\n📊 Variación: {}".format(venta_MEP, compra_MEP, variacion_MEP), inline=False)
    embed.add_field(name="💵 Dolar Turista:",
                    value="💸 Valor de venta: {}\n💰 Valor de compra: {}\n📊 Variación: {}".format(venta_DT, compra_DT, variacion_DT), inline=False)
    embed.add_field(name="💵 Dólar Mayorista:",
                    value="💸 Valor de venta: {}\n💰 Valor de compra: {}\n📊 Variación: {}".format(venta_DM, compra_DM, variacion_DM), inline=False)
    embed.add_field(name="💵 Dólar Crypto:",
                    value="💸 Valor de venta: {}\n💰 Valor de compra: {}\n📊 Variación: {}".format(venta_DC, compra_DC, variacion_DC), inline=False)
    embed.add_field(name="💵 Euro:",
                    value="💸 Valor de venta: {}\n💰 Valor de compra: {}\n📊 Variación: {}".format(venta_EURO, compra_EURO, variacion_EURO), inline=False)
    embed.add_field(name="💵 Euro Blue:",
                    value="💸 Valor de venta: {}\n💰 Valor de compra: {}\n📊 Variación: {}".format(venta_EB, compra_EB, variacion_EB), inline=False)
    return embed

def create_embedDB():
    response = requests.get(urlDB)
    embed = discord.Embed(
        title="Valores del dólar blue",
        description="💵Aquí están los valores de compra y venta del dólar blue en tiempo real💵:",
        color=0x3498db  
    )
    if response.status_code == 200:
        embed.add_field(name="💸Valor de venta:", value=response.json()["venta"], inline=False)
        embed.add_field(name="💰Valor de compra:", value=response.json()["compra"], inline=False)
        embed.add_field(name="📊 Variacion:", value=response.json()["variacion"], inline=False)
    return embed

def create_embedDN():
    response = requests.get(urlDN)
    embed = discord.Embed(
        title="Valores del dólar Oficial",
        description="💵Aquí están los valores de compra y venta del dólar Oficial en tiempo real💵:",
        color=0x3498db  
    )
    if response.status_code == 200:
        embed.add_field(name="💸Valor de venta:", value=response.json()["venta"], inline=False)
        embed.add_field(name="💰Valor de compra:", value=response.json()["compra"], inline=False)
        embed.add_field(name="📊 Variacion:", value=response.json()["variacion"], inline=False)
    return embed

def create_embedEURO():
    response = requests.get(urlEuro)
    embed = discord.Embed(
        title="Valores del Euro",
        description="💶 Aquí están los valores de compra y venta del Euro en tiempo real 💶:",
        color=0x3498db  
    )
    if response.status_code == 200:
        embed.add_field(name="💸 Valor de venta:", value=response.json()["venta"], inline=False)
        embed.add_field(name="💰 Valor de compra:", value=response.json()["compra"], inline=False)
        embed.add_field(name="📊 Variación:", value=response.json()["variacion"], inline=False)
    return embed

def create_embedEBLUE():
    response = requests.get(urlEUROB)
    embed = discord.Embed(
        title="Valores del Euro Blue",
        description="💶 Aquí están los valores de compra y venta del Euro Blue en tiempo real 💶:",
        color=0x3498db  
    )
    if response.status_code == 200:
        embed.add_field(name="💸 Valor de venta:", value=response.json()["venta"], inline=False)
        embed.add_field(name="💰 Valor de compra:", value=response.json()["compra"], inline=False)
        embed.add_field(name="📊 Variación:", value=response.json()["variacion"], inline=False)
    return embed

def get_random_meme():
    try:
        response = requests.get("https://api.memegen.link/images")
        if response.status_code == 200:
            data = response.json()
            random_meme = random.choice(data)
            print("Random meme data:", random_meme)
            return random_meme['url']
        else:
            return "No se pudo obtener un meme en este momento. Inténtalo de nuevo más tarde."
    except Exception as e:
        print("Error al obtener el meme:", e)
        return "Ocurrió un error al obtener el meme."

def create_rules_and_commands_embed():
    rules_embed = discord.Embed(title='Reglas del Servidor', description='Aquí están las reglas del servidor:')
    rules_embed.add_field(name='Regla 1', value='¡Sé respetuoso con los demás miembros!', inline=False)
    rules_embed.add_field(name='Regla 2', value='No se permite el spam o el contenido inapropiado.', inline=False)
    rules_embed.add_field(name='Regla 3', value='¡Diviértete!', inline=False)
    
    norms_embed = discord.Embed(title='Comandos del Servidor', description='Aquí están los comandos que puedes usar en el servidor')
    norms_embed.add_field(name='Sección: Comandos divertidos', value='', inline=False)
    norms_embed.add_field(name='Ping', value='¡El bot te responde con un pong!', inline=False)
    norms_embed.add_field(name='Che hola', value='¡El Bot te saluda!', inline=False)
    norms_embed.add_field(name='Che chau', value='¡El bot te despide!', inline=False)
    norms_embed.add_field(name='Che salame', value='¡El Bot se reta contigo!', inline=False)
    norms_embed.add_field(name='Che comandos', value='¡El Bot te enseña todos los comandos!', inline=False)
    norms_embed.add_field(name='che meme ', value='El bot te da un meme aleatorio', inline=False)
    norms_embed.add_field(name='che hora ', value='El bot te muestra la hora', inline=False)
    norms_embed.add_field(name='che chiste', value='El bot te tira un chiste', inline=False)
    norms_embed.add_field(name='che limpiar', value='El bot limpia cierta cantidad de mensajes', inline=False)
    norms_embed.add_field(name='che ban', value='El bot banea a la persona deseada', inline=False)
    norms_embed.add_field(name='che traducir', value='El bot traduce texto', inline=False)
    norms_embed.add_field(name='che info usuario', value='El bot muestra info de un usuario', inline=False)
    norms_embed.add_field(name='', value='', inline=False)
    norms_embed.add_field(name='Sección: Comandos Economía', value='', inline=False)
    norms_embed.add_field(name='Che dolar blue', value='¡El bot te muestra el precio del dólar blue en tiempo real!', inline=False)
    norms_embed.add_field(name='Che dolar oficial', value='¡El Bot te muestra el precio del dólar oficial en tiempo real!', inline=False)
    norms_embed.add_field(name='Che dolar precios', value='¡El bot te muestra el precio de todos los tipos de dólar y euro en tiempo real (la respuesta puede tardar dependiendo de la velocidad de tu internet)!', inline=False)
    norms_embed.add_field(name='Che euro', value='¡El Bot te muestra el precio del euro en tiempo real!', inline=False)
    norms_embed.add_field(name='Che euro blue', value='¡El bot te muestra el precio del euro blue en tiempo real!', inline=False)
    norms_embed.add_field(name='Che acciones', value='El bot te muestra las acciones de dos empresas conocidas en argentina', inline=False)
    norms_embed.add_field(name='Che bitcoin', value='El bot te muestra el precio del bitcoin en tiempo real y en pesos argentinos', inline=False)
    norms_embed.add_field(name='', value='', inline=False)
    norms_embed.add_field(name='Seccion: Comandos de juego', value='', inline=False)
    norms_embed.add_field(name='che quiero jugar', value='El bot te da un menu con 3 juegos', inline=False)

    
    return rules_embed, norms_embed

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    historical_data = stock.history(period="1d")
    if not historical_data.empty:
        close_price = historical_data['Close'][0]
        return close_price
    else:
        print(f"No se encontraron datos para el símbolo {symbol}")
        return None

def create_stock_embed(data, symbol):
    embed = discord.Embed(
        title=f"Precio de la acción: {symbol}",
        description="Aquí está el precio de cierre de la acción en tiempo real:",
        color=0x00ff00
    )
    if data:
        embed.add_field(name="Precio de cierre:", value=f"${data['close_price']:.2f}", inline=False)
    return embed

def acciones(url, symbol):
    stock_data = get_stock_price(url, symbol)
    embed = create_stock_embed(stock_data, symbol)
    return embed

def bitcoin_price_embed():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {
        'symbol': 'BTC',
        'convert': 'ARS'  # Cambiar a la moneda deseada, en este caso pesos argentinos
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '2d4241ab-58b9-49a5-8257-df57956a596c'  # Reemplazar 'TU_API_KEY' con tu clave de API de CoinMarketCap
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    if 'error' in data:
        error_message = data['error']['message']
        return discord.Embed(title="Error", description=error_message, color=0xFF0000)
    else:
        bitcoin_price_ars = data['data']['BTC']['quote']['ARS']['price']
        embed = discord.Embed(title="Precio del Bitcoin en Pesos Argentinos (ARS)", color=0xF2A900)
        embed.add_field(name="Precio", value=f"${bitcoin_price_ars:.2f}", inline=False)
        return embed



class MyClient(discord.Client):
    
    async def translate_message(self, channel, target_language, message):
        try:
            translation = translator.translate(message, dest=target_language)
            translated_text = translation.text
            await channel.send(f"Texto traducido a {target_language}: {translated_text}")
        except Exception as e:
            await channel.send(f"Ocurrió un error durante la traducción: {str(e)}")

    
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        content_lower = message.content.lower()
    
    
    
    async def obtener_chiste(self):
        response = requests.get('https://api.chucknorris.io/jokes/random')
        data = response.json()
        return data['value']
    
    async def obtener_hora(self):
        ahora = datetime.datetime.now()
        hora_actual = ahora.strftime("%H:%M:%S")
        return hora_actual

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.verification_message_sent = False
    async def on_ready(self):
        print('Logged on as', self.user)
        await self.enviar_mensaje_verificacion()
   
    async def on_member_remove(self, member):  
        print(f'{member} has left the server.')
        try:
            dm_channel = await member.create_dm()
            await dm_channel.send("Nos vemos.")
        except discord.Forbidden:
            print(f"No se puede enviar mensaje directo a {member}, permisos insuficientes.")
        
    async def on_message(self, message):
        if message.author == self.user:
            return
        

        content_lower = message.content.lower()

        if content_lower == 'ping':
            await message.channel.send('pong')
        
        if content_lower == "che hola":
            await message.channel.send("Hola pa")
        
        if content_lower == "che chau":
            await message.channel.send("chau pa")

        if content_lower == "che salame":
            await message.channel.send("salame vo wachin  :nerd:")

        if content_lower == "che comandos":
            await self.mostrar_comandos(message.channel)
        
        if content_lower == "che info":
            rules_embed, norms_embed = create_rules_and_commands_embed()
            await message.channel.send(embed=rules_embed)
            await message.channel.send(embed=norms_embed)

        if content_lower == "che dolar blue":
            embed = create_embedDB()
            await message.channel.send(embed=embed)

        if content_lower == "che dolar oficial":
            embed1 = create_embedDN()
            await message.channel.send(embed=embed1)

        if content_lower == "che dolar precios":
            combined_embed = create_combined_embed()
            if combined_embed:
                await message.channel.send(embed=combined_embed)
        
        if content_lower == "che euro":
            embed_euro = create_embedEURO()
            await message.channel.send(embed=embed_euro)

        if content_lower == "che euro blue":
            embed_euro_blue = create_embedEBLUE()
            await message.channel.send(embed=embed_euro_blue)
        
        if content_lower == "che meme":
            meme = get_random_meme()
            await message.channel.send(meme)
        
        if content_lower == "che quiero jugar":
            await self.mostrar_menu_juegos(message.channel)

        if content_lower == "che bitcoin":
            embedbit = bitcoin_price_embed()
            await message.channel.send(embed=embedbit)

        if content_lower == "che hora":
            hora = await self.obtener_hora()
            await message.channel.send(f"¡Son las {hora}!")
        
        if content_lower == "che chiste":
            chiste = await self.obtener_chiste()
            await message.channel.send(chiste)
        
        if content_lower.startswith("che limpiar"):
            if message.author.guild_permissions.manage_messages:  
                try:
                    amount = int(content_lower.split(' ')[-1])  
                    await message.channel.purge(limit=amount)
                    await message.channel.send(f'Se limpiaron {amount} mensajes.')
                except ValueError:
                    await message.channel.send('Por favor, ingresa un número válido.')
            else:
                await message.channel.send('No tienes permisos para limpiar mensajes.')

        if content_lower == "che info usuario":
            await message.channel.send("¿De qué usuario quieres obtener información? Por favor menciona al usuario.")
            
            def check(m):
                return m.author == message.author and m.channel == message.channel
            
            try:
                response = await self.wait_for('message', check=check, timeout=60)
                usuario_mencionado = response.mentions[0]
                
               
                user_info_embed = discord.Embed(title="Información del Usuario", color=0x00ff00)
                user_info_embed.add_field(name="Nombre de Usuario", value=usuario_mencionado.name, inline=True)
                user_info_embed.add_field(name="Apodo", value=usuario_mencionado.display_name, inline=True)
                user_info_embed.add_field(name="ID de Usuario", value=usuario_mencionado.id, inline=False)
                roles = ", ".join([role.name for role in usuario_mencionado.roles])
                user_info_embed.add_field(name="Roles", value=roles if roles else "Sin roles", inline=False)
                await message.channel.send(embed=user_info_embed)
            
            except asyncio.TimeoutError:
                await message.channel.send("Se acabó el tiempo. Por favor intenta nuevamente.")
        
        if content_lower.startswith("che ban"):
            if message.author.guild_permissions.ban_members:
                command_parts = content_lower.split(" ")
                if len(command_parts) < 3:
                    await message.channel.send("Uso incorrecto del comando. Por favor, proporciona el nombre del usuario y el motivo del ban.")
                    return
                user_name = command_parts[2]
                ban_reason = " ".join(command_parts[3:])
                user = discord.utils.get(message.guild.members, name=user_name)
                if user:
                    dm_channel = await user.create_dm()
                    ban_message = f"Has sido baneado del servidor. Motivo: {ban_reason}"
                    await dm_channel.send(ban_message)
                    await user.ban(reason=ban_reason)
                    await message.channel.send(f"{user.name} ha sido baneado del servidor. Se ha enviado un mensaje privado con el motivo del ban.")
                else:
                    await message.channel.send("No se encontró al usuario especificado en el servidor.")
            else:
                await message.channel.send("No tienes permisos para banear miembros.")

       
        if content_lower.startswith('che traducir'):
            
            parts = content_lower.split(' ', 2)
            if len(parts) == 3:
                target_language = parts[1]
                text_to_translate = parts[2]
                await self.translate_message(message.channel, target_language, text_to_translate)
            else:
                await message.channel.send("Formato incorrecto. Uso correcto: `che traducir <idioma> <texto>`")

        if content_lower == "che noticias":
            
            params = {
                'apiKey': NEWS_API_KEY,
                'country': 'ar',  
                'pageSize': 1  
            }
            response = requests.get(NEWS_API_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                articles = data.get('articles', [])
                if articles:
                    
                    article = articles[0]
                    title = article.get('title', 'Sin título')
                    description = article.get('description', 'Sin descripción')
                    url = article.get('url', '')

                    
                    embed = Embed(title=title, description=description, url=url)
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send("No se encontraron noticias.")
            else:
                await message.channel.send("Error al obtener noticias.")
        
        if message.content.lower() == "che acciones":
            symbol1 = "GGAL.BA"  
            symbol2 = "YPF"      
            
          
            price1 = get_stock_price(symbol1)
            price2 = get_stock_price(symbol2)

         
            embed = discord.Embed(title="Precios de las Acciones", color=0x00ff00)
            embed.add_field(name=" 📈 Grupo Financiero Galicia (GGAL.BA)", value=f"${price1:.2f}", inline=False)
            embed.add_field(name="📈 YPF", value=f"${price2:.2f}", inline=False)

            
            await message.channel.send(embed=embed)
    
    
 
    async def on_reaction_add(self, reaction, user):
        if user == self.user:
            return
        
        channel = reaction.message.channel
        if channel.id ==1233018197398130780 and str(reaction.emoji) == "✅":
            guild = reaction.message.guild
            role = discord.utils.get(guild.roles, id=1233018196940816428)
            await user.add_roles(role)
    async def enviar_mensaje_verificacion(self):
        channel = self.get_channel(1233018197398130780)  
        if channel:
            message = "Se te han envado por privado las reglas y comandos del servidor, si las aceptas, reaccion abajo para verificarte!"
            embed = discord.Embed(description=message, color=0x00FF00)  
            msg = await channel.send(embed=embed)
            await msg.add_reaction("✅")
    async def on_member_join(self, member):
        print(f"¡Se ha unido un nuevo miembro! {member}")
        await self.send_welcome_message(member)
        
    async def send_welcome_message(self, member):
        dm_channel = await member.create_dm()
    
        welcome_message = f'Bienvenido al servidor!'
        await dm_channel.send(welcome_message)
        
        rules_embed = discord.Embed(title='Reglas del Servidor', description='Aquí están las reglas del servidor:')
        rules_embed.add_field(name='Regla 1', value='¡Sé respetuoso con los demás miembros!', inline=False)
        rules_embed.add_field(name='Regla 2', value='No se permite el spam o el contenido inapropiado.', inline=False)
        rules_embed.add_field(name='Regla 3', value='¡Diviértete!', inline=False)
        
        norms_embed = discord.Embed(title='Comandos del Servidor', description='Aquí están los comandos que puedes usar en el servidor')
        norms_embed.add_field(name='Sección: Comandos divertidos', value='', inline=False)
        norms_embed.add_field(name='Ping', value='¡El bot te responde con un pong!', inline=False)
        norms_embed.add_field(name='Che hola', value='¡El Bot te saluda!', inline=False)
        norms_embed.add_field(name='Che chau', value='¡El bot te despide!', inline=False)
        norms_embed.add_field(name='Che salame', value='¡El Bot se reta contigo!', inline=False)
        norms_embed.add_field(name='Che comandos', value='¡El Bot te enseña todos los comandos!', inline=False)
        norms_embed.add_field(name='che meme', value='El bot te tira un meme aleatorio', inline=False)
        norms_embed.add_field(name='che hora', value='El bot te tira la hora', inline=False)
        norms_embed.add_field(name='che chiste', value='El bot te tira un chiste', inline=False)
        norms_embed.add_field(name='che limpiar', value='El bot limpia cierta cantidad de mensajes', inline=False)
        norms_embed.add_field(name='che ban', value='El bot banea a la persona deseada', inline=False)
        norms_embed.add_field(name='che traducir', value='El bot traduce texto', inline=False)
        norms_embed.add_field(name='che info usuario', value='El bot muestra info de un usuario', inline=False)
        norms_embed.add_field(name='', value='', inline=False)
        norms_embed.add_field(name='Sección: Comandos Economía', value='', inline=False)
        norms_embed.add_field(name='Che dolar blue', value='¡El bot te muestra el precio del dólar blue en tiempo real!', inline=False)
        norms_embed.add_field(name='Che dolar oficial', value='¡El Bot te muestra el precio del dólar oficial en tiempo real!', inline=False)
        norms_embed.add_field(name='Che dolar precios', value='¡El bot te muestra el precio de todos los tipos de dólar y euro en tiempo real (la respuesta puede tardar dependiendo de la velocidad de tu internet)!', inline=False)
        norms_embed.add_field(name='Che euro', value='¡El Bot te muestra el precio del euro en tiempo real!', inline=False)
        norms_embed.add_field(name='Che euro blue', value='¡El bot te muestra el precio del euro blue en tiempo real!', inline=False)
        norms_embed.add_field(name='Che acciones', value='El bot te muestra las acciones de dos empresas conocidas en argentina', inline=False)
        norms_embed.add_field(name='Che bitcoin', value='El bot te muestra el precio del bitcoin en tiempo real y en pesos argentinos', inline=False)
        norms_embed.add_field(name='', value='', inline=False)
        norms_embed.add_field(name='Seccion: Comandos de juego', value='', inline=False)
        norms_embed.add_field(name='che quiero jugar', value='El bot te da un menu con 3 juegos', inline=False)

        
        await dm_channel.send(embed=rules_embed)
        await dm_channel.send(embed=norms_embed)
        if os.path.isfile(image_path):
            with open(image_path, 'rb') as image_file:
                await dm_channel.send(file=discord.File(image_file, filename=image_filename))

    
    async def mostrar_menu_juegos(self, channel):
        embed = discord.Embed(title="Menú de Juegos", description="Elige un juego:", color=0x00ff00)
        embed.add_field(name="Piedra, Papel o Tijeras", value="Selecciona esta opción con 1️⃣", inline=False)
        embed.add_field(name="Adivinar numero", value="Selecciona esta opción con 2️⃣", inline=False)
        embed.add_field(name="Tirar dados", value="Selecciona esta opción con 3️⃣", inline=False)
        
        msg = await channel.send(embed=embed)
        
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("3️⃣")

        def check(reaction, user):
            return user != self.user and reaction.message.author == self.user
        reaction, user = await self.wait_for('reaction_add', check=check)
    
        if str(reaction.emoji) == "1️⃣":
            await self.jugar_piedra_papel_tijeras(channel)
        elif str(reaction.emoji) == "2️⃣":
            await self.adivinar_numero(channel)
        elif str(reaction.emoji) == "3️⃣":
            await self.jugar_tirar_dados(channel)

    async def adivinar_numero(self, channel):
        while True:
            await channel.send('¡Bienvenido al juego de adivinar un número! Tienes 3 intentos para adivinar el número que estoy pensando entre 1 y 10. ¡Comencemos!')
            
            numero_pensado = random.randint(1, 10)
            intentos_restantes = 3

            while intentos_restantes > 0:
                    await channel.send('Intenta adivinar el número:')
                    intento = await self.wait_for('message', check=lambda m: m.author != self.user and m.channel == channel)
                    
                    try:
                        numero_intento = int(intento.content)
                    except ValueError:
                        await channel.send('Por favor, ingresa un número válido.')
                        continue
                    
                    if numero_intento == numero_pensado:
                        await channel.send('bien ahi! adivinaste el numero correctamente ')
                        break
                    else:
                        intentos_restantes -= 1
                        if intentos_restantes > 0:
                            await channel.send(f'Incorrecto. Te quedan {intentos_restantes} intentos.')
                        else:
                            await channel.send(f'perdon El número era {numero_pensado}. suerte en la proxima')

            respuesta = await self.esperar_respuesta(channel, "¿Quieres seguir jugando? (sí/no)")
            if respuesta.lower() not in ["sí", "si"]:
                await channel.send("Chau!")
                break

    async def jugar_tirar_dados(self, channel):
        while True:  
            resultado_dado = random.randint(1, 6)
            embed = discord.Embed(title="Tirar Dados", description=f"Sacaste un un {resultado_dado}!", color=0xffd700)
            await channel.send(embed=embed) 
            respuesta = await self.esperar_respuesta(channel, "¿Quieres seguir jugando? (sí/no)")
            if respuesta.lower() not in ["sí", "si"]:
                    await channel.send("Chau!!")
                    break
        
    async def jugar_piedra_papel_tijeras(self, channel):
        while True:
            await channel.send("¡Vamos a jugar Piedra, Papel o Tijeras!")

            opciones = ["piedra", "papel", "tijeras"]

            embed = discord.Embed(title="Piedra, Papel o Tijeras", description="Reacciona con tu elección:", color=0x00ff00)
            embed.add_field(name="Piedra", value="⛰️", inline=True)
            embed.add_field(name="Papel", value="📰", inline=True)
            embed.add_field(name="Tijeras", value="✂️", inline=True)
            msg = await channel.send(embed=embed)

            await msg.add_reaction("⛰️")
            await msg.add_reaction("📰")
            await msg.add_reaction("✂️")

            def check(reaction, user):
                return user != self.user and reaction.message.author == self.user
            reaction, user = await self.wait_for('reaction_add', check=check)

            eleccion_usuario = None
            for emoji in ["⛰️", "📰", "✂️"]:
                if str(reaction.emoji) == emoji:
                    if emoji == "⛰️":
                        eleccion_usuario = "piedra"
                    elif emoji == "📰":
                        eleccion_usuario = "papel"
                    elif emoji == "✂️":
                        eleccion_usuario = "tijeras"
                    break
            eleccion_computadora = random.choice(opciones)

            if eleccion_usuario == eleccion_computadora:
                resultado = "¡Empate!"
            elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijeras") or \
                 (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
                 (eleccion_usuario == "tijeras" and eleccion_computadora == "papel"):
                resultado = "¡Ganaste!"
            else:
                resultado = "¡Perdiste!"

            await channel.send(f"vos elegiste: {eleccion_usuario}\n yo elegi: {eleccion_computadora}\n{resultado}")

            respuesta = await self.esperar_respuesta(channel, "¿Quieres seguir jugando? (sí/no)")
            if respuesta.lower() not in ["sí", "si"]:
                await channel.send("Chau!")
                break

    async def esperar_respuesta(self, channel, pregunta):
        await channel.send(pregunta)
        def check(m):
            return m.channel == channel and m.author != self.user
        try:
            respuesta = await self.wait_for('message', check=check, timeout=60)
            return respuesta.content
        except asyncio.TimeoutError:
            await channel.send("Se acabó el tiempo. Hasta luego.")
            return ""

    async def mostrar_comandos(self, channel):
        embed = discord.Embed(title="Lista de comandos", description="¡Aquí tienes todos los comandos disponibles!", color=0x00ff00)
        embed.add_field(name="Seccion: Comandos comunes", value="", inline=False)
        embed.add_field(name="Che hola", value="¡Saludo del bot!", inline=False)
        embed.add_field(name="Che chau", value="¡Despedida del bot!", inline=False)
        embed.add_field(name="Che salame", value="¡Respuesta graciosa del bot!", inline=False)
        embed.add_field(name="Che comandos", value="¡Muestra esta lista de comandos!", inline=False)
        embed.add_field(name='che meme', value='El bot te tira un meme aleatorio', inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="Seccion: Comandos de Economia", value="", inline=False)
        embed.add_field(name="Che dolar blue", value="¡Muestra el valor del dólar blue!", inline=False)
        embed.add_field(name="Che dolar oficial", value="¡Muestra el valor del dólar oficial!", inline=False)
        embed.add_field(name="Che dolar precios", value="¡Muestra los valores de todas las variantes del dólar!", inline=False)
        embed.add_field(name="Che euro", value="¡Muestra el valor del euro!", inline=False)
        embed.add_field(name="Che euro blue", value="¡Muestra el valor del euro blue!", inline=False)
        embed.add_field(name='Che acciones', value='El bot te muestra las acciones de dos empresas conocidas en argentina', inline=False)
        embed.add_field(name='Che bitcoin', value='El bot te muestra el precio del bitcoin en tiempo real y en pesos argentinos', inline=False)
        embed.add_field(name='', value='', inline=False)
        embed.add_field(name='Seccion: Comandos de juego', value='', inline=False)
        embed.add_field(name='che quiero jugar', value='El bot te da un menu con 3 juegos', inline=False)

        await channel.send(embed=embed)

    async def on_member_remove(self, member):
       
        channel_id = 1235723117670830162  
        channel = self.get_channel(channel_id)
        
        if channel:
            
            await channel.send(f'{member.display_name} ha abandonado el servidor. ¡Buena suerte!')
        else:
            print("No se encontró el canal para despedidas.")

    
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = MyClient(intents=intents)
client.run('TOKEN')