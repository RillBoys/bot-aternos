import time
from mcstatus import MinecraftServer
import threading

# Ganti ip dan port server kalian
server_address = "ip_server:port"

# Interval ping dalam detik
interval = 300  # 5 menit

def ping_server():
    server = MinecraftServer.lookup(server_address)
    while True:
        try:
            status = server.status()
            print(f"Ping server berhasil: {status.players.online} pemain online.")
        except Exception as e:
            print(f"Terjadi kesalahan saat ping: {e}")
        time.sleep(interval)

def keep_alive():
    while True:
        try:
            ping_server()
        except Exception as e:
            print(f"Terjadi kesalahan pada keep alive: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    print("Bot KeepAlive dimulai...")
    threading.Thread(target=keep_alive).start()