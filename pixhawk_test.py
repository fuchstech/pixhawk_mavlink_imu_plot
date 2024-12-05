import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from pymavlink import mavutil

# Pixhawk bağlantısı
connection = mavutil.mavlink_connection('COM7', baud=115200)
connection.wait_heartbeat()
print("Pixhawk ile bağlantı kuruldu.")

# Gerçek zamanlı grafik
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Ekseni hazırla
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_title("Pixhawk Gerçek Zamanlı Hareket")

# Güncellemeler için çizim fonksiyonu
while True:
    message = connection.recv_match(type='ATTITUDE', blocking=True)
    if message:
        roll = message.roll
        pitch = message.pitch
        yaw = message.yaw

        # Yön vektörlerini hesapla
        x = np.cos(roll)
        y = np.sin(pitch)
        z = np.sin(yaw)

        ax.cla()  # Eski veriyi temizle
        ax.quiver(0, 0, 0, x, y, z, length=0.5)
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([-1, 1])
        ax.set_title("Pixhawk Gerçek Zamanlı Hareket")

        plt.pause(0.01)  # Gerçek zamanlı güncelleme