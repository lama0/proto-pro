import streamlit as st

# 1. إعداد الصفحة الأساسية لتكون عريضة
st.set_page_config(page_title="تاريخ ملوك المملكة", layout="wide")

# 2. تصميم CSS مكثف واحترافي لتحقيق الرؤية التصميمية لميمي
st.markdown("""
    <style>
    /* خلفية التطبيق - لون أخضر باستيل غامق فخم (بدون زخارف) */
    .stApp {
        background-color: #e0eae4; /* Olive Pastle */
    }
    
    /* تنسيق العنوان الرئيسي العلوي */
    .main-title {
        color: #1a3c2e;
        font-family: 'Arial', sans-serif;
        font-weight: 900;
        text-align: center;
        font-size: 70px !important;
        margin-top: 60px;
        margin-bottom: 20px;
        display: block;
        width: 100%;
    }
    
    /* تنسيق الجملة التمهيدية البيضاء (أصغر ومع مسافة) */
    .sub-text-intro {
        color: #ffffff;
        background-color: #1a3c2e;
        padding: 20px 40px;
        border-radius: 20px;
        text-align: center;
        font-size: 24px !important;
        font-weight: bold;
        max-width: 900px;
        margin: 20px auto 60px auto; /* مسافة كبيرة بالأسفل */
        display: block;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    /* تنسيق الدوائر لركائز المملكة */
    .pillar-circle {
        width: 240px;
        height: 240px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: white;
        font-weight: bold;
        padding: 25px;
        margin: 30px auto;
        font-size: 22px !important;
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        transition: transform 0.3s ease;
    }
    .pillar-circle:hover {
        transform: scale(1.05);
    }
    .circle-1 { background-color: #1a3c2e; }
    .circle-2 { background-color: #2d6a4f; }
    .circle-3 { background-color: #40916c; }

    /* تنسيق البطاقات (Boxes) لأسماء الملوك */
    .king-card {
        background-color: #1a3c2e;
        color: white;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        margin: 15px 0;
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease, transform 0.2s ease;
        cursor: pointer;
    }
    .king-card:hover {
        background-color: #2d6a4f;
        transform: translateY(-5px);
    }
    .king-name {
        font-size: 40px !important;
        font-weight: 900;
        margin: 0;
    }

    /* تنسيق الأزرار (اكتشف، عودة) */
    div.stButton > button {
        background-color: #1a3c2e !important;
        color: white !important;
        font-size: 28px !important;
        font-weight: bold !important;
        padding: 20px 70px !important;
        border-radius: 50px !important;
        border: none !important;
        display: block;
        margin: 60px auto !important;
        width: auto !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    div.stButton > button:hover {
        background-color: #2d6a4f !important;
    }
    
    /* تنسيق صفحة الملك التفصيلية */
    .king-detail-container {
        background-color: white;
        padding: 40px;
        border-radius: 25px;
        border-right: 15px solid #1a3c2e;
        color: #1a3c2e;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. بيانات الملوك التفصيلية (تم توسيعها وتدقيقها)
KING_DETAILS = {
    "الملك عبدالعزيز": {
        "title": "الملك عبدالعزيز بن عبدالرحمن آل سعود (المؤسس)",
        "image": "https://raw.githubusercontent.com/lama0/proto-pro/main/images/king_abdulaziz.jpg",
        "description": "قاد كفاحاً طويلاً لتوحيد البلاد، بدأه باستعادة الرياض عام 1319هـ. أعلن قيام المملكة العربية السعودية عام 1351هـ. وضع أسس الدولة الحديثة، وركز على توطين البادية واستخراج النفط."
    },
    "الملك سعود": {
        "title": "الملك سعود بن عبدالعزيز آل سعود",
        "image": "https://raw.githubusercontent.com/lama0/proto-pro/main/images/king_saud.jpg",
        "description": "واصل مسيرة البناء بعد والده، شهد عهده قفزة في التعليم والصحة. أسس جامعة الملك سعود (أول جامعة بالمملكة)، ووسع المسجد الحرام والمسجد النبوي."
    },
    "الملك فيصل": {
        "title": "الملك فيصل بن عبدالعزيز آل سعود",
        "image": "https://raw.githubusercontent.com/lama0/proto-pro/main/images/king_faisal.jpg",
        "description": "عُرف بحكمته ودعمه للقضايا الإسلامية. أنشأ مشروع الري والصرف بالأحساء، واهتم بالتعليم الفني، وقاد تضامناً إسلامياً واسعاً."
    },
    "الملك خالد": {
        "title": "الملك خالد بن عبدالعزيز آل سعود",
        "image": "https://raw.githubusercontent.com/lama0/proto-pro/main/images/king_khaled.jpg",
        "description": "شهد عهده رخاءً اقتصادياً، ونُفذت خطط تنموية شاملة. أسس الهيئة الملكية للجبيل وينبع، واهتم بتحسين مستوى معيشة المواطنين."
    },
    "الملك فهد": {
        "title": "الملك فهد بن عبدالعزيز آل سعود",
        "image": "https://raw.githubusercontent.com/lama0/proto-pro/main/images/king_fahd.jpg",
        "description": "أول من اتخذ لقب 'خادم الحرمين الشريفين'. وضع النظام الأساسي للحكم، ونفذ أكبر توسعة للحرمين، وطوّر التعليم العالي."
    },
    "الملك عبدالله": {
        "title": "الملك عبدالله بن عبدالعزيز آل سعود",
        "image": "https://raw.githubusercontent.com/lama0/proto-pro/main/images/king_abdullah.jpg",
        "description": "أطلق برنامج خادم الحرمين للابتعاث الخارجي، وأسس المدن الاقتصادية، وطوّر نظام القضاء، وشجع الحوار بين الأديان والثقافات."
    },
    "الملك سلمان": {
        "title": "الملك سلمان بن عبدالعزيز آل سعود",
        "image": "https://raw.githubusercontent.com/lama0/proto-pro/main/images/king_salman.jpg",
        "description": "قائد الحزم والعزم، في عهده انطلقت 'رؤية المملكة 2030' الطموحة بقيادة سمو ولي العهد. شهدت المملكة تحولاً رقمياً شاملاً، وتطوراً في كافة المجالات."
    }
}

# 4. إدارة الصفحات باستخدام Session State
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'selected_king' not in st.session_state:
    st.session_state.selected_king = None

def go_to_page(page_name):
    st.session_state.current_page = page_name
    st.rerun()

def select_king(king_name):
    st.session_state.selected_king = king_name
    st.session_state.current_page = 'king_detail'
    st.rerun()

# ==========================================
#                  الصفحات
# ==========================================

# --- الصفحة الرئيسية ---
if st.session_state.current_page == 'home':
    # العنوان الكبير
    st.markdown('<h1 class="main-title">تاريخ الملوك في المملكة العربية السعودية</h1>', unsafe_allow_html=True)
    
    # الجملة التمهيدية البيضاء (أصغر وتحتها مسافة)
    st.markdown('<div class="sub-text-intro">تأسست المملكة العربية السعودية في عام 1932م على يد الملك عبدالعزيز بن عبدالرحمن آل سعود</div>', unsafe_allow_html=True)

    # قسم الصور المطلوبة (روابط محدثة وموثوقة لضمان الظهور)
    col_img1, col_img2, col_img3 = st.columns(3)
    with col_img1:
        st.image("https://images.unsplash.com/photo-1591604129939-f1efa4d9f7fa", caption="مكة المكرمة")
    with col_img2:
        st.image("https://images.unsplash.com/photo-1590074259118-439549f3e496", caption="المسجد النبوي")
    with col_img3:
        st.image("https://images.unsplash.com/photo-1582483540243-bd372659e99a", caption="برج المملكة بالرياض")

    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    # ركائز المملكة على شكل دوائر (بخط أكبر)
    st.markdown("<h2 style='text-align: center; color: #1a3c2e; font-size: 50px; font-weight: 900;'>ركائز المملكة</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="pillar-circle circle-1">مجتمع حيوي وقيم إسلامية راسخة</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="pillar-circle circle-2">اقتصاد مزدهر وقوة استثمارية</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="pillar-circle circle-3">وطن طموح وحوكمة فعالة</div>', unsafe_allow_html=True)

    # الزر الكبير للذهاب لصفحة الملوك
    if st.button("اكتشف تاريخ الملوك ⬇️"):
        go_to_page('kings_menu')

# --- صفحة قائمة الملوك (البطاقات) ---
elif st.session_state.current_page == 'kings_menu':
    st.markdown('<h1 class="main-title">سيرة ملوك الوطن</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #1a3c2e; font-size: 24px;'>اضغط على اسم الملك لاستعراض سيرته التفصيلية وصورته</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # عرض الملوك كبطاقات قابلة للضغط
    # نستخدم الحلقات (Loops) لإنشاء البطاقات بشكل مرتب
    for king_name in KING_DETAILS.keys():
        col_king, _ = st.columns([1, 1]) # نضع البطاقة في عمود واحد لتأخذ عرض الصفحة
        with col_king:
            st.markdown(f'<div class="king-card"><p class="king-name">{king_name}</p></div>', unsafe_allow_html=True)
            # زر مخفي خلف البطاقة للضغط
            if st.button(f"عرض سيرة {king_name}", key=king_name, use_container_width=True):
                select_king(king_name)
    
    # زر العودة للرئيسية
    if st.button("🏠 العودة للصفحة الرئيسية"):
        go_to_page('home')

# --- صفحة الملك التفصيلية ---
elif st.session_state.current_page == 'king_detail':
    king_name = st.session_state.selected_king
    if king_name:
        king_info = KING_DETAILS[king_name]
        
        st.markdown(f'<h1 class="main-title">{king_info["title"]}</h1>', unsafe_allow_html=True)
        
        # تنسيق الصفحة التفصيلية (صورة الملك + الكلام)
        col_king_img, col_king_text = st.columns([1, 2], gap="large")
        
        with col_king_img:
            # صورة الملك (نحاول تحميلها، وإذا لم تظهر نضع علامة)
            st.image(king_info["image"], use_container_width=True)
            
        with col_king_text:
            st.markdown(f'<div class="king-detail-container">', unsafe_allow_html=True)
            st.markdown(f"<h2>أبرز الإنجازات</h2>", unsafe_allow_html=True)
            # نكتب الكلام بشكل منسق بدلاً من st.write لضمان الحجم
            for line in king_info["description"].split('، '):
                st.markdown(f"<p style='font-size: 22px; line-height: 1.6;'>✅ {line}</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # أزرار العودة
        col_back1, col_back2 = st.columns(2)
        with col_back1:
            if st.button("👑 العودة لقائمة الملوك"):
                go_to_page('kings_menu')
        with col_back2:
            if st.button("🏠 العودة للصفحة الرئيسية"):
                go_to_page('home')
