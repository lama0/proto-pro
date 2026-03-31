import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="تاريخ الملوك في المملكة العربية السعودية", layout="wide")

# تصميم CSS مخصص لتطبيق ملاحظات ميمي
st.markdown("""
    <style>
    /* خلفية التطبيق - لون أخضر باستيل مع زخرفة إسلامية بسيطة */
    .stApp {
        background-color: #f0f7f4;
        background-image: url("https://www.transparenttextures.com/patterns/arabesque.png");
    }
    
    /* تنسيق العنوان الرئيسي */
    .main-title {
        color: #1b4332;
        font-family: 'Arial', sans-serif;
        font-weight: 900;
        text-align: center;
        font-size: 45px;
        margin-bottom: 5px;
    }
    
    /* تنسيق نص التأسيس (الأبيض الصغير) */
    .sub-text {
        color: #ffffff;
        background-color: rgba(27, 67, 50, 0.4);
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-size: 18px;
        max-width: 600px;
        margin: 0 auto 30px auto;
    }

    /* تنسيق الدوائر لركائز المملكة */
    .pillar-circle {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: white;
        font-weight: bold;
        padding: 20px;
        margin: 0 auto;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        font-size: 16px;
    }

    /* ألوان درجات الأخضر للدوائر */
    .circle-1 { background-color: #2d6a4f; }
    .circle-2 { background-color: #40916c; }
    .circle-3 { background-color: #52b788; }

    /* تنسيق الزر الكبير */
    div.stButton > button {
        background-color: #1b4332 !important;
        color: white !important;
        font-size: 22px !important;
        font-weight: bold !important;
        padding: 15px 40px !important;
        border-radius: 50px !important;
        border: none !important;
        display: block;
        margin: 0 auto;
        width: 300px;
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    # العنوان
    st.markdown('<p class="main-title">تاريخ الملوك في المملكة العربية السعودية</p>', unsafe_allow_html=True)
    
    # نص التأسيس
    st.markdown('<p class="sub-text">تأسست المملكة العربية السعودية في عام 1932م على يد الملك عبدالعزيز بن عبدالرحمن آل سعود</p>', unsafe_allow_html=True)

    # قسم الصور
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1591604129939-f1efa4d9f7fa", caption="مكة المكرمة")
    with col2:
        st.image("https://images.unsplash.com/photo-1586724237569-f3d0c1dee8c6", caption="المسجد النبوي")
    with col3:
        st.image("https://images.unsplash.com/photo-1578895101408-1a36b834405b", caption="برج المملكة بالرياض")

    st.write("---")

    # ركائز المملكة على شكل دوائر
    st.markdown("<h2 style='text-align: center; color: #1b4332;'>ركائز المملكة</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="pillar-circle circle-1">مجتمع حيوي وقيم إسلامية راسخة</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="pillar-circle circle-2">اقتصاد مزدهر وقوة استثمارية</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="pillar-circle circle-3">وطن طموح وحوكمة فعالة</div>', unsafe_allow_html=True)

    st.write("<br><br>", unsafe_allow_html=True)
    
    # الزر الكبير
    if st.button("اكتشف تاريخ الملوك"):
        st.session_state.page = 'kings'
        st.rerun()

# --- صفحة الملوك ---
elif st.session_state.page == 'kings':
    st.markdown('<p class="main-title">سيرة ملوك الوطن</p>', unsafe_allow_html=True)
    
    kings_data = {
        "الملك عبدالعزيز": "توحيد البلاد، توطين البادية، وبداية استخراج النفط.",
        "الملك سعود": "تأسيس أول جامعة (جامعة الملك سعود) والتوسع في الصحة.",
        "الملك فيصل": "مشروع الري والصرف، ودعم التعليم الفني والقضايا الإسلامية.",
        "الملك خالد": "خطط التنمية الشاملة وإنشاء الهيئة الملكية للجبيل وينبع.",
        "الملك فهد": "وضع النظام الأساسي للحكم، وتوسعة الحرمين الشريفين الكبرى.",
        "الملك عبدالله": "برنامج الابتعاث الخارجي، وتطوير القضاء، والمدن الاقتصادية.",
        "الملك سلمان": "انطلاق رؤية 2030، التحول الرقمي الشامل، وقيادة الحزم."
    }

    # استخدام التبويبات لعرض الملوك
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(list(kings_data.keys()))
    tabs = [tab1, tab2, tab3, tab4, tab5, tab6, tab7]
    
    for i, king in enumerate(kings_data.keys()):
        with tabs[i]:
            st.markdown(f"<div style='background-color: white; padding: 20px; border-radius: 15px; border-left: 5px solid #1b4332; color: #1b4332;'><h3>{king}</h3><p>{kings_data[king]}</p></div>", unsafe_allow_html=True)

    if st.button("العودة للرئيسية"):
        st.session_state.page = 'home'
        st.rerun()
