import asyncio
import schedule
import time
from core.cloak import StealthBrowser
from core.megaphone import Megaphone
from dotenv import load_dotenv

# Memuat variabel environment
load_dotenv()

async def execute_campaign():
    """Fungsi utama untuk menjalankan satu siklus kampanye."""
    async with async_playwright() as p:
        engine = StealthBrowser()
        context, page = await engine.get_context(p)
        
        megaphone = Megaphone(page)
        
        pesan_hari_ini = "Kebebasan bersuara bukanlah hak istimewa, melainkan fondasi dasar. #VIGILANTE #KebebasanBersuara"
        
        # Eksekusi transmisi
        await megaphone.post_to_x(pesan_hari_ini)
        
        # Tutup konteks secara aman untuk menyimpan cookies
        print("[JARVIS] Operasi selesai. Mengamankan cookies dan menutup sesi.")
        await context.close()

def job_wrapper():
    """Bungkus sinkron untuk menjalankan async loop."""
    asyncio.run(execute_campaign())

if __name__ == "__main__":
    print("""
    ===================================================
      VIGILANTE NEXUS - SOCIAL COMMAND CENTER ONLINE
    ===================================================
    [JARVIS] Menunggu instruksi penjadwalan, Tuan...
    """)
    
    # Mode Langsung (Testing)
    job_wrapper()
    
    # Mode Penjadwalan (Cron) - Uncomment untuk produksi
    # schedule.every().day.at("10:30").do(job_wrapper)
    # schedule.every().day.at("18:45").do(job_wrapper)
    # 
    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)
