import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
import os

class StealthBrowser:
    def __init__(self):
        # Menyimpan session (cookies, local storage) agar tidak perlu login berulang
        self.user_data_dir = os.path.join(os.getcwd(), "data", "browser_profile")
        
    async def get_context(self, p):
        """Membuat instance browser yang kebal deteksi bot."""
        print("[JARVIS] Menginisialisasi The Cloak: Stealth Browser Engine...")
        
        browser_context = await p.chromium.launch_persistent_context(
            user_data_dir=self.user_data_dir,
            headless=False, # Set ke True jika ingin berjalan di background tanpa UI
            args=[
                '--disable-blink-features=AutomationControlled',
                '--no-sandbox',
                '--disable-infobars'
            ],
            viewport={"width": 1366, "height": 768}
        )
        
        page = await browser_context.new_page()
        # Menginjeksikan script anti-deteksi ke dalam halaman
        await stealth_async(page)
        
        return browser_context, page
