import asyncio
from telethon import TelegramClient

# البيانات التي استخرجتها أنت
api_id = 20443064
api_hash = '061a4fa5feffd11330bcc62ce0dd65cc'

# قائمة البوتات التي تريد مراسلتها (تأكد من المعرفات)
target_bots = ['@Uploadfilesmnbot', '@Ghhggggffdfgggbot']

async def main():
    # إنشاء العميل (سيطلب منك رقم الهاتف في المرة الأولى)
    async with TelegramClient('my_session', api_id, api_hash) as client:
        print("✅ تم تسجيل الدخول بنجاح! البوت يعمل الآن...")
        
        while True:
            for bot in target_bots:
                try:
                    # إرسال رسالة لتنشيط البوتات
                    await client.send_message(bot, 'نبضة تنشيط 🔄')
                    print(f"🚀 تم إرسال رسالة إلى {bot}")
                except Exception as e:
                    print(f"❌ خطأ مع {bot}: {e}")
            
            # الانتظار 5 دقائق (300 ثانية)
            print("🕒 في انتظار الدورة القادمة بعد 5 دقائق...")
            await asyncio.sleep(300)

if __name__ == '__main__':
    asyncio.run(main())
