'''
    ราชาศัพท์ หมวดร่างกาย: https://www.thairath.co.th/lifestyle/life/2214560
    ราชาศัพท์ หมวดกริยา:   https://sites.google.com/site/mayeiei24242/thima-kha-rachasaphth/khaa-rachasaphth-hmwd-kha-kiriya
'''

RAJAWORDS = {
    "ศีรษะ": "พระเศียร",
    "เส้นผม": "เส้นพระเจ้า",
    "มวยผม": "พระโมลี",
    "หน้าผาก": "พระนลาฏ",
    "คิ้ว": "พระขนง",
    "ดวงตา": "พระเนตร",
    "แก้วตา": "พระเนตรดารา",
    "ตาดำ": "ดวงพระเนตรดำ",
    "ตาขาว": "ดวงพระเนตรขาว",
    "ขนตา": "ขนพระเนตร",
    "น้ำตา": "น้ำพระเนตร",
    "จมูก": "พระนาสิก",
    "สันจมูก": "สันพระนาสิก",
    "ขนจมูก": "ขนพระนาสิก",
    "เนื้อ": "พระมังสา",
    "หนวด": "พระมัสสุ",
    "ลมหายใจเข้า": "พระปัสสาสะ",
    "ลมหายใจออก": "พระอัสสาสะ",
    "ปาก": "พระโอษฐ์",
    "เพดานปาก": "เพดานพระโอษฐ์",
    "เขี้ยว": "พระทาฐะ",
    "ฟัน": "พระทนต์",
    "ลิ้น": "พระชิวหา",
    "แก้ม": "พระปราง",
    "กระพุ้งแก้ม": "กระพุ้งพระปราง",
    "หู": "พระกรรณ",
    "ใบหน้า": "พระพักตร์",
    "หน้า": "พระพักตร์",
    "คอ": "พระศอ",
    "รักแร้": "พระกัจฉะ",
    "แขน": "พระกร",
    "ข้อมือ": "ข้อพระกร",
    "มือ": "พระหัตถ์",
    "ฝ่ามือ": "ฝ่าพระหัตถ์",
    "นิ้วมือ": "พระองคุลี",
    "นิ้วชี้": "พระดัชนี",
    "นิ้วกลาง": "พระมัชฌิมา",
    "นิ้วโป้ง": "พระอังคุฐ",
    "นิ้วหัวแม่มือ": "พระอังคุฐ",
    "นิ้วก้อย": "พระกนิษฐา",
    "เล็บ": "พระนขา",
    "ไฝ": "พระปีฬกะ",
    "ขีแมลงวัน": "พระปีฬกะ",
    "สิว": "พระอสา",
    "เงา": "พระฉายา",
    "ขน": "พระโลมา",
    "กระดูก": "พระอังคาร",
    "เหงื่อ": "พระเสโท",
    "น้ำลาย": "พระเขฬะ",
    "ลูกกระเดือก": "พระกัณฐมณี",
    "ไหปลาร้า": "พระรากขวัญ",
    "อก": "พระอุระ",
    "น้ำนม": "พระกษิรธารา",
    "สายรก": "สายพระสกุล",
    "สีข้าง": "พระปรัศว์",
    "กล้ามเนื้อ": "กล้ามพระมังสา",
    "บ่า": "พระพาหุ",
    "ชีพจร": "พระชีพจร",
    "หัวฝี": "พระยอด",
    "กระดูกแขน": "พระพาหัฐิ",
    "กระดูกคอ": "พระคีวัฐิ",
    "กระดูกแข้ง": "พระชังฆัฐิ",
    "กระดูกเท้า": "พระปาทัฐิ",
    "ตะโพก": "พระโสภี",
    "สะโพก": "พระโสภี",
    "กระเพาะปัสสาวะ": "พระวัตถิ",
    "น้ำลาย": "พระเขฬะ",
    "หลอดลม": "หลอดพระวาโย",
    "เส้น": "พระนหารู",
    "เอ็น": "พระนหารู",
    "เส้นเอ็น": "พระนหารู",
    "ปอด": "พระปัปผาสะ",
    "ม้าม": "พระปิหกะ",
    "เส้นประสาท": "พระธมนี",
    "ไต": "พระยกนะ",
    "ลำไส้ใหญ่": "พระอันตะ",
    "หัวใจ": "พระหทัย",
    "ท้อง": "พระอุทร",
    "เส้นเลือด": "เส้นพระโลหิต",
    "หลอดเลือด": "หลอดพระโลหิต",
    "พังผืด": "พระกิโลมกะ",
    "น้ำในไขข้อ": "พระลสิกา",
    "ดี": "พระปิตตะ",
    "น้ำดี": "พระปิตตะ",
    "เสลด": "พระเสมหะ",
    "เสมหะ": "พระเสมหะ",
    "น้ำหนอง": "น้ำเหลือง",
    "น้ำเหลือง": "พระบุพโพ",
    "ขา": "พระเพลา",
    "ตัก": "พระเพลา",
    "แข้ง": "พระชงฆ์",
    "น่อง": "หลังพระชงฆ์",
    "เท้า": "พระบาท",
    "นิ้วเท้า": "นิ้วพระบาท",
    "ตาตุ่ม": "พระโคปผกะ",
    "อุจจาระ": "พระบังคนหนัก",
    "อึ": "พระบังคนหนัก",
    "ขี้": "พระบังคนหนัก",
    "ปัสสาวะ": "พระบังคนเบา",
    "ฉี่": "พระบังคนเบา",
    "เถ้ากระดูก": "พระอังคาร",
    "ขี้เล็บ": "มูลพระนขา",
    "ซี่โครง": "พระผาสุกะ",
    "กระดูกซี่โครง": "พระผาสุกัฐิ",
    "มันในสมอง": "พระมัตถลุงค์",
    "ส้นเท้า": "ส้นพระบาท",
    "ส้นตีน": "ส้นพระบาท",
    "ฝ่าเท้า": "ผ่าพระบาท",
    "หลังเท้า": "หลังพระบาท",
    "มดลูก": "กล่องพระสกุล",
    "เอว": "พระกฤษฎี",
    "ก้น": "พระที่นั่ง",
    "บั้นท้าย": "พระที่นั่ง",
    "สะดือ": "พระนาภี",
    "ร่างกาย": "พระวรกาย",
    "ศอก": "พระกับประ",
    "พูด": "ทรงมีพระราชดำรัส",
    "คำพูด": "พระราชดำรัส",
    "พูด": "ตรัส",
    "เดิน": "เสด็จพระราชดำเนิน",
    "แต่งหนังสือ": "ทรงพระราชนิพนธ์",
    "ไอ": "ทรงพระกาสะ",
    "หัวเราะ": "ทรงพระสรวล",
    "เซ็นชื่อ": "ทรงพระปรมาภิไธย",
    "ลงชื่อ": "ทรงพระปรมาภิไธย",
    "ลงนาม": "ทรงพระปรมาภิไภย",
    "จับ": "ทรงสัมผัส",
    "สุขสบาย": "ทรงพระเกษมสำราญ",
    "จาม": "ทรงพระปินาสะ",
    "คำสั่ง": "พระราชโองการ",
    "สั่ง": "ทรงมีพระราชโองการ",
    "ออกคำสั่ง": "ทรงมีพระราชโองการ",
    "คำสอน": "พระราโชวาท",
    "ทักทาย": "ทรงมีพระราชปฏิสันถาร",
    "อยากให้": "ทรงมีพระราชประสงค์ให้",
    "ต้องการ": "ทรงมีพระราชประสงค์",
    "ความอยาก": "พระราชประสงค์",
    "ความต้องการ": "พระราชประสงค์",
    "ล้างหน้า": "สรงพระพักตร์",
    "ล้าง": "ชำระ",
    "ไปเที่ยวที่": "เสด็จประพาส ณ ",
    "ถาม": "ทรงมีพระราชปุจฉา",
    "คำถาม": "พระราชปุจฉา",
    "ไหว้": "ถวายบังคม",
    "ตัดสิน": "ทรงมีพระบรมราชวินิจฉัย",
    "การตัดสิน": "พระราชวินิจฉัย",
    "คำตัดสิน": "พระราชวินิจฉัย",
    "ดู": "ทอดพระเนตร",
    "ให้": "พระราชทาน",          ### CAUTION!
    "เขียนจดหมาย": "ทรงพระราชหัตเลขา",
    "แต่งตัว": "ทรงเครื่อง",
    "เรียน": "ทรงพระอักษร",
    "เขียน": "ทรงพระอักษร",
    "อ่าน": "ทอดพระเนตร",
    "นั่ง": "ประทับ",
    "ยืน": "ทรงยืน",
    "นอน": "บรรทม"
}