import streamlit as st

# 1. إعداد الصفحة وتناسق الألوان (بدون زخارف)
st.set_page_config(page_title="تاريخ ملوك المملكة", layout="wide")

st.markdown("""
    <style>
    /* خلفية باستيل أخضر غامق فخم */
    .stApp {
        background-color: #2d4c3e; 
        color: white;
    }
    
    /* العنوان الرئيسي - ضخم وعريض جداً */
    .main-title {
        color: #ffffff;
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        text-align: center;
        font-size: 80px !important;
        margin-top: 50px;
        margin-bottom: 5px;
    }
    
    /* الجملة التمهيدية - أصغر ومع مسافة */
    .sub-text-intro {
        color: #e0eae4;
        text-align: center;
        font-size: 22px !important;
        margin-top: 40px;
        margin-bottom: 80px;
        display: block;
    }

    /* تصميم البوكسات (الخانات) لأسماء الملوك */
    .king-box {
        background-color: #3d6351;
        border: 2px solid #4d7a64;
        border-radius: 25px;
        padding: 50px 20px;
        text-align: center;
        margin: 15px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .king-box:hover {
        background-color: #4d7a64;
        transform: scale(1.02);
        border-color: #ffffff;
    }
    .king-box h2 {
        color: white !important;
        font-size: 45px !important;
        font-weight: 800 !important;
    }

    /* الدوائر لركائز المملكة */
    .pillar-circle {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        background-color: #1a3c2e;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin: 20px auto;
        padding: 20px;
        font-size: 20px;
        font-weight: bold;
        border: 4px solid #52b788;
    }

    /* الزر الكبير (اكتشف / عودة) */
    div.stButton > button {
        background-color: #1a3c2e !important;
        color: white !important;
        font-size: 26px !important;
        font-weight: bold !important;
        padding: 15px 50px !important;
        border-radius: 50px !important;
        border: 2px solid #ffffff !important;
        display: block;
        margin: 50px auto !important;
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_king' not in st.session_state:
    st.session_state.selected_king = None

# بيانات الملوك (المحتوى التفصيلي)
KING_DETAILS = {
    "الملك عبدالعزيز": {
        "image": "https://static.majalla.com/styles/1200xauto/public/2023-09/159277.jpeg?VersionId=XTJ5e4r0bMAqk5h0vOHxBaHqC8Fpjzoe",
        "bio": "مؤسس المملكة وموحدها، استعاد الرياض عام 1319هـ وأعلن توحيد المملكة عام 1351هـ. وضع أسس الإدارة والتعليم والاقتصاد."
    },
    "الملك سعود": {
        "image": "https://www.marefa.org/w/images/b/b9/Saud.jpg",
        "bio": "شهد عهده نهضة تعليمية كبرى بتأسيس أول جامعة، وتوسعة الحرمين الشريفين، وإنشاء العديد من الوزارات."
    },
    "الملك فيصل": {
        "image": "https://www.qpedia.org//public/topics/1615201503.jpg",
        "bio": "رائد التضامن الإسلامي، طور التعليم والزراعة وأنشأ مشروع الري والصرف بالأحساء."
    },
    "الملك خالد": {
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgz3MT_fTLBRivU83q73_vvtKW5mP9Oc8dfw&s",
        "bio": "تميز عهده بالرخاء الاقتصادي، وإنشاء الهيئة الملكية للجبيل وينبع، ودعم خطط التنمية الخمسية."
    },
    "الملك فهد": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Fahd_of_Saudi_Arabia_Portrait.jpg/250px-Fahd_of_Saudi_Arabia_Portrait.jpg",
        "bio": "خادم الحرمين الشريفين، أصدر النظام الأساسي للحكم، ونفذ أكبر توسعة تاريخية للحرمين الشريفين."
    },
    "الملك عبدالله": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/98/Abdullah_of_Saudi_Arabia.jpg",
        "bio": "أطلق برنامج الابتعاث الخارجي، وأسس جامعة الملك عبدالله للعلوم والتقنية، وطور منظومة القضاء."
    },
    "الملك سلمان": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/%D8%A7%D9%84%D8%B5%D9%88%D8%B1%D8%A9_%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A%D8%A9_%D9%84%D8%AE%D8%A7%D8%AF%D9%85_%D8%A7%D9%84%D8%AD%D8%B1%D9%85%D9%8A%D9%86_%D8%A7%D9%84%D8%B4%D8%B1%D9%8A%D9%81%D9%8A%D9%86_%D8%A7%D9%84%D9%85%D9%84%D9%83_%D8%B3%D9%84%D9%85%D8%A7%D9%86_%D8%A8%D9%86_%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B9%D8%B2%D9%8A%D8%B2_%D8%A2%D9%84_%D8%B3%D8%B9%D9%88%D8%AF.jpg/330px-%D8%A7%D9%84%D8%B5%D9%88%D8%B1%D8%A9_%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A%D8%A9_%D9%84%D8%AE%D8%A7%D8%AF%D9%85_%D8%A7%D9%84%D8%AD%D8%B1%D9%85%D9%8A%D9%86_%D8%A7%D9%84%D8%B4%D8%B1%D9%8A%D9%81%D9%8A%D9%86_%D8%A7%D9%84%D9%85%D9%84%D9%83_%D8%B3%D9%84%D9%85%D8%A7%D9%86_%D8%A8%D9%86_%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B9%D8%B2%D9%8A%D8%B2_%D8%A2%D9%84_%D8%B3%D8%B9%D9%88%D8%AF.jpg",
        "bio": "قائد التحول التاريخي، انطلقت في عهده رؤية 2030، وشهدت المملكة تمكيناً غير مسبوق للشباب والمرأة."
    }
}

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    st.markdown('<h1 class="main-title">تاريخ الملوك</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text-intro">تأسست المملكة العربية السعودية في عام 1932م على يد الملك عبدالعزيز بن عبدالرحمن آل سعود</p>', unsafe_allow_html=True)

    # صور المعالم
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://makkah-madinah.accor.com/wp-content/uploads/2024/08/004-Kaaba-Makkah1.jpgا", caption="مكة المكرمة")
    with col2:
        st.image("https://blog.bayut.sa/uploads/2024/06/Body_01-49-1024x640.jpg", caption="برج التحلية")
    with col3:
        st.image("https://saudipedia.com/var/site/storage/images/0/8/5/8/5238580-1-ara-SA/a55fbe324284-88564.jpg", caption="برج المملكة - الرياض")

    st.write("<br><hr><br>", unsafe_allow_html=True)
    
    # الركائز (الدوائر)
    st.markdown("<h2 style='text-align: center; font-size: 40px;'>ركائز المملكة</h2>", unsafe_allow_html=True)
    r1, r2, r3 = st.columns(3)
    with r1: st.markdown('<div class="pillar-circle">مجتمع حيوي</div>', unsafe_allow_html=True)
    with r2: st.markdown('<div class="pillar-circle">اقتصاد مزدهر</div>', unsafe_allow_html=True)
    with r3: st.markdown('<div class="pillar-circle">وطن طموح</div>', unsafe_allow_html=True)

    if st.button("اكتشف تاريخ الملوك"):
        st.session_state.page = 'list'
        st.rerun()

# --- صفحة قائمة الملوك (البوكسات) ---
elif st.session_state.page == 'list':
    st.markdown('<h1 class="main-title">ملوك المملكة</h1>', unsafe_allow_html=True)
    
    # عرض كل ملك في بوكس لحاله
    for king in KING_DETAILS.keys():
        st.markdown(f'<div class="king-box"><h2>{king}</h2></div>', unsafe_allow_html=True)
        if st.button(f"عرض تفاصيل {king}", key=king):
            st.session_state.selected_king = king
            st.session_state.page = 'details'
            st.rerun()
            
    if st.button("العودة للرئيسية"):
        st.session_state.page = 'home'
        st.rerun()

# --- صفحة الملك التفصيلية ---
elif st.session_state.page == 'details':
    name = st.session_state.selected_king
    king = KING_DETAILS[name]
    
    st.markdown(f'<h1 class="main-title">{name}</h1>', unsafe_allow_html=True)
    
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        st.image(king["image"], use_container_width=True)
    with col_txt:
        st.markdown(f"<div style='background: #3d6351; padding: 40px; border-radius: 20px; font-size: 26px; line-height: 1.8;'>{king['bio']}</div>", unsafe_allow_html=True)
    
    if st.button("العودة لقائمة الملوك"):
        st.session_state.page = 'list'
        st.rerun()
