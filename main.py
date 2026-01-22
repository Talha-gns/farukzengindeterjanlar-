import flet as ft

def main(page: ft.Page):
    # Sayfa Genel Ayarları
    page.title = "Faruk Zengin Deterjanları"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F0F8FF"
    page.horizontal_alignment = "center"
    page.padding = 0
    page.spacing = 0

    # 1. SES DOSYASI (Müzik)
    # Tarayıcılar otomatik sesi engellediği için sağ alta kontrol butonu ekledik
    audio1 = ft.Audio(
        src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        autoplay=False,
    )
    page.overlay.append(audio1)

    # 2. İÇERİK ALANI (Değişecek kısım)
    content_area = ft.Container(padding=40, expand=True)

    # --- SAYFA İÇERİKLERİ ---
    
    # Ürünlerimiz
    urunler = ft.Column([
        ft.Text("Temizliğin Gücü: Faruk Zengin Ürünleri", size=30, weight="bold", color="blue"),
        ft.Row([
            ft.Container(content=ft.Column([ft.Icon("cleaning_services", size=40), ft.Text("Ultra Beyazlatıcı")], horizontal_alignment="center"), bgcolor="white", padding=20, border_radius=15, shadow=ft.BoxShadow(blur_radius=10, color="black12")),
            ft.Container(content=ft.Column([ft.Icon("water_drop", size=40), ft.Text("Sıvı Deterjan")], horizontal_alignment="center"), bgcolor="white", padding=20, border_radius=15, shadow=ft.BoxShadow(blur_radius=10, color="black12")),
            ft.Container(content=ft.Column([ft.Icon("local_florist", size=40), ft.Text("Parfümlü Yumuşatıcı")], horizontal_alignment="center"), bgcolor="white", padding=20, border_radius=15, shadow=ft.BoxShadow(blur_radius=10, color="black12")),
        ], alignment="center", spacing=20, wrap=True)
    ], horizontal_alignment="center", spacing=20)

    # İletişim
    iletisim = ft.Column([
        ft.Text("Bizimle İletişime Geçin", size=30, weight="bold", color="blue"),
        ft.TextField(label="Adınız Soyadınız", width=350, border_radius=10),
        ft.TextField(label="Mesajınız", multiline=True, min_lines=3, width=350, border_radius=10),
        ft.ElevatedButton("Gönder", icon="send", bgcolor="blue", color="white", height=50)
    ], horizontal_alignment="center", spacing=20)

    # Sosyal Medya
    sosyal = ft.Column([
        ft.Text("Bizi Takip Edin", size=30, weight="bold", color="blue"),
        ft.Row([
            ft.IconButton("facebook", icon_size=40, icon_color="blue", on_click=lambda _: page.launch_url("https://facebook.com")),
            ft.IconButton("camera_alt", icon_size=40, icon_color="pink", on_click=lambda _: page.launch_url("https://instagram.com")),
            ft.IconButton("share", icon_size=40, icon_color="grey"),
        ], alignment="center", spacing=30)
    ], horizontal_alignment="center", spacing=30)

    # --- NAVİGASYON FONKSİYONU ---
    def menu_tikla(e):
        if e.control.text == "Ürünlerimiz":
            content_area.content = urunler
        elif e.control.text == "İletişim":
            content_area.content = iletisim
        elif e.control.text == "Sosyal Medya":
            content_area.content = sosyal
        page.update()

    # Müzik Aç/Kapat
    def toggle_music(e):
        if audio1.autoplay == False:
            audio1.play()
            audio_btn.icon = "music_note"
            audio_btn.text = "Müzik Açık"
        else:
            audio1.pause()
            audio_btn.icon = "music_off"
            audio_btn.text = "Müzik Kapalı"
        page.update()

    # ÜST HEADER VE MENÜ
    header = ft.Container(
        content=ft.Column([
            ft.Text("FARUK ZENGİN DETERJANLARI", color="white", size=40, weight="bold"),
            ft.Row([
                ft.TextButton("Ürünlerimiz", style=ft.ButtonStyle(color="white"), on_click=menu_tikla),
                ft.TextButton("İletişim", style=ft.ButtonStyle(color="white"), on_click=menu_tikla),
                ft.TextButton("Sosyal Medya", style=ft.ButtonStyle(color="white"), on_click=menu_tikla),
            ], alignment="center")
        ], horizontal_alignment="center"),
        bgcolor="blue",
        padding=30,
    )

    # Sağ alt müzik butonu
    audio_btn = ft.FloatingActionButton(icon="music_off", text="Müzik Çal", on_click=lambda _: audio1.play())
    page.floating_action_button = audio_btn

    # Başlangıç sayfası
    content_area.content = urunler
    page.add(header, content_area)
    page.update()

ft.app(target=main)
