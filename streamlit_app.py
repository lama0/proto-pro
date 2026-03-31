import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="موطني مجد وعلياء", page_icon="🇸🇦", layout="wide")

# 2. نظام التنقل (Navigation) باستخدام Session State
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to_kings():
    st.session_state.page = 'kings'

def go_to_home():
    st.session_state.page = 'home'

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    st.title("🇸🇦 المملكة العربية السعودية: قصة مجد")
    
    # مقدمة بسيطة
    st.markdown("""
    ### مقدمة تاريخية
    تأسست المملكة العربية السعودية الحديثة على يد الملك عبدالعزيز بن عبدالرحمن آل سعود عام 1932م. 
    هي أرض الحرمين الشريفين، وقبلة المسلمين، ومنارة الاقتصاد العالمي.
    """)
    
    st.divider()

    # صور للمملكة (Grid)
    st.subheader("📸 صور من بلادي")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1591604129939-f1efa4d9f7fa", caption="مكة المكرمة")
    with col2:
        st.image("https://images.unsplash.com/photo-1586724237569-f3d0c1dee8c6", caption="المدينة المنورة")
    with col3:
        st.image("https://images.unsplash.com/photo-1578895101408-1a36b834405b", caption="العاصمة الرياض")

    st.divider()

    # ركائز الرؤية وأهدافها
    st.subheader("🚀 رؤية المملكة 2030")
    r1, r2, r3 = st.columns(3)
    with r1:
        st.info("### مجتمع حيوي\nتركيز على جودة الحياة والحرمين الشريفين.")
    with r2:
        st.success("### اقتصاد مزدهر\nتنوع مصادر الدخل ودعم الابتكار والشباب.")
    with r3:
        st.warning("### وطن طموح\nحكومة فاعلة ومواطن مسؤول للمستقبل.")

    # زر الانتقال لصفحة الملوك
    st.write("---")
    st.button("اكتشف تاريخ الملوك ⬅️", on_click=go_to_kings)

# --- صفحة الملوك ---
elif st.session_state.page == 'kings':
    st.title("👑 ملوك المملكة العربية السعودية")
    st.write("اضغط على اسم الملك لاستعراض أبرز إنجازاته")

    kings_data = {
        "الملك عبدالعزيز": "توحيد البلاد، توطين البادية، وبداية استخراج النفط.",
        "الملك سعود": "تأسيس أول جامعة (جامعة الملك سعود) والتوسع في الصحة.",
        "الملك فيصل": "مشروع الري والصرف، ودعم التعليم الفني.",
        "الملك خالد": "خطط التنمية الشاملة وإنشاء الهيئة الملكية للجبيل وينبع.",
        "الملك فهد": "النظام الأساسي للحكم، وتوسعة الحرمين الشريفين الكبرى.",
        "الملك عبدالله": "برنامج الابتعاث الخارجي، وتطوير القضاء، والمدن الاقتصادية.",
        "الملك سلمان": "انطلاق رؤية 2030، التحول الرقمي الشامل، وقيادة الحزم."
    }

    # عرض الملوك في خانات (Tabs)
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(list(kings_data.keys()))

    tabs = [tab1, tab2, tab3, tab4, tab5, tab6, tab7]
    for i, king in enumerate(kings_data.keys()):
        with tabs[i]:
            st.success(f"### أبرز إنجازات {king}")
            st.write(kings_data[king])

    # أزرار العودة
    st.divider()
    col_back1, col_back2 = st.columns(2)
    with col_back1:
        st.button("🏠 العودة للصفحة الرئيسية", on_click=go_to_home)
