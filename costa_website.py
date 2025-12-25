import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import base64
import os
import random
from datetime import datetime
import random
import time

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="My little gift", page_icon="🌺", layout="centered")

# ==========================================
# YARDIMCI FONKSİYONLAR (EN ÜSTE ALDIK)
# ==========================================
def fotoyu_kodla(dosya_yolu):
    """Bilgisayardaki fotoğrafı HTML içinde gösterilecek formata çevirir."""
    if not os.path.exists(dosya_yolu):
        return None
    with open(dosya_yolu, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

def sevgi_butonu():
    sebepler = [
        "You have the cutest smile in the whole world.",
        "You always belive in me, even when I don't.",
        "You're fucking cool.",
        "You're the best comedian ever.",
        "You make me feel at home.",
        "Your voice has a tone that clenses my soul.",
        "You are incredibly smart and talented.",
        "Your giggels melt my heart.",
        "You're the most amazing person on earth.",
        "Being human is so much easier with you by my side.",
        "You're my favorite meal",
    ]
    return sebepler

def ana_sayfa():
    st.success("Time left to our ""officializiation"" anniversary:")
    
    # Hedef tarih (Bunu kendine göre değiştir: Yıl, Ay, Gün, Saat)
    hedef_tarih = datetime(2026, 9, 14, 0, 0, 0) 
    simdi = datetime.now()
    kalan = hedef_tarih - simdi
    
    # Gün, Saat, Dakika hesaplama
    gun = kalan.days
    saat = kalan.seconds // 3600
    dakika = (kalan.seconds // 60) % 60
    
    # Ekrana Güzel Bir Kutu İçinde Yazdırma
    col1, col2, col3 = st.columns(3)
    col1.metric("Time left", f"{gun} Days")
    col2.metric("Hours", f"{saat} Hours")
    col3.metric("Minutes", f"{dakika} Minutes")
    
    st.write("---")
    return ""

# ==========================================
# 🎨 TASARIM VE RENK AYARLARI (CSS)
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #FFFDE7; border-right: 2px solid #FBC02D; }
    
    /* Genel Yazı Tipleri */
    h1, h2, h3, h4, p, label { color: #2E7D32 !important; font-family: 'Helvetica', sans-serif; }
    
    /* Radyo Butonları */
    .stRadio > div { background-color: #ffffff; padding: 10px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    
    /* --- NORMAL BUTONLAR (YEŞİL) --- */
    div.stButton > button[kind="secondary"] { 
        background-color: #43A047; 
        color: white !important; 
        border-radius: 20px; 
        border: none; 
        padding: 10px 24px; 
        font-weight: bold; 
    }
    div.stButton > button[kind="secondary"]:hover { 
        background-color: #2E7D32; 
    }

    /* --- ÖZEL SEVGİ BUTONU (GÖZ ALICI PEMBE) --- */
    div.stButton > button[kind="primary"] { 
        background-color: #FFFF8C; /* Pastel Sarı */
        color: white !important;
        border: none;
        border-radius: 50px; /* Daha yuvarlak */
        padding: 15px 30px; /* Daha büyük */
        font-size: 20px !important; /* Yazısı daha büyük */
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(233, 30, 99, 0.4); /* Parlak gölge */
        transition: all 0.3s ease;
        width: 100%; /* Mobilde tam genişlik */
    }
    
    /* Üzerine gelince efekt */
    div.stButton > button[kind="primary"]:hover { 
        background-color: #C2185B; 
        transform: scale(1.05); /* Hafif büyüme efekti */
        box-shadow: 0 6px 20px rgba(233, 30, 99, 0.6);
    }

    [data-testid="stMetricValue"] { color: #F9A825 !important; }
    .streamlit-expanderHeader { background-color: #E8F5E9; color: #2E7D32; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- MENÜ ---
st.sidebar.title("Menu 🌼")
secim = st.sidebar.radio(
    "", 
    ["🏠 Home Page", "📅 Time Tunnel", "🗺️ Our Map", "💌 Letters", "🎮 Quiz"]
)
st.sidebar.markdown("---")
st.sidebar.info("TI AMO 💛")
st.sidebar.markdown("Developed by your lover 😘")

# ==========================================
# 1. BÖLÜM: HOME PAGE
# ==========================================
if "Home Page" in secim:
    st.title("Welcome to our website ☀️")
    st.image("photos/costa_kolaj.png",use_container_width=True) 
    
    baslangic_tarihi = datetime(2025, 5, 17) 
    bugun = datetime.now()
    gecen_sure = bugun - baslangic_tarihi
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="The Days Passed Since We Met", value=f"{gecen_sure.days}")
    with col2:
        st.metric(label="Total Seconds", value=f"{gecen_sure.total_seconds():.0f}")
    
    st.success("Thank you so much for being a part of my life.")
    st.write("I designed this website to show you how much I appriciate your presence in my life, "
             "so I hope it would be a nice way to re visit some old memories or to create new ones together. 💛")
    
    st.write(ana_sayfa())
    
    if st.button("Random reasons why I love you ❤️", type="primary"):
        secilen = random.choice(sevgi_butonu())
        st.info(f"💖 {secilen}")

# ==========================================
# 2. BÖLÜM: TIME TUNNEL
# ==========================================
elif "Time Tunnel" in secim:
    st.header("A throwback to our story 📅")
    st.write("---")
    
    # def memory_card(tarih, olay, emoji,foto=None):
    #     img_html = ""
    #     if foto:
    #         kodlanmis_foto = fotoyu_kodla(foto)
    #         if kodlanmis_foto:
    #             img_html = f'<img src="{kodlanmis_foto}" style="width:100%; border-radius:10px; margin-top:10px; border: 2px solid #C5E1A5;">'

    #     st.markdown(f"""
    #     <div style="background-color: #F1F8E9; padding: 15px; border-radius: 15px; margin-bottom: 10px; border-left: 5px solid #8BC34A;">
    #         <h4 style="margin:0; color:#33691E;">{emoji} {tarih}</h4>
    #         <p style="margin:5px 0 0 0;">{olay}</p>
    #     </div>
    #     """, unsafe_allow_html=True)
    def memory_card(tarih, olay, emoji, foto=None):
    # 1. Fotoğraf HTML kodunu hazırla
        img_html = ""
        if foto:
            kodlanmis_foto = fotoyu_kodla(foto)
            if kodlanmis_foto:
                img_html = f'<img src="{kodlanmis_foto}" style="width:100%; border-radius:10px; margin-top:10px; border: 2px solid #C5E1A5;">'
            else:
                # İsteğe bağlı: Fotoğraf bulunamazsa hata mesajı bas ki görelim
                st.error(f"Fotoğraf yüklenemedi: {foto}")

        # 2. EKSİK OLAN KISIM: Kartı ekrana çizdir
        st.markdown(f"""
        <div style="background-color: #F1F8E9; padding: 15px; border-radius: 15px; margin-bottom: 10px; border-left: 5px solid #8BC34A;">
            <h4 style="margin:0; color:#33691E;">{emoji} {tarih}</h4>
            <p style="margin:5px 0 0 0;">{olay}</p>
            {img_html}
        </div>
        """, unsafe_allow_html=True)

    memory_card(f"17 May 2025", "The first time that I heard your beautiful voice.", " 🎶")
    memory_card(f"23 May 2025", "Your First ever message to me.", "💬","photos/first_msg.jpeg")
    memory_card(f"24 May 2025", "The first reels video that you sent me on instagram.", "🎥")
    memory_card(f"29 May 2025", "Day I got to learn what porca madonna meant.", "🤬","photos/porca_madonna.jpeg")
    memory_card(f"29 May 2025", "at 19:57 I made one of the best and boldest decision of my life with buying those tikets to florence.", "🎟️")
    memory_card(f"12 June 2025", "And We can't forget about \"I ReaLLy MiSs you AnD I REally WanT you, I'm DanciNg In a FounTaiN BarEfOOt.\"", "🦶🏽")
    memory_card(f"16 June 2025", "The day that I arrived in Florence for the first time, I can still remember how my legs where shaking during the train ride.", "🚆")
    memory_card(f"18 June 2025", "Night on your teras, it's one of the days that I won't foget about until I die.", "🍕")
    memory_card(f"2 July 2025", "We applied to a procject together even tho I didn't get accpeted it lead to another amazing event.", "🤗")
  

# ==========================================
# 3. BÖLÜM: OUR MAP (FOTOĞRAFLI & LİSTELİ)
# ==========================================
elif "Our Map" in secim:
    st.header("Places we have been together 🌍")
    
    m = folium.Map(location=[39.0, 30.0], zoom_start=4)

    # --- BURAYA DİKKAT: FOTOĞRAF İSİMLERİ ---
    # Klasöründeki fotoğraf isimleri buradaki 'foto' kısmıyla AYNI olmalı.
    places_we_have_been = [
        {
            "isim": "Rhodos", 
            "lat": 36.4485, "lon": 28.2278, 
            "ikon": "heart", "renk": "red", 
            "not": "The time that we felt the sea breeze together.",
            "foto": "photos/rhodos.jpg"  # Klasöründe rhodos.jpg olmalı
        },
        {
            "isim": "Florence", 
            "lat": 43.7696, "lon": 11.2558, 
            "ikon": "star", "renk": "green", 
            "not": "Seeing where you lived and then creating new memories there was an unexplainable feeling..",
            "foto": "photos/florence.jpg"     # Klasöründe florence.jpg olmalı
        },
        {
            "isim": "Bolu",
            "lat": 40.7128, "lon": 31.5788,
            "ikon": "heart", "renk": "blue",
            "not": "You made my hometown so much more special to me with that one single night.",
            "foto": "photos/Bolu.jpeg"  # Klasöründe Bolu.jpeg olmalı
        }
    ]

    for yer in places_we_have_been:
        resim_kodu = None
        # Fotoğrafı kontrol et ve kodla
        if "foto" in yer and yer["foto"]:
            resim_kodu = fotoyu_kodla(yer["foto"])
        
        if resim_kodu:
            html_icerik = f"""
            <div style="width:250px; text-align:center;">
                <h4 style="margin:5px 0; color:#2E7D32;">{yer['isim']}</h4>
                <img src="{resim_kodu}" style="width:100%; max-height:200px; object-fit:cover; border-radius:10px; margin:10px 0; border:2px solid #4CAF50;">
                <p style="font-style:italic;">{yer['not']}</p>
            </div>
            """
        else:
            html_icerik = f"<b>{yer['isim']}</b><br>{yer['not']}"

        popup = folium.Popup(html_icerik, max_width=300)
        folium.Marker(
            [yer["lat"], yer["lon"]],
            popup=popup,
            tooltip=yer["isim"],
            icon=folium.Icon(color=yer["renk"], icon=yer["ikon"], prefix="fa")
        ).add_to(m)

    st_folium(m, width=700, height=500)
    st.markdown("---") 

    # --- BUCKET LIST KISMI ---
    st.subheader("✈️ List of Places We Want to Visit Together")
    st.info("Write the name of the place you want us to visit together.")

    dosya_adi = "bucket_list.csv"
    if os.path.exists(dosya_adi):
        df = pd.read_csv(dosya_adi)
    else:
        df = pd.DataFrame(columns=["Yer", "Durum"])

    with st.form("ekleme_formu", clear_on_submit=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            yeni_yer = st.text_input("Where do you want to go?", placeholder="ex: Bali, Iceland...")
        with col2:
            st.write("") 
            st.write("")
            ekle_butonu = st.form_submit_button("Add ➕")

        if ekle_butonu:
            if yeni_yer:
                yeni_veri = pd.DataFrame({"Yer": [yeni_yer], "Durum": [False]})
                df = pd.concat([df, yeni_veri], ignore_index=True)
                df.to_csv(dosya_adi, index=False)
                st.success(f"Perfecto '{yeni_yer}' added to our list. 🎒")
                st.rerun()

    if not df.empty:
        st.write("📝 **Our List:** (When we will visit them, check the box)")
        duzenlenen_df = st.data_editor(
            df,
            column_config={
                "Durum": st.column_config.CheckboxColumn("visited?", default=False),
                "Yer": st.column_config.TextColumn("Place Name")
            },
            hide_index=True,
            num_rows="dynamic",
            key="bucket_list_editor_foto"
        )
        if not df.equals(duzenlenen_df):
            duzenlenen_df.to_csv(dosya_adi, index=False)
            st.rerun()

# ==========================================
# 4. BÖLÜM: LETTERS
# ==========================================
elif "Letters" in secim:
    st.header("Read these letter when you feel the need to 💌")
    with st.expander("open at 31st of December around midnight"):
        st.write("I will write it down later...")
    with st.expander("♥️ I will always love you"):
        st.write("I will always love you. Before meeting you, I was this guy who thought his life was going in some direction that I didn't have much control over. " \
        "But one day it all shattered. You made me realize that I was able to be loved for who I am, and even though I have defects as a person, I could be cared for. You taught me how to value myself so that I can value you. You taught an emotionally bland guy how to feel." \
        " You changed my life in a way that it's never going to be the same anymore, and I couldn't be happier about that. I love you.")
    with st.expander("🧿 Eyes of Art"):
        st.write("Your eyes are the most sacred piece of art in this world; they belong in the most well-protected and preserved museum. " \
        "I lose track of time every time I look into them. Those brown eyes with magnificent lashes could make me feel the coldness of Antarctica," \
        " the warmth of a cozy fireplace, and the hotness of the Sahara Desert with the way they look at me, and I would enjoy every single moment of those feelings.")
    with st.expander("☀️ About you"):
        st.write("You know the feeling of something feeling just right. The many moments that I had with you made me feel like that. " \
        "The way you answered me, the way you showed your love, there is just something so right and true about it. " \
        "Even the times when you're down or annoyed or whatever, there is just something that fills my head with the thought that I am with the right person. " \
        "You're making me addicted to you in many ways. I don't think that I could go a day without even seeing you now, because I would miss the part that felt right in my life." \
        " If life is about making the right or wrong decisions, you're the best decision that I have ever made.")
    with st.expander("💛 My obsession"):
        st.write("The thing that I can't get enough of, no matter how much I look at, touch, or smell it. From head to toe, you're perfect. " \
        "The way you stand, the way you walk, the way you sit. I'm in love with every single part of you. " \
        "I'm so down bad for you that even the thought of you gets me going. I can't understand how you're able to attract me this much. " \
        "You're making me blind in a way that I'm only able to see you and nothing else.")

# ==========================================
# 5. BÖLÜM: CROSSWORDS (BULMACA)
# ==========================================
elif "Quiz" in secim:
    st.header("A little quiz that I prepared that has a grand prize 🧩")
    st.write("Read the hints and try to guess the words!")
    st.markdown("---")

    # --- AYARLAR: KELİMELER VE İPUÇLARI BURAYA ---
    # Sol tarafa CEVABI, sağ tarafa İPUCUNU yaz.
    # Cevapları BÜYÜK HARFLE yazman yeterli.
    sorular = {
        "CHICKEN STORIES": "My favorite fast food restourant at rhodos?",
        "ZA CUBE": "A glorious piece of art in berlin?",
        "TRUFFLE": "The pizza topping that you had on your pizza at that night on the terrass?",
        "JUST THE TWO OF US": "The song that you sang me with the ukelele thruogh a voice message and made my whole night?",
        "KARACAYIR": "Name of the neighborhood where we had our first kiss?",
        "SENDEN BASKA": "Turkish name of the song that we sang in the taverna at Rhodos?",
        "EYES": "My favorite body part of yours?",
    }
    
    # Çözülenleri hafızada tutmak için
    if 'cozulenler' not in st.session_state:
        st.session_state.cozulenler = []

    # Soruları ekrana basma döngüsü
    for cevap, ipucu in sorular.items():
        # Eğer soru daha önce bilindiyse YEŞİL kutu göster
        if cevap in st.session_state.cozulenler:
            st.success(f"✅ {cevap} - {ipucu}")
        
        else:
            # Bilinmediyse Soru ve Input kutusu göster
            st.markdown(f"**Question:** {ipucu}")
            kullanici_cevabi = st.text_input(f"Answer ({len(cevap)} letters):", key=cevap).upper()
            
            # Kontrol Butonu (Her soru için ayrı buton olmaması için input değişimine bakıyoruz)
            if kullanici_cevabi:
                # Boşlukları sil (Örn: 'ZA CUBE' ile 'ZACUBE' aynı sayılsın)
                temiz_cevap = cevap.replace(" ", "")
                temiz_kullanici = kullanici_cevabi.replace(" ", "")
                
                if temiz_kullanici == temiz_cevap:
                    st.session_state.cozulenler.append(cevap)
                    st.balloons() # Konfeti patlat
                    st.rerun() # Sayfayı yenile ki yeşile dönsün
                else:
                    st.error("Not what I had in my mind, try again aşkım! 🤔")
            
            st.markdown("---") # Sorular arası çizgi

    # Hepsi bitti mi kontrolü
    if len(st.session_state.cozulenler) == len(sorular):
        st.info("You just won a massage session and a 1000 kisses from me. 😘")