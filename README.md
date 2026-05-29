# discord-bot

Bot de Discord hecho con Python y `discord.py`.

## Que hace

El bot se conecta a Discord y responde al comando slash `/hola` con un mensaje de bienvenida.

## Crear el archivo `.env`

El token real no va en GitHub. Va solamente en tu PC.

En VS Code, dentro de la carpeta del bot, crea un archivo llamado `.env` y escribe:

```env
DISCORD_TOKEN=ACA_PEGA_EL_TOKEN_DE_TU_BOT
```

No pongas comillas alrededor del token. El archivo `.env.example` queda como ejemplo seguro para copiar.

## Instalar y correr en VS Code

1. Descarga o clona este repo en tu PC.
2. Abre la carpeta del proyecto en VS Code.
3. Abre una terminal en VS Code.
4. Crea un entorno virtual:

```bash
python -m venv .venv
```

5. Activa el entorno virtual.

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

En CMD:

```cmd
.venv\Scripts\activate.bat
```

6. Instala las dependencias:

```bash
pip install -r requirements.txt
```

7. Crea el archivo `.env` con tu token.
8. Ejecuta el bot:

```bash
python bot.py
```

Cuando aparezca `Bot conectado como ...`, el bot ya esta funcionando.

## Invitar el bot al servidor

En el Discord Developer Portal, genera una URL de invitacion con estos scopes:

```text
bot
applications.commands
```

Luego invita el bot a tu servidor. El comando `/hola` puede tardar un poco en aparecer porque Discord sincroniza los comandos slash.
