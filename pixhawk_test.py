from pymavlink import mavutil

# Pixhawk bağlantısı kur
connection = mavutil.mavlink_connection('COM7', baud=115200)  # COM portunu kontrol edin.

# Bağlantıyı bekle
connection.wait_heartbeat()
print("Pixhawk ile bağlantı kuruldu.")


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_orientation(roll, pitch, yaw):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Bir vektör ile simüle et
    ax.quiver(0, 0, 0, np.cos(roll), np.sin(pitch), np.sin(yaw))
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_title("Pixhawk Orientation")
    plt.show()

# Sürekli olarak attitude (tutum) bilgisi al
while True:
    message = connection.recv_match(type='ATTITUDE', blocking=True)
    if message:
        roll = message.roll  # Roll açısı (radyan)
        pitch = message.pitch  # Pitch açısı (radyan)
        yaw = message.yaw  # Yaw açısı (radyan)
        
        print(f"Roll: {roll}, Pitch: {pitch}, Yaw: {yaw}")
        plot_orientation(roll, pitch, yaw)