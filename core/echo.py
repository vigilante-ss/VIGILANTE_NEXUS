import asyncio
import random

class Echo:
    def __init__(self, page, megaphone_utils):
        self.page = page
        self.utils = megaphone_utils # Meminjam fungsi human_typing dan human_jitter

    async def intercept_instagram(self, target_username, comment_text):
        """Menyusup ke profil Instagram target dan mengomentari postingan terbaru."""
        print(f"[JARVIS] Menetapkan kordinat ke Instagram: @{target_username}")
        try:
            # 1. Navigasi langsung ke profil target
            await self.page.goto(f"https://www.instagram.com/{target_username}/")
            await self.utils.human_jitter(3, 5)

            # 2. Mencari dan mengklik postingan (grid) paling awal/terbaru
            # Selector ini menargetkan elemen tautan gambar pertama di grid profil
            first_post_selector = 'article a' 
            await self.page.wait_for_selector(first_post_selector)
            await self.page.locator(first_post_selector).first.click()
            await self.utils.human_jitter(2, 4)

            # 3. Menemukan kolom komentar
            comment_box_selector = 'textarea[aria-label="Tambahkan komentar..."], textarea[aria-label="Add a comment..."]'
            await self.page.wait_for_selector(comment_box_selector)
            
            print(f"[JARVIS] Menginjeksi suara VIGILANTE pada postingan @{target_username}...")
            await self.utils.human_typing(comment_box_selector, comment_text)
            
            # 4. Eksekusi pengiriman (Tekan Enter)
            await self.utils.human_jitter(1, 2)
            await self.page.keyboard.press("Enter")
            print(f"[JARVIS] Injeksi berhasil di Instagram @{target_username}.")
            
            # Tutup modal postingan agar bisa lanjut ke target berikutnya
            await self.page.keyboard.press("Escape")
            await self.utils.human_jitter(2, 3)

        except Exception as e:
            print(f"[ERROR] Gagal menembus pertahanan Instagram @{target_username}: {str(e)}")

    async def intercept_threads(self, target_username, comment_text):
        """Menyusup ke profil Threads target dan memberikan balasan."""
        print(f"[JARVIS] Menetapkan kordinat ke Threads: @{target_username}")
        try:
            await self.page.goto(f"https://www.threads.net/@{target_username}")
            await self.utils.human_jitter(4, 6)

            # Klik tombol Reply pada postingan pertama
            # Perhatian: Class UI Threads sangat dinamis karena dirender oleh React, 
            # kita menggunakan aria-label atau pencarian teks universal.
            reply_button = self.page.get_by_role("button", name="Reply").first
            await reply_button.click()
            await self.utils.human_jitter(2, 3)

            # Ketik komentar
            editor_selector = 'div[contenteditable="true"]'
            await self.page.wait_for_selector(editor_selector)
            await self.utils.human_typing(editor_selector, comment_text)

            # Klik Post
            await self.utils.human_jitter(1, 2)
            await self.page.get_by_role("button", name="Post").click()
            print(f"[JARVIS] Injeksi suara berhasil di Threads @{target_username}.")

        except Exception as e:
            print(f"[ERROR] Gagal menyusup di Threads @{target_username}: {str(e)}")
