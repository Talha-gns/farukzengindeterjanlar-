import flet as ft

def main(page: ft.Page):
    page.title = "Faruk Zengin Deterjanları"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F0F8FF"
    page.horizontal_alignment = "center"
    page.padding = 0

    # İÇERİK ALANI
    content_area = ft.Container(padding=40, alignment=ft.alignment.center)

    # --- SAYFALAR ---
    urunler = ft.Column([
        ft.Text("Ürün Gruplarımız", size=30, weight="bold", color="blue"),
        ft.Row([
            ft.Container(content=ft.Text("Ultra Beyazlatıcı"), bgcolor="white", padding=20, border_radius=10),
            ft.Container(content=ft.Text("Sıvı Deterjan"), bgcolor="white", padding=20, border_radius=10),
            ft.Container(content=ft.Text("Yumuşatıcı"), bgcolor="white", padding=20, border_radius=10),
        ], alignment="center", wrap=True)
    ], horizontal_alignment="center")

    iletisim = ft.Column([
        ft.Text("İletişim", size=30, weight="bold"),
        ft.TextField(label="Mesajınız", multiline=True, width=300),
        ft.ElevatedButton("Gönder", bgcolor="blue", color="white")
    ], horizontal_alignment="center")

    sosyal = ft.Column([
        ft.Text("Bizi Takip Edin", size=30, weight="bold"),
        ft.ElevatedButton("Instagram", on_click=lambda _: page.launch_url("https://instagram.com")),
        ft.ElevatedButton("Facebook", on_click=lambda _: page.launch_url("https://facebook.com")),
    ], horizontal_alignment="center")

    # MÜZİK (Web üzerinde çalışması için bir buton ekledik)
    audio1 = ft.Audio(src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", autoplay=False)
    page.overlay.append(audio1)

    def play_music(e):
        audio1.play()
        page.show_snack_bar(ft.SnackBar(ft.Text("Müzik Başlatıldı!")))

    # NAVİGASYON FONKSİYONU
    def navigasyon(e):
        if e.control.text == "Ürünlerimiz":
            content_area.content = urunler
        elif e.control.text == "İletişim":
            content_area.content = iletisim
        elif e.control.text == "Sosyal Medya":
            content_area.content = sosyal
        page.update()

    # ÜST MENÜ
    header = ft.Container(
        bgcolor="blue",
        padding=20,
        content=ft.Column([
            ft.Text("FARUK ZENGİN DETERJANLARI", color="white", size=35, weight="bold"),
            ft.Row([
                ft.TextButton("Ürünlerimiz", on_click=navigasyon, style=ft.ButtonStyle(color="white")),
                ft.TextButton("İletişim", on_click=navigasyon, style=ft.ButtonStyle(color="white")),
                ft.TextButton("Sosyal Medya", on_click=navigasyon, style=ft.ButtonStyle(color="white")),
                ft.IconButton(icon=ft.icons.MUSIC_NOTE, icon_color="white", on_click=play_music),
            ], alignment="center")
        ], horizontal_alignment="center")
    )

    content_area.content = urunler
    page.add(header, content_area)

ft.app(target=main)
