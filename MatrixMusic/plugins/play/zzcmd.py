import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, Message
from typing import Union
from pyrogram.types import InlineKeyboardButton
from MatrixMusic import app
from MatrixMusic.misc import HAPP, SUDOERS, XCB
from config import OWNER_ID
                                       
                                       
@app.on_callback_query(filters.regex("zzzback"))
async def zzzback(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>⌔︙مرحباً بك عزيزي</b>\n<b>⌔︙استخدم الازرار بالاسفل\n⌔︙ل تصفح اوامر بوت القران</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ اوامر التشغيل ›", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "‹ اوامر القناة ›", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "‹ اوامر الادمن ›", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "‹ اوامر المطور ›", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(
                        "اذاعة القران الكريم", url="https://t.me/quran_Tv21"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzdv") & SUDOERS)
async def mpdtsf(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>⌔︙مرحباً بك عزيزي المطور </b>\n\n<b>⌔︙استخدم الازرار بالاسفل\n⌔︙ل تصفح اوامر بوت القران</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ التحديث ›", callback_data="zzzup"),
                ],[
                    InlineKeyboardButton(
                        "‹ الرفع ›", callback_data="zzzsu"),
                    InlineKeyboardButton(
                        "‹ الحظر ›", callback_data="zzzbn"),
                ],[
                    InlineKeyboardButton(
                        "‹ اشعارات & المساعد ›", callback_data="zzzas"),
                ],[
                    InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="zzzback"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzll"))
async def zzzll(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⌔︙<b>قائمة اوامر التشغيل :</b>
– – – – – – – – – – – – – – – – – –
تشغيل + (اسم الاغنية / رابط الاغنية)
<b>- ل تشغيل السورة في المكالمة الصوتية</b>
– – – – – – – – – – – – – – – – – –
فيديو + (اسم المقطع / رابط المقطع)
<b>- ل تشغيل فيديو في المكالمة المرئية</b>
– – – – – – – – – – – – – – – – – –
بحث + الاسم
<b>- ل تحميل السور والمقاطع الصوتيه من اليوتيوب</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzad"))
async def zzzad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⌔︙<b>قائمة اوامر الادمن :</b>
– – – – – – – – – – – – – – – – – –
الاعدادات
<b>- ل عرض إعدادات اوضاع التشغيل</b>
– – – – – – – – – – – – – – – – – –
ايقاف / انهاء / اسكت
<b>- ل إيقاف تشغيل السورة في المكالمة</b>
– – – – – – – – – – – – – – – – – –
وقف / توقف
<b>- ل إيقاف تشغيل السورة في المكالمة مؤقتاً</b>
– – – – – – – – – – – – – – – – – –
كمل / كملي
<b>- ل إستئناف تشغيل السورة في المكالمة</b>
– – – – – – – – – – – – – – – – – –
تخطي
<b>- ل تخطي السورة وتشغيل السورة التاليه</b>
– – – – – – – – – – – – – – – – – –
الاغاني
<b>- ل معرفة السور الموجودة في قائمة الانتظار</b>
– – – – – – – – – – – – – – – – – –
بنج
<b>- ل عرض سرعة تشغيل البوت</b>
– – – – – – – – – – – – – – – – – –
رفع ادمن/تنزيل ادمن
<b>- ل رفع/تنزيل ادمن في البوت</b>
– – – – – – – – – – – – – – – – – –
الادمنيه
<b>- ل عرض قائمة ادمنية البوت</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzch"))
async def zzzch(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⌔︙<b>قائمة اوامر التشغيل في القناة :</b>
– – – – – – – – – – – – – – – – – –
<b>- ارفع البوت إشراف في القناة و شغل مباشر</b>
<b>- ارسل (/channelplay او ربط) + يوزر القناة ل الربط</b>
<b>- ثم استخدم الاوامر بالاسفل ل التشغيل</b>
– – – – – – – – – – – – – – – – – –
تشغيل + اسم الاغنية
<b>- ل تشغيل السورة في المكالمة الصوتية</b>
– – – – – – – – – – – – – – – – – –
فيديو + اسم المقطع
<b>- ل تشغيل فيديو في المكالمة المرئية</b>
– – – – – – – – – – – – – – – – – –
ايقاف / انهاء / اسكت
<b>- ل إيقاف تشغيل السورة في المكالمة</b>
– – – – – – – – – – – – – – – – – –
وقف / توقف
<b>- ل إيقاف تشغيل السورة في المكالمة مؤقتاً</b>
– – – – – – – – – – – – – – – – – –
كمل / استئناف
<b>- ل إستئناف تشغيل السورة في المكالمة</b>
– – – – – – – – – – – – – – – – – –
تخطي
<b>- ل تخطي السورة وتشغيل السورة التاليه</b>
– – – – – – – – – – – – – – – – – –
/seek + عدد الثواني
<b>- ل تقديم السورة ل الامام</b>
/seekback + عدد الثواني
<b>- ل إرجاع السورة ل الخلف</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzup") & SUDOERS)
async def zzzup(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⌔︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>- قائمة اوامر التحديثات :</b>
– – – – – – – – – – – – – – – – – –
السجلات
<b>- لـ جلب سجلات البوت</b>
– – – – – – – – – – – – – – – – – –
تحديث
<b>- لـ تحديث البوت</b>
– – – – – – – – – – – – – – – – – –
اعاده تشغيل
<b>- لـ اعادة تشغيل البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzsu") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⌔︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>- قائمة اوامر الرفع :</b>
– – – – – – – – – – – – – – – – – –
رفع مطور/تنزيل مطور
<b>- ل رفع/تنزيل شخص مطور في بوت القران</b>
– – – – – – – – – – – – – – – – – –
المطورين
<b>- ل عرض قائمة مطورين البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzbn") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⌔︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>- قائمة اوامر الحظر :</b>
– – – – – – – – – – – – – – – – – –
بلوك/الغاء بلوك/المبلكين
<b>- ل حظر/الغاء حظر شخص من استخدام بوت القران</b>
– – – – – – – – – – – – – – – – – –
احظره عام/الغاء حظره عام
<b>- ل حظر/الغاء حظر شخص من استخدام بوت القران عام</b>
– – – – – – – – – – – – – – – – – –
المحظورين عام
<b>- ل جلب قائمة المحظورين عام في البوت</b>
– – – – – – – – – – – – – – – – – –
حظر مجموعة/سماح
<b>- ل حظر/الغاء حظر مجموعة من استخدام بوت القران</b>
– – – – – – – – – – – – – – – – – –
المجموعات المحظورة
<b>- ل جلب قائمة بالمجموعات المحظورة من استخدام البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("zzzas") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⌔︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>⌔︙قائمة اوامر المساعد :</b>
– – – – – – – – – – – – – – – – – –
السجل ⦗ تفعيل / تعطيل ⦘
<b>- ل تفعيل/تعطيل اشعارات مجموعة سجل البوت</b>
– – – – – – – – – – – – – – – – – –
⦗ المغادره التلقائيه ⦗ تفعيل / تعطيل
<b>- تفعيل/تعطيل المغادره التلقائيه ل الحساب المساعد من المجموعات عند عدم استخدام بوت القران</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="zzzdv"),
               ],
          ]
        ),
   )
