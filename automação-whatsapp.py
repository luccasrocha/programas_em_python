import pywhatkit as kit
import time
from datetime import datetime
import schedule

# CONFIGURAÇÕES
NUMERO = "+5534999384055"  # Número com DDD e código do país (ex: +55 Brasil)
MENSAGEM = "Oi! Mensagem automática do Python! 🤖"

def enviar_whatsapp_agora():
    """Envia mensagem AGORA mesmo"""
    try:
        kit.sendwhatmsg(NUMERO, MENSAGEM, 15, 30)  # 15h30 (ajuste pro horário atual)
        print("✅ Mensagem enviada AGORA!")
    except Exception as e:
        print(f"❌ Erro: {e}")

def enviar_whatsapp_horario(hora, minuto, mensagem):
    """Agenda mensagem para horário específico"""
    try:
        kit.sendwhatmsg(NUMERO, mensagem, hora, minuto)
        print(f"✅ Mensagem agendada para {hora}:{minuto}")
    except Exception as e:
        print(f"❌ Erro: {e}")

def loop_mensagens_automaticas():
    """Envia mensagens em loop"""
    mensagens = [
        "1️⃣ Primeira mensagem automática!",
        "2️⃣ Segunda mensagem do dia!",
        "3️⃣ Tudo funcionando perfeitamente! 🔥",
        "4️⃣ Mensagem recorrente! ⏰"
    ]

    for i, msg in enumerate(mensagens, 1):
        print(f"Enviando mensagem {i}...")
        enviar_whatsapp_agora()
        print(f"Aguardando 2 minutos...")
        time.sleep(120)  # 2 minutos entre mensagens

# ========== EXEMPLO DE USO ==========

# 1. Enviar AGORA
print("🔥 Enviando AGORA...")
enviar_whatsapp_agora()

# 2. Agendar para HOJE às 15:30
print("\n📅 Agendando para 15:30...")
enviar_whatsapp_horario(15, 30, "Mensagem agendada para 15:30! ⏰")

# 3. Loop automático (comente se não quiser)
# loop_mensagens_automaticas()

# 4. Agendamento diário com schedule
def mensagem_diaria():
    enviar_whatsapp_horario(10, 0, "Bom dia! Mensagem diária! ☀️")

schedule.every().day.at("10:00").do(mensagem_diaria)

print("\n⏰ Agendamentos configurados!")
print("Pressione Ctrl+C para parar")

# Manter rodando
while True:
    schedule.run_pending()
    time.sleep(60)
