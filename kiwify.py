from plyer import notification

# Configurações da notificação
title = "Notificação do Kiwify"
message = "Esta é uma notificação falsa para fins educacionais."

# Enviando a notificação
notification.notify(
    title=title,
    message=message,
    app_name='Kiwify',
    timeout=10  # A notificação ficará visível por 10 segundos
)
