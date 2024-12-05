# Pixhawk IMU Verileri Üzerine Çalışma

Bu proje, Pixhawk uçuş kontrolcüsünden alınan IMU (Inertial Measurement Unit) verilerini analiz etmek ve görselleştirmek amacıyla oluşturulmuştur.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki yazılımlara ihtiyacınız olacak:
- Python 3.x
- NumPy
- Matplotlib
- Mavlink

## Kurulum

Gerekli Python paketlerini yüklemek için aşağıdaki komutu çalıştırın:
```bash
pip install requirements.txt
```

## Kullanım

1. Pixhawk cihazınızı bilgisayarınıza bağlayın.
2. IMU verilerini toplamak için `collect_data.py` dosyasını çalıştırın:
    ```bash
    python collect_data.py
    ```
3. Toplanan verileri görselleştirmek için `plot_data.py` dosyasını çalıştırın:
    ```bash
    python plot_data.py
    ```

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request gönderin veya bir sorun (issue) açın.

