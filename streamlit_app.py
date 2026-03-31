import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="تاريخ الملوك في المملكة العربية السعودية", layout="wide")

# تصميم CSS بلمسات أغمق وأوضح
st.markdown("""
    <style>
    .stApp {
        background-color: #e8f5e9; /* أخضر باستيل أغمق قليلاً للخلفية */
        background-image: url("https://www.transparenttextures.com/patterns/arabesque.png");
    }
    
    /* العنوان الرئيسي - أخضر غامق جداً وكبير */
    .main-title {
        color: #0a2f1f; 
        font-family: 'Arial', sans-serif;
        font-weight: 900;
        text-align: center;
        font-size: 80px !important; 
        margin-top: 40px;
        margin-bottom: 5px;
        display: block;
        width: 100%;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    /* نص التأسيس - خلفية غامقة جداً لبروز الأبيض */
    .sub-text {
        color: #ffffff !important;
        background-color: #1b4332; /* أخضر غامق ملكي */
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        font-size: 32px !important; 
        font-weight: 900;
        max-width: 1000px;
        margin: 5px auto 60px auto;
        display: block;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    /* الدوائر - درجات غامقة */
    .pillar-circle {
        width: 240px;
        height: 240px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: white !important;
        font-weight: 900;
        padding: 25px;
        margin: 20px auto;
        font-size: 24px !important;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        line-height: 1.2;
    }

    .circle-1 { background-color: #081c15; } /* أغمق درجة */
    .circle-2 { background-color: #1b4332; }
    .circle-3 { background-color: #2d6a4f; }

    /* الزر الكبير - أخضر غامق جداً */
    div.stButton > button {
        background-color: #081c15 !important;
        color: #ffffff !important;
        font-size: 32px !important;
        font-weight: 900 !important;
        padding: 25px 80px !important;
        border-radius: 60px !important;
        border: 3px solid #ffffff !important;
        display: block;
        margin: 60px auto !important;
        width: 450px !important;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background-color: #1b4332 !important;
        transform: scale(1.05);
    }

    /* تحسين شكل الصور */
    .stImage img {
        border-radius: 20px;
        border: 4px solid #1b4332;
    }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    # العنوان
    st.markdown('<h1 class="main-title">تاريخ الملوك في المملكة العربية السعودية</h1>', unsafe_allow_html=True)
    
    # نص التأسيس
    st.markdown('<div class="sub-text">تأسست المملكة العربية السعودية في عام 1932م على يد الملك عبدالعزيز بن عبدالرحمن آل سعود</div>', unsafe_allow_html=True)

    # الصور
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1542851910-85f02c61793a", caption="مكة المكرمة")
    with col2:
        st.image("https://images.unsplash.com/photo-1590074259118-439549f3e496", caption="المسجد النبوي")
    with col3:
        st.image("https://images.unsplash.com/photo-1582483540243-bd372659e99a", caption="برج المملكة بالرياض")

    st.markdown("<br><br>", unsafe_allow_html=True)

    # الركائز
    st.markdown("<h2 style='text-align: center; color: #081c15; font-size: 50px; font-weight: 900;'>ركائز المملكة</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="pillar-circle circle-1">مجتمع حيوي وقيم إسلامية راسخة</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="pillar-circle circle-2">اقتصاد مزدهر وقوة استثمارية</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="pillar-circle circle-3">وطن طموح وحوكمة فعالة</div>', unsafe_allow_html=True)

    # الزر
    if st.button("اكتشف تاريخ الملوك"):
        st.session_state.page = 'kings'
        st.rerun()

# --- صفحة الملوك ---
elif st.session_state.page == 'kings':
    st.markdown('<h1 class="main-title">سيرة ملوك الوطن</h1>', unsafe_allow_html=True)
    
    kings_data = {
        "الملك عبدالعزيز": "توحيد البلاد، توطين البادية، وبداية استخراج النفط.",
        "الملك سعود": "تأسيس أول جامعة (جامعة الملك سعود) والتوسع في الصحة.",
        "الملك فيصل": "مشروع الري والصرف، ودعم التعليم الفني والقضايا الإسلامية.",
        "الملك خالد": "خطط التنمية الشاملة وإنشاء الهيئة الملكية للجبيل وينبع.",
        "الملك فهد": "وضع النظام الأساسي للحكم، وتوسعة الحرمين الشريفين الكبرى.",
        "الملك عبدالله": "برنامج الابتعاث الخارجي، وتطوير القضاء، والمدن الاقتصادية.",
        "الملك سلمان": "انطلاق رؤية 2030، التحول الرقمي الشامل، وقيادة الحزم."
    }

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(list(kings_data.keys()))
    tabs = [tab1, tab2, tab3, tab4, tab5, tab6, tab7]
    for i, king in enumerate(kings_data.keys()):
        with tabs[i]:
            st.markdown(f"<div style='background-color: white; padding: 40px; border-radius: 20px; border-right: 15px solid #081c15; color: #081c15; font-size: 28px; font-weight: bold;'><h3>{king}</h3><p>{kings_data[king]}</p></div>", unsafe_allow_html=True)

    if st.button("العودة للرئيسية"):
        st.session_state.page = 'home'
        st.rerun()
