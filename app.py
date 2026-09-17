import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string
from werkzeug.utils import secure_filename

app = Flask(__name__)

# إعداد مجلد حفظ الملفات والتأكد من إنشائه تلقائياً لمنع أي خطأ 500
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# مسار لجلب وعرض الشعار logo.jpg
@app.route('/logo.jpg')
def serve_logo():
    return send_from_directory('.', 'logo.jpg')

# 1. الصفحة الرئيسية (اختيار السداسي الدراسي)
@app.route('/')
def index():
    html_content = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>منصة كلية الشريعة - خروبة</title>
        <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --bg-base: #030a07;
                --gold-primary: #f3c68f;
                --gold-glow: #d4af37;
                --card-glass: rgba(10, 26, 18, 0.75);
                --border-glass: rgba(243, 198, 143, 0.18);
                --text-main: #f4f9f5;
                --text-muted: #95b8a6;
            }
            body { 
                font-family: 'Amiri', serif; 
                background: var(--bg-base);
                background-image: 
                    radial-gradient(circle at 10% 10%, rgba(27, 67, 50, 0.5) 0%, transparent 40%),
                    radial-gradient(circle at 90% 90%, rgba(212, 175, 55, 0.12) 0%, transparent 40%),
                    radial-gradient(circle at 50% 50%, rgba(15, 42, 29, 0.8) 0%, #030a07 100%);
                margin: 0; padding: 35px 15px; text-align: center; color: var(--text-main); 
                display: flex; flex-direction: column; min-height: 85vh; justify-content: space-between; background-attachment: fixed;
            }
            .wrapper { max-width: 540px; margin: 0 auto; width: 100%; }
            .container { 
                background: var(--card-glass); padding: 45px 28px; border-radius: 28px; 
                box-shadow: 0 30px 70px rgba(0, 0, 0, 0.6), 0 0 50px rgba(27, 67, 50, 0.3); 
                border: 1px solid var(--border-glass); text-align: right; backdrop-filter: blur(25px); position: relative; overflow: hidden;
            }
            .container::before {
                content: "❖ ✧ ✦ ✧ ❖"; display: block; text-align: center; color: var(--gold-primary); 
                font-size: 13px; margin-bottom: 22px; letter-spacing: 10px; opacity: 0.85; text-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
            }
            .logo-img { display: block; margin: 0 auto 20px auto; max-width: 90px; border-radius: 50%; border: 2px solid var(--gold-glow); box-shadow: 0 5px 15px rgba(0,0,0,0.5); }
            .category-title {
                font-size: 20px; color: var(--gold-primary); margin: 0 0 18px 0; font-weight: 700; 
                border-bottom: 1px solid rgba(243, 198, 143, 0.2); padding-bottom: 12px; display: flex; align-items: center; gap: 12px; text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
            }
            .category-title span.icon {
                background: linear-gradient(135deg, #1b4332, #0f2a1d); color: var(--gold-primary); width: 40px; height: 40px; 
                display: inline-flex; align-items: center; justify-content: center; border-radius: 14px; font-size: 16px; border: 1px solid rgba(243, 198, 143, 0.3);
            }
            .btn { 
                display: block; background: linear-gradient(135deg, rgba(45, 106, 79, 0.85) 0%, rgba(27, 67, 50, 0.95) 100%); 
                color: var(--text-main); padding: 16px 22px; margin: 14px 0; text-decoration: none; border-radius: 16px; 
                font-size: 18px; font-weight: 700; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3); transition: all 0.4s ease; text-align: center; border: 1px solid rgba(255, 255, 255, 0.08);
            }
            .btn:hover { transform: translateY(-4px); background: linear-gradient(135deg, rgba(64, 145, 108, 0.9) 0%, rgba(45, 106, 79, 1) 100%); border-color: var(--gold-glow); }
            .btn-secondary { background: linear-gradient(135deg, rgba(30, 70, 52, 0.85) 0%, rgba(15, 42, 29, 0.95) 100%); }
            footer { font-size: 13px; color: var(--text-muted); margin-top: 35px; font-weight: 700; text-shadow: 0 2px 6px rgba(0, 0, 0, 0.8); }
        </style>
    </head>
    <body>
        <div class="wrapper">
            <div class="container">
                <img src="/logo.jpg" alt="شعار منصة كلية الشريعة" class="logo-img">
                <div class="category-title">
                    <span class="icon">🏛️</span> اختر السداسي الدراسي
                </div>
                <a href="/semester5" class="btn">السداسي الخامس</a>
                <a href="#" class="btn btn-secondary" style="opacity: 0.5; cursor: not-allowed;" onclick="return false;">السداسي السادس</a>
            </div>
        </div>
        <footer>جميع الحقوق محفوظة منصة كلية الشريعة © 2026</footer>
    </body>
    </html>
    """
    return render_template_string(html_content)

# 2. صفحة السداسي الخامس
@app.route('/semester5')
def semester5():
    html_content = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>السداسي الخامس - السنة الثالثة فقه وأصوله</title>
        <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --bg-base: #030a07;
                --gold-primary: #f3c68f;
                --gold-glow: #d4af37;
                --card-glass: rgba(10, 26, 18, 0.75);
                --border-glass: rgba(243, 198, 143, 0.18);
                --text-main: #f4f9f5;
                --text-muted: #95b8a6;
            }
            body { 
                font-family: 'Amiri', serif; background: var(--bg-base);
                background-image: 
                    radial-gradient(circle at 10% 10%, rgba(27, 67, 50, 0.5) 0%, transparent 40%),
                    radial-gradient(circle at 90% 90%, rgba(212, 175, 55, 0.12) 0%, transparent 40%),
                    radial-gradient(circle at 50% 50%, rgba(15, 42, 29, 0.8) 0%, #030a07 100%);
                margin: 0; padding: 35px 15px; text-align: center; color: var(--text-main); 
                display: flex; flex-direction: column; min-height: 85vh; justify-content: space-between; background-attachment: fixed;
            }
            .wrapper { max-width: 540px; margin: 0 auto; width: 100%; }
            .top-nav { display: flex; justify-content: flex-start; margin-bottom: 22px; }
            .back-home-btn {
                background: rgba(15, 42, 29, 0.6); backdrop-filter: blur(16px); color: var(--gold-primary);
                padding: 11px 22px; border-radius: 16px; text-decoration: none; font-size: 16px; font-weight: 700;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4); border: 1px solid var(--border-glass); display: inline-flex; align-items: center; gap: 8px; transition: 0.3s;
            }
            .back-home-btn:hover { background: rgba(27, 67, 50, 0.9); border-color: var(--gold-glow); color: #fff; }
            .container { 
                background: var(--card-glass); padding: 45px 28px; border-radius: 28px; 
                box-shadow: 0 30px 70px rgba(0, 0, 0, 0.6); border: 1px solid var(--border-glass); text-align: right; backdrop-filter: blur(25px); position: relative;
            }
            .container::before {
                content: "❖ ✧ ✦ ✧ ❖"; display: block; text-align: center; color: var(--gold-primary); 
                font-size: 13px; margin-bottom: 22px; letter-spacing: 10px; opacity: 0.85;
            }
            .category-title {
                font-size: 20px; color: var(--gold-primary); margin: 38px 0 18px 0; font-weight: 700; 
                border-bottom: 1px solid rgba(243, 198, 143, 0.2); padding-bottom: 12px; display: flex; align-items: center; gap: 12px;
            }
            .category-title:first-of-type { margin-top: 0; }
            .category-title span.icon {
                background: linear-gradient(135deg, #1b4332, #0f2a1d); color: var(--gold-primary); width: 40px; height: 40px; 
                display: inline-flex; align-items: center; justify-content: center; border-radius: 14px; font-size: 16px; border: 1px solid rgba(243, 198, 143, 0.3);
            }
            .btn { 
                display: block; background: linear-gradient(135deg, rgba(45, 106, 79, 0.85) 0%, rgba(27, 67, 50, 0.95) 100%); 
                color: var(--text-main); padding: 16px 22px; margin: 14px 0; text-decoration: none; border-radius: 16px; 
                font-size: 18px; font-weight: 700; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3); text-align: center; border: 1px solid rgba(255, 255, 255, 0.08); transition: 0.3s;
            }
            .btn:hover { transform: translateY(-4px); background: linear-gradient(135deg, rgba(64, 145, 108, 0.9) 0%, rgba(45, 106, 79, 1) 100%); border-color: var(--gold-glow); }
            .btn-secondary { background: linear-gradient(135deg, rgba(30, 70, 52, 0.85) 0%, rgba(15, 42, 29, 0.95) 100%); }
            footer { font-size: 13px; color: var(--text-muted); margin-top: 35px; font-weight: 700; text-shadow: 0 2px 6px rgba(0, 0, 0, 0.8); }
        </style>
    </head>
    <body>
        <div class="wrapper">
            <div class="top-nav">
                <a href="/" class="back-home-btn"><span>← الرئيسية</span></a>
            </div>
            <div class="container">
                <div class="category-title"><span class="icon">📜</span> أعمال توجيهية (تطبيق TD)</div>
                <a href="/module_manage?name=ترتيل و حفظ القرآن" class="btn">ترتيل و حفظ القرآن</a>
                <a href="/module_manage?name=لغة عربية (بلاغة)" class="btn">لغة عربية (بلاغة)</a>
                <a href="/module_manage?name=قواعد تفسير النصوص" class="btn">قواعد تفسير النصوص</a>
                <a href="/module_manage?name=المواريث" class="btn">المواريث</a>
                <a href="/module_manage?name=فقه مقارن" class="btn">فقه مقارن</a>
                <a href="/module_manage?name=قضايا فقهية معاصرة" class="btn">قضايا فقهية معاصرة</a>
                <a href="/module_manage?name=لغة أجنبية (إنجليزية)" class="btn">لغة أجنبية (إنجليزية)</a>

                <div class="category-title" style="margin-top: 42px;"><span class="icon">🏛️</span> محاضرات (Cours)</div>
                <a href="#" class="btn btn-secondary">قواعد تفسير النصوص</a>
                <a href="#" class="btn btn-secondary">قضايا فقهية معاصرة</a>
                <a href="#" class="btn btn-secondary">المواريث</a>
                <a href="#" class="btn btn-secondary">مقاصد الشريعة</a>
                <a href="#" class="btn btn-secondary">النظام القضائي</a>
                <a href="#" class="btn btn-secondary">التفسير و الحديث الموضوعي</a>
                <a href="#" class="btn btn-secondary">الحوكمة و أخلاقيات المهنة</a>
            </div>
        </div>
        <footer>جميع الحقوق محفوظة منصة كلية الشريعة ©2026</footer>
    </body>
    </html>
    """
    return render_template_string(html_content)

# 3. صفحة إدارة محتوى المقياس ورفع الدروس (تتعامل بسلاسة مع POST لتفادي الـ 500)
@app.route('/module_manage', methods=['GET', 'POST'])
def module_manage():
    module_name = request.args.get('name', 'المقياس التعليمي')
    
    if request.method == 'POST':
        if 'lesson_file' in request.files:
            file = request.files['lesson_file']
            title = request.form.get('lesson_title', '')
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('semester5'))

    html_content = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>إدارة محتوى المقياس - منصة كلية الشريعة</title>
        <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --bg-base: #030a07;
                --gold-primary: #f3c68f;
                --gold-glow: #d4af37;
                --card-glass: rgba(10, 26, 18, 0.75);
                --border-glass: rgba(243, 198, 143, 0.18);
                --text-main: #f4f9f5;
                --text-muted: #95b8a6;
            }
            body { 
                font-family: 'Amiri', serif; background: var(--bg-base);
                background-image: 
                    radial-gradient(circle at 10% 10%, rgba(27, 67, 50, 0.5) 0%, transparent 40%),
                    radial-gradient(circle at 90% 90%, rgba(212, 175, 55, 0.12) 0%, transparent 40%),
                    radial-gradient(circle at 50% 50%, rgba(15, 42, 29, 0.8) 0%, #030a07 100%);
                margin: 0; padding: 25px 15px; text-align: center; color: var(--text-main); 
                display: flex; flex-direction: column; min-height: 85vh; justify-content: space-between; background-attachment: fixed;
            }
            .wrapper { max-width: 540px; margin: 0 auto; width: 100%; }
            .top-nav { display: flex; justify-content: flex-start; margin-bottom: 15px; }
            .back-btn {
                background: rgba(15, 42, 29, 0.7); backdrop-filter: blur(16px); color: var(--gold-primary);
                padding: 8px 16px; border-radius: 12px; text-decoration: none; font-size: 15px; font-weight: 700;
                box-shadow: 0 6px 15px rgba(0, 0, 0, 0.4); border: 1px solid var(--border-glass); display: inline-flex; align-items: center; gap: 6px; transition: 0.3s;
            }
            .back-btn:hover { background: rgba(27, 67, 50, 0.9); border-color: var(--gold-glow); color: #fff; }
            .container { 
                background: var(--card-glass); padding: 30px 22px; border-radius: 24px; 
                box-shadow: 0 30px 70px rgba(0, 0, 0, 0.6); border: 1px solid var(--border-glass); text-align: right; backdrop-filter: blur(25px);
            }
            .module-title {
                font-size: 20px; color: var(--gold-primary); margin: 0 0 18px 0; font-weight: 700; 
                border-bottom: 1px solid rgba(243, 198, 143, 0.2); padding-bottom: 10px; text-align: center; text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
            }
            .upload-box { background: rgba(15, 42, 29, 0.6); border: 1px dashed rgba(243, 198, 143, 0.35); padding: 20px; border-radius: 18px; margin-bottom: 10px; }
            .input-field {
                width: 100%; background: rgba(10, 26, 18, 0.8); border: 1px solid rgba(243, 198, 143, 0.25);
                padding: 12px 15px; border-radius: 12px; color: var(--text-main); font-family: 'Amiri', serif; font-size: 16px; box-sizing: border-box; margin-bottom: 12px; outline: none;
            }
            .input-field::placeholder { color: var(--text-muted); }
            .file-label {
                display: block; background: linear-gradient(135deg, rgba(30, 70, 52, 0.9), rgba(15, 42, 29, 0.9));
                border: 1px solid rgba(243, 198, 143, 0.3); padding: 12px; border-radius: 12px; text-align: center; color: var(--gold-primary); cursor: pointer; font-weight: 700; font-size: 16px; transition: 0.3s; margin-bottom: 12px;
            }
            .file-label:hover { background: linear-gradient(135deg, rgba(45, 106, 79, 1), rgba(30, 70, 52, 1)); border-color: var(--gold-glow); color: #fff; }
            .submit-btn {
                display: block; width: 100%; background: linear-gradient(135deg, rgba(45, 106, 79, 0.9), rgba(27, 67, 50, 1));
                color: var(--text-main); padding: 12px; border: none; border-radius: 12px; font-size: 17px; font-weight: 700; font-family: 'Amiri', serif; cursor: pointer; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3); border: 1px solid var(--border-glass); transition: 0.3s;
            }
            .submit-btn:hover { background: linear-gradient(135deg, rgba(64, 145, 108, 1), rgba(45, 106, 79, 1)); border-color: var(--gold-glow); color: #fff; }
            .no-lessons { text-align: center; color: var(--text-muted); font-size: 15px; padding: 20px 0; margin: 0; }
            footer { font-size: 13px; color: var(--text-muted); margin-top: 25px; font-weight: 700; }
        </style>
    </head>
    <body>
        <div class="wrapper">
            <div class="top-nav">
                <a href="/semester5" class="back-btn">← العودة للسداسي الخامس</a>
            </div>
            <div class="container">
                <div class="module-title">📖 إدارة محتوى: {module_name}</div>
                <div class="upload-box">
                    <form method="POST" enctype="multipart/form-data">
                        <input type="text" name="lesson_title" class="input-field" placeholder="أدخل عنوان الدرس (مثال: محاضرة المدخل للفقه)" required>
                        <label for="file-input" class="file-label">📁 اضغط لاختيار صورة أو ملف PDF</label>
                        <input type="file" id="file-input" name="lesson_file" accept="image/*,.pdf" required style="display: none;">
                        <button type="submit" class="submit-btn">نشر الدرس / الملف</button>
                    </form>
                </div>
                <p class="no-lessons">لا توجد دروس مرفوعة حتى الآن.</p>
            </div>
        </div>
        <footer>جميع الحقوق محفوظة منصة كلية الشريعة © 2026</footer>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 
