from pymavlink import mavutil

# Pixhawk bağlantısı kur
connection = mavutil.mavlink_connection('COM7', baud=115200)  # COM portunu kontrol edin.

# Bağlantıyı bekle
connection.wait_heartbeat()
print("Pixhawk ile bağlantı kuruldu.")

# Sürekli olarak attitude (tutum) bilgisi al
while True:
    message = connection.recv_match(type='ATTITUDE', blocking=True)
    if message:
        roll = message.roll  # Roll açısı (radyan)
        pitch = message.pitch  # Pitch açısı (radyan)
        yaw = message.yaw  # Yaw açısı (radyan)
        
        print(f"Roll: {roll}, Pitch: {pitch}, Yaw: {yaw}")
