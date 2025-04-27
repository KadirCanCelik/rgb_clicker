import pyautogui
from pynput import mouse
import tkinter as tk

def get_color_at(x, y):
    # Ekran görüntüsünü al
    screenshot = pyautogui.screenshot()
    # O koordinattaki pikselin rengini al
    color = screenshot.getpixel((x, y))
    return color

def show_color_popup(rgb):
    # Tkinter penceresi oluştur
    root = tk.Tk()
    root.title("Tıklanan Renk")
    
    # Pencerenin boyutları
    root.geometry("200x200")
    
    # Renk kutusunu pencerenin arka planı olarak ayarla
    root.config(bg=f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}')
    
    # Renk değerini yazan etiket ekle
    label = tk.Label(root, text=f"RGB: {rgb}", font=("Arial", 12), bg=f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}', fg="white")
    label.pack(pady=50)  # Label'ı pencereye yerleştir
    
    # Pencereyi açık tut
    root.mainloop()

def on_click(x, y, button, pressed):
    if pressed:
        rgb = get_color_at(x, y)
        print(f"\n📍 Koordinat: ({x}, {y})")
        print(f"🎨 Renk (RGB): {rgb}")
        
        # Renk pop-up'ını göster
        show_color_popup(rgb)
        
        # Listener'ı durdur (bir tıklama sonrası Listener sonlanır)
        return False

if __name__ == "__main__":
    print("🖱️ Ekrandan bir yere tıklayın, tıkladığınız yerin rengini alalım...")
    
    # Mouse Listener başlatılıyor
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()  # Dinleyiciyi başlat
    # Listener durduktan sonra program sonlanacak
