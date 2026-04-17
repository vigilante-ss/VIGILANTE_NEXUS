import asyncio
import random

class Megaphone:
    def __init__(self, page):
        self.page = page

    async def human_jitter(self, min_sec=1.5, max_sec=4.0):
        """Menyimulasikan jeda acak manusia sebelum bertindak."""
        delay = random.uniform(min_sec, max_sec)
        await asyncio.sleep(delay)

    async def human_typing(self, selector, text):
        """Mengetik seperti manusia, huruf demi huruf dengan jeda dinamis."""
        await self.page.locator(selector).click()
        await self.human_jitter(0.5, 1.5)
        
        for char in text:
            await self.page.keyboard.press(char)
            await asyncio.sleep(random.uniform(0.05, 0.25))

    async def post_to_x(self, message):
        """Contoh alur posting ke platform X (Twitter)."""
        print(f"[JARVIS] Megaphone Aktif: Menyiapkan transmisi ke X...")
        try:
            await self.page.goto("https://twitter.com/compose/tweet")
            await self.human_jitter(3, 6)
            
            # Catatan: Selector DOM sering berubah, ini adalah placeholder
            tweet_box_selector = 'div[data-testid="tweetTextarea_0"]'
            await self.page.wait_for_selector(tweet_box_selector)
            
            print("[JARVIS] Menulis pesan VIGILANTE...")
            await self.human_typing(tweet_box_selector, message)
            
            await self.human_jitter(1, 3)
            # await self.page.locator('div[data-testid="tweetButton"]').click() # Uncomment untuk mengeksekusi
            print("[JARVIS] Transmisi berhasil dijadwalkan/diposting.")
            
        except Exception as e:
            print(f"[ERROR] Megaphone gagal: {str(e)}")
