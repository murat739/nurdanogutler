from datetime import datetime
import unicodedata
import streamlit as st

# ================================================================================
# 1. SAYFA YAPILANDIRMASI
# ================================================================================
st.set_page_config(
    page_title="Derin İlim: Hikmet Arşivi / Archive of Wisdom",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ================================================================================
# 2. DİL SEÇİMİ VE ÇEVİRİ SÖZLÜĞÜ (i18n)
# ================================================================================
if "lang" not in st.session_state:
    st.session_state["lang"] = "TR"

lang_choice = st.sidebar.selectbox(
    "🌐 Dil / Language",
    options=["TR", "EN"],
    index=0 if st.session_state["lang"] == "TR" else 1,
    key="lang_selectbox",
)

st.session_state["lang"] = lang_choice
lang = st.session_state["lang"]

# Arayüz Metinleri Sözlüğü
translations = {
    "TR": {
        "page_title": "📚 Derin İlim: Hikmet ve Tefekkür Arşivi",
        "page_subtitle": "Tasavvuf büyüklerinin, İslam alimlerinin hikmetli sözleri, Kur'an-ı Kerim ayetleri ve nebevi rehberliklerin tahkikli buluşma noktası.",
        "search_label": "🔍 İçerik Ara (Zat, Söz, Ayet, Hadis veya Kaynak):",
        "search_placeholder": "Aramak istediğiniz kelimeyi yazın...",
        "select_person": "Hakikatine Müracaat Edilecek Zât:",
        "all_option": "Tümü",
        "no_results": "Aradığınız kriterlere uygun sonuç bulunamadı.",
        "results_found": "Arama kriterlerinize uygun **{}** kayıt bulundu.",
        "word_title": "📜 Hikmetli Söz",
        "verse_title": "📖 İlahi Kelam (Ayet-i Kerime)",
        "hadith_title": "☀️ Nebevi Işık (Hadis-i Şerif)",
        "source_label": "Kaynak",
        "category_label": "Kategori",
        "item_id": "Kayıt #",
        "sidebar_title": "📌 Sistem Güvencesi",
        "info_note": "Bu arşiv, İslam düşünce tarihi ve tasavvuf büyüklerinin hikmetli sözlerini, ayet ve hadislerle tahkik ederek bir araya getiren akademik ve manevi bir çalışmadır.",
        "legal_warning_title": "⚖️ Yasal Uyarı ve Sorumluluk Reddi",
        "legal_warning_body": "Bu arşivde yer alan ayet mealleri, hadis-i şerifler, İslam alimleri ve tasavvuf büyüklerinin sözleri tamamen irşat, tefekkür, ilmi araştırma ve bilgilendirme amaçlı olarak derlenmiştir. Sunulan içeriklerin doğruluğu, akademik tahkiki veya yorum farkları tamamen kaynak eserlerin kendi literatürüne dayanmaktadır.",
        "daily_guide_title": "🗓️ Günün Rehberi",
        "daily_climate": "\"{}\" iklimi.",
    },
    "EN": {
        "page_title": "📚 Deep Knowledge: Archive of Wisdom & Contemplation",
        "page_subtitle": "A verified meeting point of wise sayings of Sufi masters, Islamic scholars, Holy Qur'an verses, and prophetic guidance.",
        "search_label": "🔍 Search Content (Person, Saying, Verse, Hadith, or Source):",
        "search_placeholder": "Type keyword to search...",
        "select_person": "Select Scholar / Master:",
        "all_option": "All",
        "no_results": "No results found matching your criteria.",
        "results_found": "**{}** entries found matching your criteria.",
        "word_title": "📜 Wise Saying",
        "verse_title": "📖 Divine Word (Qur'anic Verse)",
        "hadith_title": "☀️ Prophetic Light (Hadith)",
        "source_label": "Source",
        "category_label": "Category",
        "item_id": "Entry #",
        "sidebar_title": "📌 System Assurance",
        "info_note": "This archive is an academic and spiritual work that brings together the wise sayings of Islamic thought history and Sufi masters, verified with verses and hadiths.",
        "legal_warning_title": "⚖️ Disclaimer & Legal Notice",
        "legal_warning_body": "The Quranic verses, hadiths, and sayings of Islamic scholars and Sufi masters in this archive are compiled solely for guidance, contemplation, and academic research purposes. Content accuracy relies on referenced literature.",
        "daily_guide_title": "🗓️ Daily Guide",
        "daily_climate": "Climate of \"{}\".",
    },
}


def t(key):
    return translations[lang].get(key, key)


def akilli_temizle(metin):
    if not metin:
        return ""
    metin = metin.lower()
    return "".join(
        c
        for c in unicodedata.normalize("NFD", metin)
        if unicodedata.category(c) != "Mn"
    )


# ================================================================================
# 3. VERİ KÜMESİ (TR & EN ÇİFT DİLLİ TAM ARŞİV)
# ================================================================================
DERIN_ILIM_ARSIVI = [
    {
        "id": 1,
        "tr": {
            "zat": "Bediüzzaman Said Nursi",
            "unvan": "Bediüzzaman -kuddise sırruh-",
            "kategori": "Sabır ve Şükür",
            "soz": "Musibet, sabır içinde şükrettirir; şükür içinde sabır ister.",
            "soz_kaynagi": "Lem'alar, On Yedinci Lem'a",
            "ayet": "Şüphesiz sabredenlere mükafatları hesapsız olarak ödenir.",
            "ayet_kaynagi": "Zümer Suresi, 10. Ayet",
            "hadis": "Müminin durumu ne gariptir! Onun her işi hayırdır... Eğer başına bir sevinç gelirse şükreder, bu onun için hayır olur; bir sıkıntı gelirse sabreder, bu da onun için hayır olur.",
            "hadis_kaynagi": "Müslim, Zühd, 64",
        },
        "en": {
            "zat": "Bediuzzaman Said Nursi",
            "unvan": "Bediuzzaman -may his secret be sanctified-",
            "kategori": "Patience and Gratitude",
            "soz": "Calamity evokes gratitude within patience, and demands patience within gratitude.",
            "soz_kaynagi": "The Flashes, Seventeenth Flash",
            "ayet": "Only those who are patient will be given their reward without account.",
            "ayet_kaynagi": "Surah Az-Zumar, Verse 10",
            "hadis": "How wonderful is the affair of the believer! Every affair of his is good... If prosperity comes to him, he expresses gratitude and it is good for him; if adversity befalls him, he endures it patiently and it is good for him.",
            "hadis_kaynagi": "Muslim, Asceticism, 64",
        },
    },
    {
        "id": 2,
        "tr": {
            "zat": "Şeyh Halil Fevzi",
            "unvan": "Halil Fevzi Efendi -kuddise sırruh-",
            "kategori": "Teslimiyet ve Sadakat",
            "soz": "Hakk'ın kazasına rıza göstermek, kalbin en büyük zenginliğidir.",
            "soz_kaynagi": "Divan-ı Halil",
            "ayet": "...Allah'a dayanın. Eğer müminlerseniz.",
            "ayet_kaynagi": "Maide Suresi, 23. Ayet",
            "hadis": "İşlerin hayırlısı orta olanıdır. Kim Allah'a tevekkül ederse, O ona kafidir.",
            "hadis_kaynagi": "Taberani",
        },
        "en": {
            "zat": "Shaykh Khalil Fawzi",
            "unvan": "Khalil Fawzi Efendi -may his secret be sanctified-",
            "kategori": "Submission and Loyalty",
            "soz": "Consenting to the decree of the Truth is the greatest wealth of the heart.",
            "soz_kaynagi": "Divan of Khalil",
            "ayet": "...And upon Allah rely, if you should be believers.",
            "ayet_kaynagi": "Surah Al-Ma'idah, Verse 23",
            "hadis": "The best of affairs is the moderate one. Whoever relies upon Allah, He is sufficient for him.",
            "hadis_kaynagi": "Tabarani",
        },
    },
    {
        "id": 3,
        "tr": {
            "zat": "Mevlana Celaleddin Rumi",
            "unvan": "Hz. Mevlana -kuddise sırruh-",
            "kategori": "Aşk ve Marifet",
            "soz": "Kusur arıyorsan, bütün aynalar senindir.",
            "soz_kaynagi": "Mesnevi",
            "ayet": "Kendi nefislerinizde de deliller vardır; hâlâ görmez misiniz?",
            "ayet_kaynagi": "Zâriyât Suresi, 21. Ayet",
            "hadis": "Ameller niyetlere göredir.",
            "hadis_kaynagi": "Buhari, Bed'ü'l-Vahy, 1",
        },
        "en": {
            "zat": "Mawlana Jalaluddin Rumi",
            "unvan": "Mawlana Rumi -may his secret be sanctified-",
            "kategori": "Love and Gnosis",
            "soz": "If you are looking for faults, all mirrors belong to you.",
            "soz_kaynagi": "Masnavi",
            "ayet": "And on the earth are signs for the certain in faith, and in your own selves. Then will you not see?",
            "ayet_kaynagi": "Surah Adh-Dhariyat, Verse 21",
            "hadis": "Actions are judged by intentions.",
            "hadis_kaynagi": "Bukhari, Revelation, 1",
        },
    },
    {
        "id": 4,
        "tr": {
            "zat": "Yunus Emre",
            "unvan": "Anadolu'nun Gönül Dili -kuddise sırruh-",
            "kategori": "İnsan ve Muhabbet",
            "soz": "Yaradılanı severiz, Yaradandan ötürü.",
            "soz_kaynagi": "Risaletü'n-Nushiyye",
            "ayet": "Şüphesiz müminler ancak kardeştirler.",
            "ayet_kaynagi": "Hucurât Suresi, 10. Ayet",
            "hadis": "İman etmedikçe cennete giremezsiniz; birbirinizi sevmedikçe iman etmiş olmazsınız.",
            "hadis_kaynagi": "Müslim, İman, 93",
        },
        "en": {
            "zat": "Yunus Emre",
            "unvan": "Spiritual Voice of Anatolia -may his secret be sanctified-",
            "kategori": "Humanity and Love",
            "soz": "We love the created for the sake of the Creator.",
            "soz_kaynagi": "Risalat al-Nushiyyah",
            "ayet": "The believers are but brothers, so make settlement between your brothers.",
            "ayet_kaynagi": "Surah Al-Hujurat, Verse 10",
            "hadis": "You will not enter Paradise until you believe, and you will not believe until you love one another.",
            "hadis_kaynagi": "Muslim, Faith, 93",
        },
    },
    {
        "id": 5,
        "tr": {
            "zat": "Hacı Bektaş-ı Veli",
            "unvan": "Hacı Bektaş -kuddise sırruh-",
            "kategori": "Edep ve İlim",
            "soz": "İlim suretten hakikate geçiş köprüsüdür. En büyük keramet ahlaktır.",
            "soz_kaynagi": "Makalat",
            "ayet": "İyilikle kötülük bir olmaz. Sen kötülüğü en güzel olanla sav.",
            "ayet_kaynagi": "Fussilet Suresi, 34. Ayet",
            "hadis": "Mümin, elinden ve dilinden diğer müminlerin güvende olduğu kişidir.",
            "hadis_kaynagi": "Buhari, İman, 4",
        },
        "en": {
            "zat": "Haji Bektash Veli",
            "unvan": "Haji Bektash -may his secret be sanctified-",
            "kategori": "Manners and Knowledge",
            "soz": "Knowledge is a bridge from form to truth. The greatest miracle is good character.",
            "soz_kaynagi": "Makalat",
            "ayet": "And not equal are the good deed and the bad. Repel [evil] by that which is better.",
            "ayet_kaynagi": "Surah Fussilat, Verse 34",
            "hadis": "A believer is the one from whose tongue and hand other believers are safe.",
            "hadis_kaynagi": "Bukhari, Faith, 4",
        },
    },
    {
        "id": 6,
        "tr": {
            "zat": "Hasan-ı Basri",
            "unvan": "Tabiûnun Büyük Zâhidi -rahmetullahi aleyh-",
            "kategori": "Zühd ve Takva",
            "soz": "Dünya müminin zindanı, kafirin cennetidir. Ahiret ise bunun tersidir.",
            "soz_kaynagi": "Hilyetü'l-Evliyâ",
            "ayet": "Dünya hayatı ancak bir oyun ve eğlenceden ibarettir.",
            "ayet_kaynagi": "Ankebût Suresi, 64. Ayet",
            "hadis": "Dünyada sanki bir garip veya yolcu gibi ol.",
            "hadis_kaynagi": "Buhari, Rikāk, 3",
        },
        "en": {
            "zat": "Hasan al-Basri",
            "unvan": "Great Ascetic of Tabi'un -may Allah have mercy on him-",
            "kategori": "Asceticism and Piety",
            "soz": "The world is a prison for the believer and a paradise for the disbeliever. The hereafter is the opposite.",
            "soz_kaynagi": "Hilyat al-Awliya",
            "ayet": "And this worldly life is not but diversion and amusement.",
            "ayet_kaynagi": "Surah Al-Ankabut, Verse 64",
            "hadis": "Be in this world as if you were a stranger or a traveler.",
            "hadis_kaynagi": "Bukhari, Softening the Heart, 3",
        },
    },
    {
        "id": 7,
        "tr": {
            "zat": "Ahmed Yesevi",
            "unvan": "Pir-i Türkistan -kuddise sırruh-",
            "kategori": "Hikmet ve Hizmet",
            "soz": "Gönül kırıp can incitmekten sakın; hakikatte her can bir emanettir.",
            "soz_kaynagi": "Divan-ı Hikmet",
            "ayet": "Müminler ancak kardeştirler, kardeşlerinizin arasını düzeltin.",
            "ayet_kaynagi": "Hucurât Suresi, 10. Ayet",
            "hadis": "Müslüman, elinden ve dilinden Müslümanların güvende olduğu kimsedir.",
            "hadis_kaynagi": "Buhari, İman, 4",
        },
        "en": {
            "zat": "Ahmad Yasawi",
            "unvan": "Master of Turkestan -may his secret be sanctified-",
            "kategori": "Wisdom and Service",
            "soz": "Refrain from breaking hearts and hurting souls; in truth, every soul is a trust.",
            "soz_kaynagi": "Divan-i Hikmet",
            "ayet": "The believers are but brothers, so make settlement between your brothers.",
            "ayet_kaynagi": "Surah Al-Hujurat, Verse 10",
            "hadis": "A Muslim is the one from whose tongue and hand other Muslims are safe.",
            "hadis_kaynagi": "Bukhari, Faith, 4",
        },
    },
    {
        "id": 8,
        "tr": {
            "zat": "Hacı Bayram-ı Veli",
            "unvan": "Ankara Piri -kuddise sırruh-",
            "kategori": "Acziyet ve İrfan",
            "soz": "Nefsini bilen Rabbini bilir. Acziyetini idrak eden ilahi ikrama mazhar olur.",
            "soz_kaynagi": "Bayrami Menakıbı",
            "ayet": "Ey insanlar, siz Allah'a muhtaçsınız. Allah ise her bakımdan zengindir.",
            "ayet_kaynagi": "Fâtır Suresi, 15. Ayet",
            "hadis": "Kim Allah için alçakgönüllü olursa, Allah onu yüceltir.",
            "hadis_kaynagi": "Müslim, Birr, 69",
        },
        "en": {
            "zat": "Haji Bayram Veli",
            "unvan": "Master of Ankara -may his secret be sanctified-",
            "kategori": "Helplessness and Gnosis",
            "soz": "He who knows his ego knows his Lord. Whoever realizes his helplessness receives divine favor.",
            "soz_kaynagi": "Bayrami Hagiography",
            "ayet": "O mankind, you are those in need of Allah, while Allah is the Free of need, the Praiseworthy.",
            "ayet_kaynagi": "Surah Fatir, Verse 15",
            "hadis": "Whoever humbles himself for the sake of Allah, Allah will elevate him.",
            "hadis_kaynagi": "Muslim, Virtue, 69",
        },
    },
    {
        "id": 9,
        "tr": {
            "zat": "Akşemseddin",
            "unvan": "İstanbul'un Manevi Fatihi -kuddise sırruh-",
            "kategori": "Fetih ve İhlas",
            "soz": "Gönüller fethedilmeden topraklar kalıcı olarak kazanılmaz.",
            "soz_kaynagi": "Risaletü'n-Nûriyye",
            "ayet": "Allah size kesin bir zafer nasip edecektir.",
            "ayet_kaynagi": "Fetih Suresi, 3. Ayet",
            "hadis": "Ameller niyetlere göredir.",
            "hadis_kaynagi": "Buhari, Bed'ü'l-Vahy, 1",
        },
        "en": {
            "zat": "Aqshamsaddin",
            "unvan": "Spiritual Conqueror of Istanbul -may his secret be sanctified-",
            "kategori": "Conquest and Sincerity",
            "soz": "Lands cannot be permanently won unless hearts are conquered first.",
            "soz_kaynagi": "Risalat al-Nuriyyah",
            "ayet": "And that Allah may aid you with a mighty victory.",
            "ayet_kaynagi": "Surah Al-Fath, Verse 3",
            "hadis": "Actions are judged by intentions.",
            "hadis_kaynagi": "Bukhari, Revelation, 1",
        },
    },
    {
        "id": 10,
        "tr": {
            "zat": "Aziz Mahmud Hüdayi",
            "unvan": "Hüdayi Hazretleri -kuddise sırruh-",
            "kategori": "Dua ve Yakarış",
            "soz": "Ey Rabbimiz! Lütfunla kalplerimizi nurlandır, bizi rızandan ayırma.",
            "soz_kaynagi": "Hüdayi Divanı",
            "ayet": "Bana dua edin, duanıza icabet edeyim.",
            "ayet_kaynagi": "Mü'min Suresi, 60. Ayet",
            "hadis": "Dua ibadetin ta kendisidir.",
            "hadis_kaynagi": "Tirmizi, Deavât, 1",
        },
        "en": {
            "zat": "Aziz Mahmud Hudayi",
            "unvan": "Hazrat Hudayi -may his secret be sanctified-",
            "kategori": "Prayer and Supplication",
            "soz": "O Lord! Illuminate our hearts with Your grace, do not separate us from Your pleasure.",
            "soz_kaynagi": "Divan of Hudayi",
            "ayet": "Call upon Me; I will respond to you.",
            "ayet_kaynagi": "Surah Ghafir, Verse 60",
            "hadis": "Supplication is worship itself.",
            "hadis_kaynagi": "Tirmidhi, Supplications, 1",
        },
    },
    {
        "id": 11,
        "tr": {
            "zat": "İbrahim Hakkı Erzurumlu",
            "unvan": "Erzurumlu İbrahim Hakkı -kuddise sırruh-",
            "kategori": "Marifetname Hikmeti",
            "soz": "Mevla görelim neyler, neylerse güzel eyler.",
            "soz_kaynagi": "Marifetname",
            "ayet": "Olur ki bir şey sizin için hayırlıyken, siz onu hoş görmezsiniz.",
            "ayet_kaynagi": "Bakara Suresi, 216. Ayet",
            "hadis": "Müminin her işi hayırdır.",
            "hadis_kaynagi": "Müslim, Zühd, 64",
        },
        "en": {
            "zat": "Ibrahim Hakki Erzurumi",
            "unvan": "Ibrahim Hakki of Erzurum -may his secret be sanctified-",
            "kategori": "Wisdom of Marifetname",
            "soz": "Let us see what the Lord does; whatever He does, He does well.",
            "soz_kaynagi": "Marifetname",
            "ayet": "But perhaps you hate a thing and it is good for you.",
            "ayet_kaynagi": "Surah Al-Baqarah, Verse 216",
            "hadis": "Every affair of the believer is good.",
            "hadis_kaynagi": "Muslim, Asceticism, 64",
        },
    },
]

# ================================================================================
# 4. SOL KENAR ÇUBUĞU (SIDEBAR) VE FİLTRELEME
# ================================================================================
st.sidebar.markdown(f"### {t('sidebar_title')}")
st.sidebar.caption(t("info_note"))
st.sidebar.markdown("---")

with st.sidebar.expander(t("legal_warning_title")):
    st.sidebar.caption(t("legal_warning_body"))

st.sidebar.markdown(f"### 🔍 {t('select_person')}")

tum_zatlar = [t("all_option")] + sorted(
    list(
        set(
            [
                item["en"]["zat"] if lang == "EN" else item["tr"]["zat"]
                for item in DERIN_ILIM_ARSIVI
            ]
        )
    )
)

secilen_zat = st.sidebar.selectbox(t("select_person"), tum_zatlar)

st.sidebar.divider()
st.sidebar.markdown(f"### {t('daily_guide_title')}")
gunun_indeks = datetime.now().day % len(DERIN_ILIM_ARSIVI)
guncel_hikmet = (
    DERIN_ILIM_ARSIVI[gunun_indeks]["en"]
    if lang == "EN"
    else DERIN_ILIM_ARSIVI[gunun_indeks]["tr"]
)

st.sidebar.info(
    f"**{guncel_hikmet['zat']}**\n\n{t('daily_climate').format(guncel_hikmet['kategori'])}"
)

# ================================================================================
# 5. ANA EKRAN RENDER MANTIĞI
# ================================================================================
st.markdown(
    f"""
    <div style="padding: 10px 0;">
        <h1>{t('page_title')}</h1>
        <p>{t('page_subtitle')}</p>
    </div>
""",
    unsafe_allow_html=True,
)

arama_metni = st.text_input(
    t("search_label"), placeholder=t("search_placeholder")
)
temiz_arama = akilli_temizle(arama_metni)

filtrelenmis_liste = []
for veri in DERIN_ILIM_ARSIVI:
    dil_verisi = veri["en"] if lang == "EN" else veri["tr"]

    # Zat Seçimi Filtresi
    if secilen_zat != t("all_option") and dil_verisi["zat"] != secilen_zat:
        continue

    # Arama Metni Filtresi
    if temiz_arama:
        birlesik_metin = akilli_temizle(
            f"{dil_verisi['zat']} {dil_verisi['unvan']} {dil_verisi['kategori']} "
            f"{dil_verisi['soz']} {dil_verisi['soz_kaynagi']} {dil_verisi['ayet']} "
            f"{dil_verisi['ayet_kaynagi']} {dil_verisi['hadis']} {dil_verisi['hadis_kaynagi']}"
        )
        if temiz_arama in birlesik_metin:
            filtrelenmis_liste.append((veri["id"], dil_verisi))
    else:
        filtrelenmis_liste.append((veri["id"], dil_verisi))

if temiz_arama:
    if filtrelenmis_liste:
        st.info(t("results_found").format(len(filtrelenmis_liste)))
    else:
        st.warning(t("no_results"))

# ================================================================================
# 6. KARTLARIN EKRANA BASTIRILMASI
# ================================================================================
st.divider()

if not filtrelenmis_liste:
    st.warning(t("no_results"))
else:
    for item_id, content in filtrelenmis_liste:
        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown(
                f"""
                <div style="background-color: #f8fafc; padding: 20px; border-radius: 10px; border-left: 5px solid #0f172a; margin-bottom: 15px; min-height: 220px;">
                    <div style="color: #0f172a; font-weight: bold; font-size: 1.1rem;">
                        {content['zat']} <span style="font-size: 0.8rem; font-weight: normal; color: #64748b;">({content['unvan']})</span>
                    </div>
                    <small><b>{t('category_label')}:</b> {content['kategori']}</small>
                    <p style="font-size: 1.05rem; font-style: italic; color: #1e293b; margin-top: 10px;">"{content['soz']}"</p>
                    <hr style="margin: 10px 0; border: none; border-top: 1px solid #e2e8f0;">
                    <p style="font-size: 0.85rem; color: #64748b; margin: 0;"><b>{t('source_label')}:</b> {content['soz_kaynagi']}</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown(
                f"""
                <div style="background-color: #f0fdf4; padding: 15px; border-radius: 10px; border-left: 5px solid #166534; margin-bottom: 10px;">
                    <div style="color: #166534; font-weight: bold; font-size: 0.95rem;">{t('verse_title')}</div>
                    <p style="font-size: 0.95rem; color: #14532d; margin-top: 5px; margin-bottom: 5px;">"{content['ayet']}"</p>
                    <p style="font-size: 0.8rem; color: #166534; margin: 0;"><b>{t('source_label')}:</b> {content['ayet_kaynagi']}</p>
                </div>
                <div style="background-color: #fefce8; padding: 15px; border-radius: 10px; border-left: 5px solid #854d0e; margin-bottom: 15px;">
                    <div style="color: #854d0e; font-weight: bold; font-size: 0.95rem;">{t('hadith_title')}</div>
                    <p style="font-size: 0.95rem; color: #713f12; margin-top: 5px; margin-bottom: 5px;">"{content['hadis']}"</p>
                    <p style="font-size: 0.8rem; color: #854d0e; margin: 0;"><b>{t('source_label')}:</b> {content['hadis_kaynagi']}</p>
                </div>
            """,
                unsafe_allow_html=True,
            )