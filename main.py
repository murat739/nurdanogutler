import pandas as pd
import streamlit as st

# --- SAYFA YAPILANDIRMASI ---
st.set_page_config(
    page_title="Risale-i Nur Nasihat, Düstur ve Örnekler Rehberi",
    page_icon="📖",
    layout="wide",
)

# --- TÜM YAZILARIN TAM GÖRÜNMESİ İÇİN ÖZEL CSS STİLİ ---
st.markdown(
    """
    <style>
        /* Tablo benzeri kapsayıcı alanlar için tam metin görünürlüğü */
        .nasihat-card {
            background-color: #f9f9f9;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        }
        .nasihat-header {
            font-weight: bold;
            color: #1f77b4;
            font-size: 16px;
            margin-bottom: 8px;
        }
        .nasihat-text {
            font-size: 15px;
            color: #333333;
            margin-bottom: 5px;
        }
        .nasihat-footer {
            font-size: 13px;
            color: #666666;
            font-style: italic;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- YASAL UYARI VE TELİF HAKKI BİLDİRİMİ ---
st.warning(
    "⚠️ **Yasal Bilgilendirme ve Kullanım Şartları:**\n"
    "Bu yazılım ve içerdiği veritabanı tamamen akademik, araştırma ve manevi gelişim "
    "amacıyla hazırlanmıştır. **İçeriklerin kopyalanması, çoğaltılması veya ticari amaçlı "
    "kullanılması kesinlikle yasaktır.** Sunulan eser özetleri, nasihatler ve düsturlar "
    "rehberlik niteliğinde olup, hukuki veya resmi bir bağlayıcılığı bulunmamaktadır. "
    "Sadece kişisel manevi yönün gelişimi için bilgi amaçlıdır."
)

# --- 200 ADET KAPSAMLI VE EKSİKSİZ VERİ SETİ (1'DEN 200'E TAM LİSTE) ---
veriler = [
    {
        "ID": 1,
        "Konu": "İhlas",
        "Öğüt": "Amellerde yalnız ve yalnız Rıza-i İlahi esas alınmalı; insanların takdiri ve makam hırsı terk edilmelidir.",
        "Örnek ve Tatbikat": "Hizmet-i imaniyede 'halktan ecir istememek' düsturu gereğince, yapılan işlerin karşılığını sadece Allah'tan beklemek.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz - İhlas Risalesi (Üçüncü Düstur)",
    },
    {
        "ID": 2,
        "Konu": "İhlas",
        "Öğüt": "Amellere riya (gösteriş) karıştırmamak, en küçük bir şöhret arzusundan bile şiddetle sakınmak gerekir.",
        "Örnek ve Tatbikat": "Manevi makam sahibi olmayı veya nam kazanmayı arzu etmenin, ihlası zedeleyen zehirli bir bal hükmünde olması.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz - İhlas Risalesi (Birinci Düstur)",
    },
    {
        "ID": 3,
        "Konu": "İhlas",
        "Öğüt": "Kardeşlerin meziyetleriyle onur duymalı; onların şöhretini kendi makamın bilip kıskanmamalıdır.",
        "Örnek ve Tatbikat": "Bir medrese-i nuriye talebesinin, arkadaşının başarısını kendi başarısı gibi görerek ruhen sevinmesi.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz - İhlas Risalesi (İkinci Düstur)",
    },
    {
        "ID": 4,
        "Konu": "İhlas",
        "Öğüt": "Haklı davada hakiki ihlasa sahip üç kişi, ihlassız bin kişiye galip gelebilir.",
        "Örnek ve Tatbikat": "Kuvvetin çoklukta değil, kuvve-i maneviye ve ihlasta olduğunun idrakiyle sayı azlığına tasalanmamak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz - İhlas Risalesi (Dördüncü Düstur)",
    },
    {
        "ID": 5,
        "Konu": "Kardeşlik (Uhuvvet)",
        "Öğüt": "Mümin müminin kardeşidir; kardeşin kusurlarını affetmek, örtmek ve husumeti terk etmek esastır.",
        "Örnek ve Tatbikat": "Bir zühd veya hizmet arkadaşının hatasını gördüğünde onu hemen silmek yerine şefkatle ıslahına çalışmak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Lem'a - Uhuvvet Risalesi (Düstur-u Evvel)",
    },
    {
        "ID": 6,
        "Konu": "Kardeşlik (Uhuvvet)",
        "Öğüt": "İman, müminler arasında hakiki muhabbeti gerektirir; adavete ve düşmanlığa tevessül edilmemelidir.",
        "Örnek ve Tatbikat": "İman bağı vasıtasıyla, aradaki binlerce zati ayrılığa rağmen müminlerin birbirini sevmesi ve kucaklaması.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Lem'a - Uhuvvet Risalesi",
    },
    {
        "ID": 7,
        "Konu": "Müspet Hareket",
        "Öğüt": "Hak ve hakikat davası asla anarşi, kargaşa veya şiddetle değil; yalnızca müsbet hareket ve ahlakla yürütülür.",
        "Örnek ve Tatbikat": "Asayişi muhafaza etmek adına zulme uğranılsa bile sabredip sadece imana ve Kur'an'a hizmet etmek.",
        "Eser ve Detaylı Kaynak": "Mektubat (Yirmi İkinci Mektup) ve Emirdağ Lahikası",
    },
    {
        "ID": 8,
        "Konu": "Müspet Hareket",
        "Öğüt": "Mümin, içinde bulunduğu toplumun asayişini, huzurunu ve emniyetini korumakla mükelleftir.",
        "Örnek ve Tatbikat": "Kamu düzenini sarsacak hareketlerden kaçınarak, toplumun huzuruna menfi değil müspet katkı sunmak.",
        "Eser ve Detaylı Kaynak": "Emirdağ Lahikası (Asayiş ve Emniyet Düsturları)",
    },
    {
        "ID": 9,
        "Konu": "İbadet ve Namaz",
        "Öğüt": "Namaz, dinin direğidir; ubudiyetin en parlak ve kapsamlı unvanıdır.",
        "Örnek ve Tatbikat": "Günde beş vakit namazla, kainatın genel tesbihatına lisan-ı hal ve kal ile iştirak etmek.",
        "Eser ve Detaylı Kaynak": "Dördüncü Söz ve Dokuzuncu Söz",
    },
    {
        "ID": 10,
        "Konu": "İbadet ve Namaz",
        "Öğüt": "Namazları vaktinde kılmak, erken saatlerde eda etmek ruhun rahatlığı ve dünya işlerinin bereketi için şarttır.",
        "Örnek ve Tatbikat": "Sabah namazı ile güne başlayıp bütün günün rızık ve manevi sıkıntılarını erkenden halletmiş gibi ferah duymak.",
        "Eser ve Detaylı Kaynak": "Dokuzuncu Söz (Namazın Vakitlerinin Hikmetleri)",
    },
    {
        "ID": 11,
        "Konu": "Şükür",
        "Öğüt": "Verilen her nimete hem lisanen hem de hal ile şükredilmelidir; şükür nimeti artırır ve daimi kılar.",
        "Örnek ve Tatbikat": "Yenilen bir lokma ekmekten sonra 'Elhamdülillah' diyerek rızık verenin o nimetteki ikramını idrak etmek.",
        "Eser ve Detaylı Kaynak": "Yirmi Sekizinci Söz ve Otuz İkinci Söz",
    },
    {
        "ID": 12,
        "Konu": "Şükür",
        "Öğüt": "Dünyevi imkanlarda üstün olanlara bakıp sızlanmak yerine, alt hallerdeki hastalara ve fakirlere bakılarak şükredilmelidir.",
        "Örnek ve Tatbikat": "Maddi sıkıntıda iken bacağından sakat veya yatalak bir hastayı görünce kişinin kendi sağlığına hamdetmesi.",
        "Eser ve Detaylı Kaynak": "Lem'alar - Yirminci Lem'a (İhlas ve Şükür Hakikatleri)",
    },
    {
        "ID": 13,
        "Konu": "Sabır",
        "Öğüt": "Sabır üç kısımdır: Musibetlere karşı sabır, ibadette sebat ve günahlardan kaçınma sabrı.",
        "Örnek ve Tatbikat": "Günahların hırs ve cazibesi karşısında nefsi tutarak harama girmemek ve bu hususta sebat göstermek.",
        "Eser ve Detaylı Kaynak": "Mektubat - Yirmi Birinci Mektup (Sabır Risalesi)",
    },
    {
        "ID": 14,
        "Konu": "Sabır",
        "Öğüt": "Başa gelen musibetler karşısında fevri davranmamak, şikayetçi olmamak ve hal diliyle sabretmek gerekir.",
        "Örnek ve Tatbikat": "Hastalanan veya maddi kayba uğrayan birinin 'Ah, vah!' edip isyan etmek yerine tefekkürle sükuneti seçmesi.",
        "Eser ve Detaylı Kaynak": "Lem'alar - İkinci Lem'a (Sabır ve Şükür Nasihatleri)",
    },
    {
        "ID": 15,
        "Konu": "Ahlak (Yalan)",
        "Öğüt": "Yalan, imanın zıddı ve manevi bir zehirdir; maslahat kisvesi altında bile söylenmemelidir.",
        "Örnek ve Tatbikat": "Küçük bir menfaat veya korku sebebiyle gerçeği çarpıtarak hakikatle olan bağı koparmamak.",
        "Eser ve Detaylı Kaynak": "Mektubat - Yirminci Mektup (Yalanın Zararları)",
    },
    {
        "ID": 16,
        "Konu": "Ahlak (Gıybet)",
        "Öğüt": "Gıybet, manevi bir ceset yemek gibidir; din kardeşinin etini yemekten farksız bir felakettir.",
        "Örnek ve Tatbikat": "Mecliste bulunmayan birinin kusurlarını çekiştiren insanları uyararak o meclisten uzaklaşmak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Lem'a (Gıybetin Mahiyeti ve Zararları)",
    },
    {
        "ID": 17,
        "Konu": "İktisat",
        "Öğüt": "İktisat (tutumlu olmak), rızkın bereketini artırır ve insanı dilencilik zilletinden korur.",
        "Örnek ve Tatbikat": "Evdeki gıda ve eşyaları israf etmeden, tam kararında ve kanaatkar bir biçimde kullanmak.",
        "Eser ve Detaylı Kaynak": "Ondokuzuncu Lem'a - İktisat Risalesi",
    },
    {
        "ID": 18,
        "Konu": "İktisat",
        "Öğüt": "İsraf hem maddi hem manevi bereketsizliğe yol açar; su ve ekmek gibi nimetler zayi edilmemelidir.",
        "Örnek ve Tatbikat": "Yemek tabağında bırakılan artıkları çöpe atmak yerine tasarruf edip değerlendirmek.",
        "Eser ve Detaylı Kaynak": "Ondokuzuncu Lem'a - İktisat Risalesi (Ekmek ve Su Örnekleri)",
    },
    {
        "ID": 19,
        "Konu": "Kanaat ve Hırs",
        "Öğüt": "Hırs, mahrumiyete ve sefalete sebeptir; çalışmak başkadır, hırsla dünyaya tapmak başkadır.",
        "Örnek ve Tatbikat": "Daha çok kazanmak için meşru dairenin dışına çıkıp hırsla her şeyi elde etmeye çalışmamak.",
        "Eser ve Detaylı Kaynak": "Ondokuzuncu Lem'a (Hırsın Mahiyeti)",
    },
    {
        "ID": 20,
        "Konu": "Kanaat ve Hırs",
        "Öğüt": "Kanaat eden aziz olur, tükenmez bir hazineye kavuşur; hırslı olan ise daima muhtaç ve zelil kalır.",
        "Örnek ve Tatbikat": "Eldeki az rızka şükredip başkalarının servetine göz dikmeyerek ruh huzuru içinde yaşamak.",
        "Eser ve Detaylı Kaynak": "Ondokuzuncu Lem'a (Kanaat Düsturları)",
    },
    {
        "ID": 21,
        "Konu": "Nefis Terbiyesi",
        "Öğüt": "Nefis daima fenalığı emreder; nefse karşı dalkavukluk yapılmamalı, muhasebe edilmelidir.",
        "Örnek ve Tatbikat": "Nefsin kusurlarını görerek onu temize çıkarmamak ve hatalarla yüzleşmek.",
        "Eser ve Detaylı Kaynak": "Yirmi Dokuzuncu Mektup / Mesnevi-i Nuriye",
    },
    {
        "ID": 22,
        "Konu": "Nefis ve Benlik",
        "Öğüt": "Enaniyet ve gurur, manevi terakkinin en büyük engellerindendir; benlik terk edilmelidir.",
        "Örnek ve Tatbikat": "Başarıları şahsına mal etmek yerine, onları inayet-i ilahiye olarak telakki etmek.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz / Otuzuncu Söz",
    },
    {
        "ID": 23,
        "Konu": "Tevazu",
        "Öğüt": "İnsan ne kadar büyük makam veya ilme sahip olursa olsun, tevazudan ayrılmamalıdır.",
        "Örnek ve Tatbikat": "Büyük bir kariyere sahipken sıradan insanlarla mütevazı bir şekilde iletişim kurmak.",
        "Eser ve Detaylı Kaynak": "Mektubat Külliyatı",
    },
    {
        "ID": 24,
        "Konu": "Ahlak (Haset)",
        "Öğüt": "Haset, haset edeni yer bitirir; başkasının nimetine rıza göstermek esastır.",
        "Örnek ve Tatbikat": "Komşunun veya mesai arkadaşının elde ettiği başarıya kalben sevinmek.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Lem'a (Haset Bahsi)",
    },
    {
        "ID": 25,
        "Konu": "Ahlak (Kibir)",
        "Öğüt": "Kibir, azamet sıfatına müdahale demektir; kibirlenen insan manen alçalır.",
        "Örnek ve Tatbikat": "Kendini diğer insanlardan üstün görme hissiyatını kalpten defetmek.",
        "Eser ve Detaylı Kaynak": "Küçük Sözler / Mesnevi-i Nuriye",
    },
    {
        "ID": 26,
        "Konu": "Af ve Hoşgörü",
        "Öğüt": "İnsanların kusurlarını bağışlamak, kin ve intikam duygularını atmak en büyük erdemdir.",
        "Örnek ve Tatbikat": "Kendisine haksızlık eden bir kimsenin hatasını affederek büyüklük göstermek.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 27,
        "Konu": "Adalet ve Zulüm",
        "Öğüt": "Kimseye zerre miktar haksızlık yapılmamalıdır; zalimlere taraftar olmak da zulümdür.",
        "Örnek ve Tatbikat": "Haklıyı savunmak, haksız kim akraba olursa olsun hakikatin yanında durmak.",
        "Eser ve Detaylı Kaynak": "Divan-ı Harb-i Örfî / İşaratü'l-İ'caz",
    },
    {
        "ID": 28,
        "Konu": "Emanet",
        "Öğüt": "Üzerinizde bulunan maddi veya manevi her türlü emanete (görev, sır, mal) riayet edilmelidir.",
        "Örnek ve Tatbikat": "Bir arkadaşın sırrını veya emanet ettiği eşyayı en güvenli şekilde korumak.",
        "Eser ve Detaylı Kaynak": "Otuz İkinci Söz",
    },
    {
        "ID": 29,
        "Konu": "Ahde Vefa",
        "Öğüt": "Verilen sözler tutulmalı, ahitlere ve antlaşmalara sadık kalınmalıdır.",
        "Örnek ve Tatbikat": "Zor duruma düşülse dahi verilen sözün gereğini yerine getirmek.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 30,
        "Konu": "Dil ve Kelam",
        "Öğüt": "Dil yalan ve dedikodudan arındırılmalı; sadece hak ve faydalı kelamlar sarf edilmelidir.",
        "Örnek ve Tatbikat": "Konuşmadan önce kelimelerin hayırlı olup olmadığını tartmak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz / Lem'alar",
    },
    {
        "ID": 31,
        "Konu": "İlim",
        "Öğüt": "İlim, Allah rızası ve insanlığa hizmet için öğrenilmeli; kibir vesilesi yapılmamalıdır.",
        "Örnek ve Tatbikat": "Öğrenilen bilgileri başkalarına menfaatsiz bir şekilde aktarmak.",
        "Eser ve Detaylı Kaynak": "İşaratü'l-İ'caz / Mektubat",
    },
    {
        "ID": 32,
        "Konu": "İlim ve Amel",
        "Öğüt": "Bilinen ilimle amel edilmeli, ilim ile amel arasındaki bağ koparılmamalıdır.",
        "Örnek ve Tatbikat": "Doğru olduğu bilinen bir dini veya ahlaki kuralı bizzat yaşantısında tatbik etmek.",
        "Eser ve Detaylı Kaynak": "Mesnevi-i Nuriye",
    },
    {
        "ID": 33,
        "Konu": "Tefekkür",
        "Öğüt": "Kainattaki eserlere ibret nazarıyla bakıp Cenab-ı Hakk’ın sanatını tefekkür etmek gerekir.",
        "Örnek ve Tatbikat": "Doğada bir çiçeğin yaratılışındaki inceliği inceleyerek Allah'ın kudretini düşünmek.",
        "Eser ve Detaylı Kaynak": "Otuz Üçüncü Söz (Pencereler Risalesi)",
    },
    {
        "ID": 34,
        "Konu": "Ölüm ve Ahiret",
        "Öğüt": "Ölüm bir yok oluş değil, ebedi bir aleme açılan kapıdır.",
        "Örnek ve Tatbikat": "Kabir ziyaretlerinde ölümün hakikatini hatırlayıp ahirete hazırlanmak.",
        "Eser ve Detaylı Kaynak": "Yirminci Söz / Yirmi Dördüncü Söz",
    },
    {
        "ID": 35,
        "Konu": "Ölüm ve Ahiret",
        "Öğüt": "Dünya hayatı geçici bir misafirhane, ahiret ise esas vatan ve mahsul yeridir.",
        "Örnek ve Tatbikat": "Dünya malına kalben bağlanmayıp geçici bir misafir gibi hareket etmek.",
        "Eser ve Detaylı Kaynak": "Otuz İkinci Söz",
    },
    {
        "ID": 36,
        "Konu": "Gençlik",
        "Öğüt": "Gençlik ömrü kıymetlidir; heva ve heves uğruna israf edilmeyip ibadetle değerlendirilmelidir.",
        "Örnek ve Tatbikat": "Gençlik enerjisini topluma ve imani hizmetlere kanalize etmek.",
        "Eser ve Detaylı Kaynak": "Gençlik Rehberi (Şualar)",
    },
    {
        "ID": 37,
        "Konu": "İhtiyarlık",
        "Öğüt": "İhtiyarlara hürmet edilmeli, onların tecrübelerine ve haklarına riayet olunmalıdır.",
        "Örnek ve Tatbikat": "Yaşlı bir kimseye toplu taşımada yer vermek veya işinde yardımcı olmak.",
        "Eser ve Detaylı Kaynak": "Lem'alar (Yirmi Altıncı Lem'a - İhtiyarlar Risalesi)",
    },
    {
        "ID": 38,
        "Konu": "Aile ve Ebeveyn",
        "Öğüt": "Anne ve babaya 'Öf' bile denilmemeli; onlara karşı son derece şefkatli ve saygılı olunmalıdır.",
        "Örnek ve Tatbikat": "Yaşlı ebeveynin her türlü ihtiyacını güler yüzle karşılamak.",
        "Eser ve Detaylı Kaynak": "Mektubat (Dokuzuncu Mektup)",
    },
    {
        "ID": 39,
        "Konu": "Akrabalık",
        "Öğüt": "Akrabalarla bağlar koparılmamalı, sevinçte ve kederde yardımlaşılmalıdır.",
        "Örnek ve Tatbikat": "Uzakta olan akrabaları arayıp hal ve hatırlarını sormak.",
        "Eser ve Detaylı Kaynak": "Mektubat Külliyatı",
    },
    {
        "ID": 40,
        "Konu": "Komşuluk",
        "Öğüt": "Komşulara maddi ve manevi zarar verilmemeli, komşunun hakkı gözetilmelidir.",
        "Örnek ve Tatbikat": "Evde yapılan yemekten komşuya ikram etmek veya gürültü yapmamak.",
        "Eser ve Detaylı Kaynak": "Lem'alar Külliyatı",
    },
    {
        "ID": 41,
        "Konu": "Sosyal Adalet",
        "Öğüt": "Yetimlerin başı okşanmalı, hakları korunmalı ve kimsesizlere el uzatılmalıdır.",
        "Örnek ve Tatbikat": "Kimsesiz çocukların eğitimine ve iaşesine katkı sunmak.",
        "Eser ve Detaylı Kaynak": "İşaratü'l-İ'caz",
    },
    {
        "ID": 42,
        "Konu": "Zekat ve Sadaka",
        "Öğüt": "Malın zekatını eksiksiz vermek ve sadaka ile muhtaçların yüzünü güldürmek rızkı bereketlendirir.",
        "Örnek ve Tatbikat": "İhtiyaç sahiplerine gizli sadakalar vererek toplumsal dengenin korunması.",
        "Eser ve Detaylı Kaynak": "Mektubat / Sözler",
    },
    {
        "ID": 43,
        "Konu": "Borç ve Ticaret",
        "Öğüt": "Gereksiz borç altına girilmemeli, borç zamanında ödenerek alacaklılar mağdur edilmemelidir.",
        "Örnek ve Tatbikat": "Ödeme gününe riayet ederek borcu aksatmadan kapatmak.",
        "Eser ve Detaylı Kaynak": "Ondokuzuncu Lem'a",
    },
    {
        "ID": 44,
        "Konu": "Ticaret Ahlakı",
        "Öğüt": "Alışverişte hile yapılmamalı, tartı ve ölçüde adaletli olunmalıdır.",
        "Örnek ve Tatbikat": "Müşteriye malın kusurunu gizlemeden dürüstçe satmak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 45,
        "Konu": "Faiz",
        "Öğüt": "Faiz haramdır ve toplumun adalet dengesini bozar; faizli işlemlerden uzak durulmalıdır.",
        "Örnek ve Tatbikat": "Finansal planlamada faizsiz alternatifleri tercih etmek.",
        "Eser ve Detaylı Kaynak": "Lem'alar / Sözler",
    },
    {
        "ID": 46,
        "Konu": "Rızık",
        "Öğüt": "'Rızkı veren Allah’tır' inancıyla hareket edilmeli, meşru dairedeki rızık herkese yeter.",
        "Örnek ve Tatbikat": "Helal kazanca kanaat edip haram yollardan rızık aramamak.",
        "Eser ve Detaylı Kaynak": "Otuz İkinci Söz / Yirmi Dördüncü Söz",
    },
    {
        "ID": 47,
        "Konu": "Çalışmak ve Gayret",
        "Öğüt": "'İnsana ancak çalıştığının karşılığı vardır' sırrınca meşru dairede azami gayret sarf edilmelidir.",
        "Örnek ve Tatbikat": "İş hayatında veya ilmi çalışmalarda tembellik etmeden çalışmak.",
        "Eser ve Detaylı Kaynak": "Yirmi Dördüncü Söz",
    },
    {
        "ID": 48,
        "Konu": "Tembellik",
        "Öğüt": "Tembellik, hem dünya hem ahiret sefaletine kapı açar; daima faal olunmalıdır.",
        "Örnek ve Tatbikat": "Boş oturmak yerine faydalı işlerle meşgul olmak.",
        "Eser ve Detaylı Kaynak": "Mesnevi-i Nuriye",
    },
    {
        "ID": 49,
        "Konu": "Zaman",
        "Öğüt": "Zaman, hayatın hammaddesidir; boşa harcanan saatlerden hesap sorulacağı unutulmamalıdır.",
        "Örnek ve Tatbikat": "Günlük plan yaparak vakti hem ibadet hem de ilimle değerlendirmek.",
        "Eser ve Detaylı Kaynak": "Birinci Söz / Asâ-yı Musa",
    },
    {
        "ID": 50,
        "Konu": "İstişare",
        "Öğüt": "Önemli işlerde ehl-i meşveret ile istişare edilmeli, tek başına buyruk hareket edilmemelidir.",
        "Örnek ve Tatbikat": "Ailevi veya kurumsal kararları ortak akılla almak.",
        "Eser ve Detaylı Kaynak": "Mektubat / Lem'alar",
    },
    {
        "ID": 51,
        "Konu": "Meşveret",
        "Öğüt": "İstişarelerde herkes fikrini söylemeli, karar verildikten sonra o karara tam uyulmalıdır.",
        "Örnek ve Tatbikat": "Çoğunluğun aldığı karara sadık kalıp muhalefeti sürdürmemek.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 52,
        "Konu": "Hata ve Tevbe",
        "Öğüt": "Hata yapıldığında inat edilmemeli, hemen hatadan dönülüp hakka teslim olunmalıdır.",
        "Örnek ve Tatbikat": "Hatalı olunduğu anlaşıldığında özür dileyip doğrusunu benimsemek.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 53,
        "Konu": "İstikamet",
        "Öğüt": "İman ve amelde istikamet üzere sebat edilmeli, aşırılıklardan kaçınılmalıdır.",
        "Örnek ve Tatbikat": "İbadetlerde ve ahlaki duruşta dengeli ve kararlı olmak.",
        "Eser ve Detaylı Kaynak": "Birinci Lem'a / Mektubat",
    },
    {
        "ID": 54,
        "Konu": "Hüsn-ü Zan",
        "Öğüt": "Müslümanlar hakkında su-i zan yerine hüsn-ü zan (iyi zannetmek) esastır.",
        "Örnek ve Tatbikat": "Birinin davranışını kötüye yormak yerine makul bir mazeret aramak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Lem'a",
    },
    {
        "ID": 55,
        "Konu": "Dostluk ve Vefa",
        "Öğüt": "Hakiki dost, hata karşısında terk eden değil, düzeltmeye çalışan vefakardır.",
        "Örnek ve Tatbikat": "Zor gününde arkadaşının yanında olup ona destek olmak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 56,
        "Konu": "Kötülüğe İyilik",
        "Öğüt": "Kötülüğe kötülükle karşılık vermek yerine, iyilikle mukabele edilmelidir.",
        "Örnek ve Tatbikat": "Size kaba davranan birine tebessüm ve tatlı dille karşılık vermek.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 57,
        "Konu": "Sebat",
        "Öğüt": "Zorluklar karşısında pes etmemeli, iman hizmetinde sabit-kadem olunmalıdır.",
        "Örnek ve Tatbikat": "Engeller karşısında azmi kaybetmeyip yola devam etmek.",
        "Eser ve Detaylı Kaynak": "Barla Lahikası / Kastamonu Lahikası",
    },
    {
        "ID": 58,
        "Konu": "Şefkat",
        "Öğüt": "Bütün canlılara, özellikle çocuklara ve zayıflara karşı merhametli olunmalıdır.",
        "Örnek ve Tatbikat": "Sokaktaki kimsesizlere ve yardıma muhtaçlara kol kanat germek.",
        "Eser ve Detaylı Kaynak": "Şualar / Mektubat",
    },
    {
        "ID": 59,
        "Konu": "Çevre ve Hayvanlar",
        "Öğüt": "Hayvanlara eziyet edilmemelidir; onların da merhamet görmeye hakkı vardır.",
        "Örnek ve Tatbikat": "Kış günlerinde sokak hayvanları için kap önüne su ve mama koymak.",
        "Eser ve Detaylı Kaynak": "Yirmi Dördüncü Söz",
    },
    {
        "ID": 60,
        "Konu": "Tevekkül",
        "Öğüt": "Tedbir alındıktan sonra işin sonu Allah’a bırakılmalı; neticeye razı olunmalıdır.",
        "Örnek ve Tatbikat": "Sınava veya işe hazırlanıp elimizden geleni yaptıktan sonra sonucu Allah'a havale etmek.",
        "Eser ve Detaylı Kaynak": "Yirmi Üçüncü Söz / Otuz Üçüncü Mektup",
    },
    {
        "ID": 61,
        "Konu": "Kader",
        "Öğüt": "Başa gelen mukadder olaylara imanla yaklaşılmalı, isyan edilmemelidir.",
        "Örnek ve Tatbikat": "Beklenmedik bir kayıp karşısında metaneti korumak.",
        "Eser ve Detaylı Kaynak": "Otuz İkinci Söz / Yirmi Altıncı Söz",
    },
    {
        "ID": 62,
        "Konu": "Dua",
        "Öğüt": "Dua ibadettir; kulun Rabbine en yakın olduğu andır, dualarda ısrarcı olunmalıdır.",
        "Örnek ve Tatbikat": "Gecenin sessizliğinde samimi bir kalple Allah'a el açıp niyaz etmek.",
        "Eser ve Detaylı Kaynak": "Yirmi Üçüncü Söz",
    },
    {
        "ID": 63,
        "Konu": "Tövbe",
        "Öğüt": "Günah işlendiğinde derhal tövbe edilmeli, kalbin pası istiğfarla temizlenmelidir.",
        "Örnek ve Tatbikat": "Yapılan bir hatadan hemen sonra pişmanlık duyup af dilemek.",
        "Eser ve Detaylı Kaynak": "Yirmi Dokuzuncu Lem'a",
    },
    {
        "ID": 64,
        "Konu": "Nefis Muhasebesi",
        "Öğüt": "Her gün akşam yatmadan önce o gün yapılanların muhasebesi yapılmalıdır.",
        "Örnek ve Tatbikat": "Günün dökümünü çıkararak nerede yanlış yapıldığını düşünmek.",
        "Eser ve Detaylı Kaynak": "Sözler",
    },
    {
        "ID": 65,
        "Konu": "Arkadaş Seçimi",
        "Öğüt": "İnsanı zararlı alışkanlıklara sürükleyen kötü arkadaşlardan uzak durulmalıdır.",
        "Örnek ve Tatbikat": "Çevredeki arkadaşları ahlaki yönden süzgeçten geçirmek.",
        "Eser ve Detaylı Kaynak": "Dokuzuncu Söz / Gençlik Rehberi",
    },
    {
        "ID": 66,
        "Konu": "İlim ve Mütalaa",
        "Öğüt": "Risale-i Nur ve Kur'an hakikatleri daimî bir şekilde mütalaa edilmelidir.",
        "Örnek ve Tatbikat": "Düzenli olarak günlük kitap okuma seansları düzenlemek.",
        "Eser ve Detaylı Kaynak": "Kastamonu Lahikası",
    },
    {
        "ID": 67,
        "Konu": "Hizmet",
        "Öğüt": "İman hizmetinde maddi ve manevi fedakarlıktan kaçınmamak gerekir.",
        "Örnek ve Tatbikat": "Hizmet için zamandan ve imkanlardan gönüllü feragat etmek.",
        "Eser ve Detaylı Kaynak": "Barla Lahikası",
    },
    {
        "ID": 68,
        "Konu": "Menfaat",
        "Öğüt": "Allah rızası için yapılan hizmetlerde hiçbir menfaat veya makam beklenmemelidir.",
        "Örnek ve Tatbikat": "Karşılıksız iyilik yapıp bunu kimseye bildirmemek.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz (İhlas Risalesi)",
    },
    {
        "ID": 69,
        "Konu": "Cemaat",
        "Öğüt": "Cemaat olmanın rahmeti unutulmamalı; şahsi iddialar cemaatin maslahatına feda edilmelidir.",
        "Örnek ve Tatbikat": "Ortak fayda için bireysel istekleri geri plana itmek.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz / Mektubat",
    },
    {
        "ID": 70,
        "Konu": "Siyaset",
        "Öğüt": "Hakiki iman hizmeti, günlük siyasi çekişmelerin ve tarafgirliklerin üstünde tutulmalıdır.",
        "Örnek ve Tatbikat": "Maneviyatı siyasete alet etmeden tarafsız kalabilmek.",
        "Eser ve Detaylı Kaynak": "Divan-ı Harb-i Örfî / Emirdağ Lahikası",
    },
    {
        "ID": 71,
        "Konu": "Vatan ve Asayiş",
        "Öğüt": "Vatanın asayişi ve huzuru her şeyin üstünde tutulmalı, asayişi bozacak şeylerden kaçınılmalıdır.",
        "Örnek ve Tatbikat": "Toplumsal barışı zedeleyecek provokasyonlara karşı uyanık olmak.",
        "Eser ve Detaylı Kaynak": "Emirdağ Lahikası / Şualar",
    },
    {
        "ID": 72,
        "Konu": "Kalp Kırmak",
        "Öğüt": "Kabe binasından daha mukaddes olan insan kalbi kırılmamalı, kimsenin ahı alınmamalıdır.",
        "Örnek ve Tatbikat": "Konuşurken kılı kırk yararak kimsenin kalbini incitmemek.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 73,
        "Konu": "İletişim",
        "Öğüt": "İnsanlarla iletişimde tatlı dil, güler yüz ve latifeli yaklaşım esas alınmalıdır.",
        "Örnek ve Tatbikat": "İnsanları tebessümle ve samimi bir üslupla karşılamak.",
        "Eser ve Detaylı Kaynak": "Mektubat / Lem'alar",
    },
    {
        "ID": 74,
        "Konu": "Öfke",
        "Öğüt": "Öfkeliyken karar verilmemeli, öfke anında susulmalı veya abdest alınmalıdır.",
        "Örnek ve Tatbikat": "Sinirli anlarda ortamı terk edip sakinleşmeyi beklemek.",
        "Eser ve Detaylı Kaynak": "Mesnevi-i Nuriye",
    },
    {
        "ID": 75,
        "Konu": "Temizlik",
        "Öğüt": "Maddi ve manevi temizliğe azami dikkat edilmeli; beden ve mekan temiz tutulmalıdır.",
        "Örnek ve Tatbikat": "Ev ve çalışma alanlarını daima derli toplu tutmak.",
        "Eser ve Detaylı Kaynak": "Mektubat / Lem'alar",
    },
    {
        "ID": 76,
        "Konu": "Sağlık",
        "Öğüt": "Beden Allah’ın emanetidir; sağlığı korumak ve zararlı alışkanlıklardan kaçınmak önemlidir.",
        "Örnek ve Tatbikat": "Sağlıklı beslenip zararlı maddelerden uzak durmak.",
        "Eser ve Detaylı Kaynak": "Asâ-yı Musa / Lem'alar",
    },
    {
        "ID": 77,
        "Konu": "Sünnet",
        "Öğüt": "Hayatın her alanında Hazret-i Muhammed'in (ASV) sünnet-i seniyesine riayet edilmelidir.",
        "Örnek ve Tatbikat": "Yemeğe başlarken besmele çekmek gibi küçük sünnetleri uygulamak.",
        "Eser ve Detaylı Kaynak": "On Birinci Lem'a (Sünnet-i Seniye Risalesi)",
    },
    {
        "ID": 78,
        "Konu": "Bid'at",
        "Öğüt": "Dinde sonradan uydurulan bid'atlardan sakınılmalı, sünnet çizgisinden sapılmamalıdır.",
        "Örnek ve Tatbikat": "Dini konularda hurafelere itibar etmeyip sünnete sarılmak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 79,
        "Konu": "Kur'an",
        "Öğüt": "Kur’an-ı Kerim her gün düzenli okunmalı, manası anlaşılmaya çalışılmalıdır.",
        "Örnek ve Tatbikat": "Her gün belirli bir sayfa meal ve tefsir okuması yapmak.",
        "Eser ve Detaylı Kaynak": "Yirmi Beşinci Söz (İcazü'l-Kur'an)",
    },
    {
        "ID": 80,
        "Konu": "Salavat",
        "Öğüt": "Peygamberimize bol bol salavat getirilmeli, sünnetine tam ittiba edilmelidir.",
        "Örnek ve Tatbikat": "Boş anlarda zihnen salavat-ı şerife getirmek.",
        "Eser ve Detaylı Kaynak": "Dokuzuncu Mektup / Lem'alar",
    },
    {
        "ID": 81,
        "Konu": "İbadet Devamlılığı",
        "Öğüt": "Az da olsa sürekli yapılan ibadet, kesintili olandan daha hayırlıdır.",
        "Örnek ve Tatbikat": "Her gün az miktarda da olsa düzenli nafile ibadet yapmak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 82,
        "Konu": "Nefse Güvenmeme",
        "Öğüt": "Nefse asla itimat edilmemeli, son nefese kadar dikkatli olunmalıdır.",
        "Örnek ve Tatbikat": "'Ben günah işlemem' demeyip her an haktan nefis için koruma istemek.",
        "Eser ve Detaylı Kaynak": "Mesnevi-i Nuriye",
    },
    {
        "ID": 83,
        "Konu": "İhsan Şuuru",
        "Öğüt": "Her an Allah’ın huzurunda olduğu bilinciyle (ihsan şuuruyla) yaşanmalıdır.",
        "Örnek ve Tatbikat": "Kimse görmese bile Allah'ın gördüğünü bilerek dürüst davranmak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz",
    },
    {
        "ID": 84,
        "Konu": "Mümin Kardeşliği",
        "Öğüt": "Sadece kendi nefsini düşünmek yerine kardeşlerinin selameti için dua edilmelidir.",
        "Örnek ve Tatbikat": "Gıyaben diğer mümin kardeşlerin sıkıntıları için dua etmek.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 85,
        "Konu": "İlme Hürmet",
        "Öğüt": "Kitaplar yüksek yerlere konulmalı, ilme ve kitaba hürmet gösterilmelidir.",
        "Örnek ve Tatbikat": "İlim kitaplarını asla yere yakın veya ayak ucu tarafa koymamak.",
        "Eser ve Detaylı Kaynak": "Barla Lahikası",
    },
    {
        "ID": 86,
        "Konu": "Güne Başlangıç",
        "Öğüt": "Güne başlarken besmele, dua ve hıfz-ı ilahi talebiyle adım atılmalıdır.",
        "Örnek ve Tatbikat": "Evden çıkarken 'Bismillahi tevekkeltü alallah' diyerek yola çıkmak.",
        "Eser ve Detaylı Kaynak": "Şualar",
    },
    {
        "ID": 87,
        "Konu": "Ahiret Hedefi",
        "Öğüt": "Hayattaki en büyük hedef imanla kabre girmek ve rıza-i ilahiyi kazanmaktır.",
        "Örnek ve Tatbikat": "Tüm amelleri ebedi hayatı kazanma endişesiyle şekillendirmek.",
        "Eser ve Detaylı Kaynak": "Otuz İkinci Söz",
    },
    {
        "ID": 88,
        "Konu": "Kardeş Hakları",
        "Öğüt": "Kardeşlik hukuku gözetilmeli; gıyabında dua edilerek destek olunmalıdır.",
        "Örnek ve Tatbikat": "Bir dostun arkasından gıybetini edenleri susturup onu savunmak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Lem'a",
    },
    {
        "ID": 89,
        "Konu": "Hakikati Kabul",
        "Öğüt": "Hakikat nerede ve kimmisinden gelirse gelsin kollar açılarak kabul edilmelidir.",
        "Örnek ve Tatbikat": "Doğru bir fikri küçük yaştaki birinden bile duyduğunda tasdik etmek.",
        "Eser ve Detaylı Kaynak": "Muhakemat",
    },
    {
        "ID": 90,
        "Konu": "Niyetin Safiyeti",
        "Öğüt": "En küçük hayırlı işte bile niyet halis ve sadece Allah rızası olmalıdır.",
        "Örnek ve Tatbikat": "Sadaka verirken övgü beklememek.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz",
    },
    {
        "ID": 91,
        "Konu": "Hizmet Düsturu",
        "Öğüt": "Hizmet-i imaniyede rekabet değil, tesanüt ve takviye esastır.",
        "Örnek ve Tatbikat": "Diğer hizmet gruplarıyla yarışmak yerine birbirinin eksiğini kapatmak.",
        "Eser ve Detaylı Kaynak": "Barla Lahikası",
    },
    {
        "ID": 92,
        "Konu": "Hizmet Edebi",
        "Öğüt": "Ehl-i imanın inkişafına mani olacak tavırlardan kesinlikle kaçınılmalıdır.",
        "Örnek ve Tatbikat": "Topluluk içinde kırıcı tartışmalara girmemek.",
        "Eser ve Detaylı Kaynak": "Kastamonu Lahikası",
    },
    {
        "ID": 93,
        "Konu": "Kusur Örtme",
        "Öğüt": "Müminlerin kusurlarını değil, güzel yönlerini ön plana çıkarmak gerekir.",
        "Örnek ve Tatbikat": "Bir arkadaşın hatalarını yüzüne vurmak yerine güzelliklerini takdir etmek.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Lem'a",
    },
    {
        "ID": 94,
        "Konu": "Müspet Davranış",
        "Öğüt": "Zarar vermek başkadır, menfi hareket etmek başkadır; müspet hareket esastır.",
        "Örnek ve Tatbikat": "Haksızlığa uğranılsa dahi şiddete başvurmadan hukuki ve meşru yolla hakkı aramak.",
        "Eser ve Detaylı Kaynak": "Emirdağ Lahikası",
    },
    {
        "ID": 95,
        "Konu": "Asayişi Koruma",
        "Öğüt": "Asayişi ihlal edecek fitnelerden uzak durmak her mümin görevidir.",
        "Örnek ve Tatbikat": "Toplumsal olaylarda sükuneti koruyup yapıcı olmak.",
        "Eser ve Detaylı Kaynak": "Şualar",
    },
    {
        "ID": 96,
        "Konu": "Tesbihat",
        "Öğüt": "Namazın hulasası olan tesbihatlar sünnete uygun şekilde tamamlanmalıdır.",
        "Örnek ve Tatbikat": "Namaz sonrasında yapılan tesbihat ve duaları aksatmamak.",
        "Eser ve Detaylı Kaynak": "Lem'alar",
    },
    {
        "ID": 97,
        "Konu": "Şükür Dengesi",
        "Öğüt": "Maddi nimetlerde aşağıdakilere, manevi nimetlerde yukarıdakilere bakılmalıdır.",
        "Örnek ve Tatbikat": "Maddi darlıkta daha fakirlere, maneviyatta ise evliyalara bakarak şükretmek.",
        "Eser ve Detaylı Kaynak": "Yirminci Lem'a",
    },
    {
        "ID": 98,
        "Konu": "Hakiki Sabır",
        "Öğüt": "Musibet anında ilk anda gösterilen metanet hakiki sabırdır.",
        "Örnek ve Tatbikat": "Kötü haberi alır almaz fevri tepki vermeyip 'Inna lillahi' demek.",
        "Eser ve Detaylı Kaynak": "İkinci Lem'a",
    },
    {
        "ID": 99,
        "Konu": "Doğruluk",
        "Öğüt": "Hakikatin hürmetine yalan söylenmemeli, doğru her zaman üstün tutulmalıdır.",
        "Örnek ve Tatbikat": "Zor durumda kalınsa bile doğrudan sapmamak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 100,
        "Konu": "Gıybetten Kaçınma",
        "Öğüt": "Gıybetin yapıldığı meclislerden hemen uzaklaşılmalı veya men edilmelidir.",
        "Örnek ve Tatbikat": "Dedikodu yapılan bir ortama girildiğinde konuyu değiştirmek veya oradan ayrılmak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Lem'a",
    },
    {
        "ID": 101,
        "Konu": "Emanete Sadakat",
        "Öğüt": "Maddi ya da manevi hiçbir emanete hıyanet edilmemelidir.",
        "Örnek ve Tatbikat": "Verilen bir görevi en mükemmel şekilde zamanında bitirmek.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 102,
        "Konu": "Hizmet Şevki",
        "Öğüt": "Manevi hizmetlerde şevk kırıklığına uğramadan daima aktif olunmalıdır.",
        "Örnek ve Tatbikat": "Yorulsa bile hayırlı işlerde koşturmaya devam etmek.",
        "Eser ve Detaylı Kaynak": "Barla Lahikası",
    },
    {
        "ID": 103,
        "Konu": "Kötü Alışkanlıklar",
        "Öğüt": "İnsanı manen uyuşturan ve iradeyi zayıflatan her türlü kötü alışkanlıktan kaçınılmalıdır.",
        "Örnek ve Tatbikat": "Zararlı maddelerden ve bağımlılıklardan iradeyle uzak durmak.",
        "Eser ve Detaylı Kaynak": "Gençlik Rehberi",
    },
    {
        "ID": 104,
        "Konu": "İhlasın Muhafazası",
        "Öğüt": "İhlası kıracak riya ve ucub gibi kalbi hastalıklardan daima sakınılmalıdır.",
        "Örnek ve Tatbikat": "Yapılan ibadetleri başkalarına anlatarak gösterişten kaçınmak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz",
    },
    {
        "ID": 105,
        "Konu": "İbadette Huzur",
        "Öğüt": "İbadetler şekilsel değil, kalbi bir huzur ve şuurla eda edilmelidir.",
        "Örnek ve Tatbikat": "Namaz kılarken manasını düşünerek ve huşu ile rükû etmek.",
        "Eser ve Detaylı Kaynak": "Sözler",
    },
    {
        "ID": 106,
        "Konu": "Rızık Endişesi",
        "Öğüt": "Yarınki rızık için aşırı endişe duyulmamalı, rızkı veren Kerim olan Allah'tır.",
        "Örnek ve Tatbikat": "Gelecek kaygısını bırakıp bugünkü vazifeye odaklanmak.",
        "Eser ve Detaylı Kaynak": "Otuz İkinci Söz",
    },
    {
        "ID": 107,
        "Konu": "Zorluklara Direnç",
        "Öğüt": "Hizmet yolundaki zorluklar birer imtihan vesilesi olarak görülmelidir.",
        "Örnek ve Tatbikat": "Gelen sıkıntılara tebessümle göğüs germek.",
        "Eser ve Detaylı Kaynak": "Kastamonu Lahikası",
    },
    {
        "ID": 108,
        "Konu": "Haddini Bilmek",
        "Öğüt": "İnsan kendi kusurlarını görmeli, başkalarının kusuruyla meşgul olmamalıdır.",
        "Örnek ve Tatbikat": "Aynaya bakıp kendi hatalarını düzeltmeye odaklanmak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Lem'a",
    },
    {
        "ID": 109,
        "Konu": "Manevi Temizlik",
        "Öğüt": "Kalp ve ruh, günahların ve manevi kirlerin pasından bolca istiğfarla arındırılmalıdır.",
        "Örnek ve Tatbikat": "Günde yüz defa istiğfar çekmeyi alışkanlık haline getirmek.",
        "Eser ve Detaylı Kaynak": "Yirmi Dokuzuncu Lem'a",
    },
    {
        "ID": 110,
        "Konu": "Cömertlik",
        "Öğüt": "İnsan elindekileri Allah yolunda infak etmekten çekinmemelidir.",
        "Örnek ve Tatbikat": "İhtiyaç sahibi birini gördüğünde elindeki imkanı paylaşmak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 111,
        "Konu": "Hakka Teslimiyet",
        "Öğüt": "Hakikat zuhur ettiğinde nefis aradan çıkarılarak derhal teslim olunmalıdır.",
        "Örnek ve Tatbikat": "Hatalı bir düşünceden hakikati görünce anında vazgeçmek.",
        "Eser ve Detaylı Kaynak": "Muhakemat",
    },
    {
        "ID": 112,
        "Konu": "Kardeş Sevgisi",
        "Öğüt": "Müminler birbirlerini menfaatsiz ve sadece Allah için sevmelidir.",
        "Örnek ve Tatbikat": "Dostunu makamından veya malından ötürü değil, imanı sebebiyle sevmek.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Lem'a",
    },
    {
        "ID": 113,
        "Konu": "Faydalı Konuşma",
        "Öğüt": "Malayani (faydasız) sözlerden dil muhafaza edilmeli, hikmetli konuşulmalıdır.",
        "Örnek ve Tatbikat": "Boş laf eden meclislerde sükutu tercih etmek.",
        "Eser ve Detaylı Kaynak": "Lem'alar",
    },
    {
        "ID": 114,
        "Konu": "Nasihat Dinleme",
        "Öğüt": "Yapılan yapıcı eleştiriler ve nasihatler gurur yapmadan dinlenmelidir.",
        "Örnek ve Tatbikat": "Bir dostun ikazını teşekkürle karşılamak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 115,
        "Konu": "Zikir ve Fikir",
        "Öğüt": "Dil Allah'ı zikrederken, akıl kainatı tefekkürle meşgul olmalıdır.",
        "Örnek ve Tatbikat": "Yürüyüş yaparken essmayı zikretmek.",
        "Eser ve Detaylı Kaynak": "Otuz Üçüncü Söz",
    },
    {
        "ID": 116,
        "Konu": "Akraba Gözetme",
        "Öğüt": "Sıla-i rahim ihmal edilmemeli, akrabalarla olan bağlar diri tutulmalıdır.",
        "Örnek ve Tatbikat": "Bayramlarda ve özel günlerde büyükleri ziyaret etmek.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 117,
        "Konu": "Misafirperverlik",
        "Öğüt": "Eve gelen misafire ikramda bulunulmalı, güler yüzle ağırlanmalıdır.",
        "Örnek ve Tatbikat": "Misafiri en iyi şekilde konuk edip memnun göndermek.",
        "Eser ve Detaylı Kaynak": "Lem'alar",
    },
    {
        "ID": 118,
        "Konu": "Hırsın Zararı",
        "Öğüt": "Hırs göstermek rızkı artırmaz, aksine insanı manen yorar ve mahrum bırakır.",
        "Örnek ve Tatbikat": "Daha çok mal mülk hırsıyla sağlığı tehlikeye atmamak.",
        "Eser ve Detaylı Kaynak": "Ondokuzuncu Lem'a",
    },
    {
        "ID": 119,
        "Konu": "Haramdan Kaçınma",
        "Öğüt": "Şüpheli şeylerden dahi uzak durularak takva dairesinde yaşanmalıdır.",
        "Örnek ve Tatbikat": "Helalliğinden şüphe edilen gıda veya kazançtan sakınmak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 120,
        "Konu": "Emaneti Koruma",
        "Öğüt": "Hayat ve beden gibi büyük emanetler israf edilmemelidir.",
        "Örnek ve Tatbikat": "Vücut sağlığına özen gösterip zararlı alışkanlıklardan kaçınmak.",
        "Eser ve Detaylı Kaynak": "Asâ-yı Musa",
    },
    {
        "ID": 121,
        "Konu": "Hakikate Sadakat",
        "Öğüt": "Nefsi argümanlar uğruna hakikat perdelenmemelidir.",
        "Örnek ve Tatbikat": "Doğru bildiğini savunurken hakkaniyet ölçüsünden sapmamak.",
        "Eser ve Detaylı Kaynak": "Muhakemat",
    },
    {
        "ID": 122,
        "Konu": "Manevi Terakki",
        "Öğüt": "Manevi derecelerde kibre düşmemek için daima aşağı seviyedekilere bakılmalıdır.",
        "Örnek ve Tatbikat": "İbadetlerde kendine güvenip ucuba girmemek.",
        "Eser ve Detaylı Kaynak": "Yirminci Lem'a",
    },
    {
        "ID": 123,
        "Konu": "Sabit-kadem Olma",
        "Öğüt": "Hizmet yolunda rüzgarlar ne kadar sert esse de sabit-kadem durulmalıdır.",
        "Örnek ve Tatbikat": "Dış etkenlerden etkilenmeden istikamet üzere kalmak.",
        "Eser ve Detaylı Kaynak": "Kastamonu Lahikası",
    },
    {
        "ID": 124,
        "Konu": "Fedakarlık",
        "Öğüt": "Kardeşlerin huzuru için kendi haklarından feragat edebilmek erdemdir.",
        "Örnek ve Tatbikat": "Ortak işlerde arkadaşına öncelik tanımak.",
        "Eser ve Detaylı Kaynak": "Barla Lahikası",
    },
    {
        "ID": 125,
        "Konu": "Kini Unutma",
        "Öğüt": "Müminler arasında kin ve düşmanlık uzun sürmemeli, çabuk barışılmalıdır.",
        "Örnek ve Tatbikat": "Küs olunan kişiyle ilk adımı atıp barışmak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Lem'a",
    },
    {
        "ID": 126,
        "Konu": "Ölüm Hatırlatması",
        "Öğüt": "Lezzetleri acılaştıran ölümü çokça hatırlamak nefsaniyeti kırar.",
        "Örnek ve Tatbikat": "Mezarlık ziyaretlerini düzenli olarak tekrarlamak.",
        "Eser ve Detaylı Kaynak": "Yirminci Söz",
    },
    {
        "ID": 127,
        "Konu": "İbadet Zevki",
        "Öğüt": "İbadetler bir yük olarak değil, ruhun gıdası ve sevinci olarak görülmelidir.",
        "Örnek ve Tatbikat": "Namazı büyük bir iştiyak ve ferahla eda etmek.",
        "Eser ve Detaylı Kaynak": "Dokuzuncu Söz",
    },
    {
        "ID": 128,
        "Konu": "Kötü Zan",
        "Öğüt": "Delilsiz olarak başkaları hakkında kötü zan beslemekten sakınılmalıdır.",
        "Örnek ve Tatbikat": "İnsanlar hakkında peşin hüküm vermekten kaçınmak.",
        "Eser ve Detaylı Kaynak": "Lem'alar",
    },
    {
        "ID": 129,
        "Konu": "İlim Paylaşımı",
        "Öğüt": "Öğrenilen hakikatler başkalarıyla paylaşılmalı, zekatı verilmelidir.",
        "Örnek ve Tatbikat": "Bildiği imani bir konuyu çevresindekilere anlatmak.",
        "Eser ve Detaylı Kaynak": "Barla Lahikası",
    },
    {
        "ID": 130,
        "Konu": "Yalanın Zararı",
        "Öğüt": "En masum görünen durumlarda bile yalan söylemekten kesinlikle kaçınılmalıdır.",
        "Örnek ve Tatbikat": "Şaka yollu dahi yalan söyleme alışkanlığı edinmemek.",
        "Eser ve Detaylı Kaynak": "Yirminci Mektup",
    },
    {
        "ID": 131,
        "Konu": "Girişimci Ruh",
        "Öğüt": "Meşru dairede rızkı aramak için tembellik etmeden hareket edilmelidir.",
        "Örnek ve Tatbikat": "Yeni ve hayırlı projeler için çalışmaya koyulmak.",
        "Eser ve Detaylı Kaynak": "Yirmi Dördüncü Söz",
    },
    {
        "ID": 132,
        "Konu": "Manevi Kalkan",
        "Öğüt": "Günahlardan korunmak için sabır ve namaz en büyük kalkandır.",
        "Örnek ve Tatbikat": "Nefis zorlandığında namaza ve sabra sığınmak.",
        "Eser ve Detaylı Kaynak": "Yirmi Birinci Mektup",
    },
    {
        "ID": 133,
        "Konu": "Müsbet Düşünce",
        "Öğüt": "Olaylara hep bardağın dolu tarafından bakıp hüsn-ü zan edilmelidir.",
        "Örnek ve Tatbikat": "Olumsuzluklarda bile bir hayır aramak.",
        "Eser ve Detaylı Kaynak": "Emirdağ Lahikası",
    },
    {
        "ID": 134,
        "Konu": "Şefkatli Yaklaşım",
        "Öğüt": "İnsanları irşat ederken veya uyarırken sert değil, şefkatli olunmalıdır.",
        "Örnek ve Tatbikat": "Hata yapan birine kırıcı değil, merhametli bir lisanla yaklaşmak.",
        "Eser ve Detaylı Kaynak": "Şualar",
    },
    {
        "ID": 135,
        "Konu": "Dürüst Ticaret",
        "Öğüt": "Ticarette dürüstlük ve güvenilirlik en büyük sermayedir.",
        "Örnek ve Tatbikat": "Alacak verecek hesaplarında son derece titiz davranmak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 136,
        "Konu": "İsraftan Kaçınma",
        "Öğüt": "Elektrik, su ve ekmek gibi en küçük nimetler bile israf edilmemelidir.",
        "Örnek ve Tatbikat": "Boş yanan lambaları kapatıp muslukları damlatmayacak şekilde sıkmak.",
        "Eser ve Detaylı Kaynak": "Ondokuzuncu Lem'a",
    },
    {
        "ID": 137,
        "Konu": "Ahiret Yatırımı",
        "Öğüt": "Dünya menfaatleri ahiret kazançlarına tercih edilmemelidir.",
        "Örnek ve Tatbikat": "Geçici dünya zevkleri için ebedi saadeti tehlikeye atmamak.",
        "Eser ve Detaylı Kaynak": "Otuz İkinci Söz",
    },
    {
        "ID": 138,
        "Konu": "Manevi Dostluk",
        "Öğüt": "Hakiki dostlar insanı Allah'a yaklaştıran onurlu kişilerdir.",
        "Örnek ve Tatbikat": "İbadet ve ilim meclislerinde ortak dostluklar kurmak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 139,
        "Konu": "Kötü Arkadaş",
        "Öğüt": "İnsanı manen düşüren kötü arkadaşlarla bağlar nazikçe kesilmelidir.",
        "Örnek ve Tatbikat": "Zararlı çevrelerden uzak durup sağlıklı sosyal çevre edinmek.",
        "Eser ve Detaylı Kaynak": "Gençlik Rehberi",
    },
    {
        "ID": 140,
        "Konu": "Kader Rızası",
        "Öğüt": "Kaderin yazısına rıza göstermek kalbe huzur ve sekunet verir.",
        "Örnek ve Tatbikat": "Değiştirilemeyecek durumlar karşısında teslimiyet göstermek.",
        "Eser ve Detaylı Kaynak": "Yirmi Altıncı Söz",
    },
    {
        "ID": 141,
        "Konu": "Nefis Eğitimi",
        "Öğüt": "Nefsin arzularına her zaman boyun eğilmeyip zaman zaman muhalefet edilmelidir.",
        "Örnek ve Tatbikat": "Nefsin hoşuna gitmeyen ama hayırlı olan işlere öncelik vermek.",
        "Eser ve Detaylı Kaynak": "Mesnevi-i Nuriye",
    },
    {
        "ID": 142,
        "Konu": "Gönül Almak",
        "Öğüt": "İstemeden kırılan kalplerin telafisi için derhal gönül alınmalıdır.",
        "Örnek ve Tatbikat": "Kırgınlık yaşayan kişiye gidip tatlı dille tatlıya bağlamak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 143,
        "Konu": "Kur'an Okuma",
        "Öğüt": "Kur'an'ı sadece Arapçasından değil, manasını anlaşılmaya çalışarak okumak gerekir.",
        "Örnek ve Tatbikat": "Okunan ayetin Türkçe mealini ve tefsirine de göz atmak.",
        "Eser ve Detaylı Kaynak": "Yirmi Beşinci Söz",
    },
    {
        "ID": 144,
        "Konu": "Hizmet Şükrü",
        "Öğüt": "İman hizmetinde bulunmak büyük bir nimet olup, şükrü lüzumludur.",
        "Örnek ve Tatbikat": "Hizmet imkanı bulduğu için her an hamdetmek.",
        "Eser ve Detaylı Kaynak": "Barla Lahikası",
    },
    {
        "ID": 145,
        "Konu": "Istigfar Bilinci",
        "Öğüt": "Hataların farkına varıldığı anda istiğfara sarılmak en büyük kalkanıdır.",
        "Örnek ve Tatbikat": "Günah işleme meyli geldiğinde hemen istiğfar etmek.",
        "Eser ve Detaylı Kaynak": "Yirmi Dokuzuncu Lem'a",
    },
    {
        "ID": 146,
        "Konu": "Hizmet İstikameti",
        "Öğüt": "İman hizmetinde sağa sola sapmadan istikamet üzere yürünmelidir.",
        "Örnek ve Tatbikat": "Şahsi menfaatleri davanın önüne geçirmemek.",
        "Eser ve Detaylı Kaynak": "Kastamonu Lahikası",
    },
    {
        "ID": 147,
        "Konu": "Zamanın Kıymeti",
        "Öğüt": "Geçen her saniye ömür sermayesinden eksiltmektedir, boş geçirilmemelidir.",
        "Örnek ve Tatbikat": "Sosyal medyada veya boş işlerde saatleri harcamamak.",
        "Eser ve Detaylı Kaynak": "Birinci Söz",
    },
    {
        "ID": 148,
        "Konu": "Manevi Yardımlaşma",
        "Öğüt": "Kardeşlerin dualarında birbirine yer vermesi manevi kuvveti artırır.",
        "Örnek ve Tatbikat": "Dostların isimlerini vererek dua halkaları oluşturmak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 149,
        "Konu": "Ahlaki Olgunluk",
        "Öğüt": "Gerçek olgunluk, zor anlarda bile ahlaktan ödün vermemektir.",
        "Örnek ve Tatbikat": "Kriz anlarında sükuneti ve nezaketi korumak.",
        "Eser ve Detaylı Kaynak": "Mesnevi-i Nuriye",
    },
    {
        "ID": 150,
        "Konu": "İman Hakikatleri",
        "Öğüt": "İman hakikatleri hem aklen hem kalben inceden inceye incelenmelidir.",
        "Örnek ve Tatbikat": "Akli delilleri tefekkür ederek imanı tahkiki dereceye taşımak.",
        "Eser ve Detaylı Kaynak": "Sözler Külliyatı",
    },
    {
        "ID": 151,
        "Konu": "Mütevazı Yaşam",
        "Öğüt": "Lüks ve şatafattan uzak, sade bir hayat tarzı benimsenmelidir.",
        "Örnek ve Tatbikat": "İhtiyaç fazlası harcamalardan kaçınıp sade yaşamak.",
        "Eser ve Detaylı Kaynak": "Lem'alar",
    },
    {
        "ID": 152,
        "Konu": "Hakkı Savunma",
        "Öğüt": "Hakkın ve adaletin hakim olması için meşru dairede gayret edilmelidir.",
        "Örnek ve Tatbikat": "Haksızlığa uğrayan birini gördüğünde ona destek olmak.",
        "Eser ve Detaylı Kaynak": "Divan-ı Harb-i Örfî",
    },
    {
        "ID": 153,
        "Konu": "Nefis Muhasebesi",
        "Öğüt": "Hatalardan ders çıkarmak için düzenli nefis muhasebesi şarttır.",
        "Örnek ve Tatbikat": "Haftalık veya günlük planla yapılanları gözden geçirmek.",
        "Eser ve Detaylı Kaynak": "Sözler",
    },
    {
        "ID": 154,
        "Konu": "İhlas Sırrı",
        "Öğüt": "Amellerde başkalarının beğenisini aramak ihlası bozar, sakınılmalıdır.",
        "Örnek ve Tatbikat": "Gizli yapılan ibadetlerin alenileştirilmesinden kaçınmak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz",
    },
    {
        "ID": 155,
        "Konu": "Kardeş Haklarına Riayet",
        "Öğüt": "Mümin kardeşinin hakkına girmemek için titiz davranılmalıdır.",
        "Örnek ve Tatbikat": "Kimsenin malına, namusuna ve hakkına el uzatmamak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 156,
        "Konu": "Şükrün Edası",
        "Öğüt": "Nimetlerin zeval bulmaması için fiili ve kavli şükür unutulmamalıdır.",
        "Örnek ve Tatbikat": "Sağlık nimetinin şükrü için bedene iyi bakmak.",
        "Eser ve Detaylı Kaynak": "Yirmi Sekizinci Söz",
    },
    {
        "ID": 157,
        "Konu": "Musibetlere Metanet",
        "Öğüt": "Musibetler günahlara kefaret olduğundan sabırla karşılanmalıdır.",
        "Örnek ve Tatbikat": "Gelen dertleri manevi bir temizlik fırsatı olarak görmek.",
        "Eser ve Detaylı Kaynak": "İkinci Lem'a",
    },
    {
        "ID": 158,
        "Konu": "Dua Israrı",
        "Öğüt": "Duaların kabulü için ümitsizliğe düşmeden ısrarla dua edilmelidir.",
        "Örnek ve Tatbikat": "Uzun süredir istenen hayırlı bir dua için her namaz sonrası el açmak.",
        "Eser ve Detaylı Kaynak": "Yirmi Üçüncü Söz",
    },
    {
        "ID": 159,
        "Konu": "Hizmet Sabrı",
        "Öğüt": "İman hizmetinde netice Allah'a bırakılmalı, vazife ise sabırla yapılmalıdır.",
        "Örnek ve Tatbikat": "İnsanların hidayete gelip gelmemesini dert etmeyip sadece tebliği yapmak.",
        "Eser ve Detaylı Kaynak": "Kastamonu Lahikası",
    },
    {
        "ID": 160,
        "Konu": "Ahlaki Duruş",
        "Öğüt": "Mümin her halükarda ahlakıyla örnek bir şahsiyet olmalıdır.",
        "Örnek ve Tatbikat": "Sözü özü bir, güvenilir bir insan profili çizmek.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 161,
        "Konu": "İlim Sevgisi",
        "Öğüt": "İlim tahsil etmek ve okumak hayatın vazgeçilmez bir parçası olmalıdır.",
        "Örnek ve Tatbikat": "Günün belirli bir saatini okumaya ve araştırmaya ayırmak.",
        "Eser ve Detaylı Kaynak": "İşaratü'l-İ'caz",
    },
    {
        "ID": 162,
        "Konu": "Gönül Zenginliği",
        "Öğüt": "Hakiki zenginlik mal çokluğu değil, gönül kanaatidir.",
        "Örnek ve Tatbikat": "Azla yetinip açgözlülükten uzak durmak.",
        "Eser ve Detaylı Kaynak": "Ondokuzuncu Lem'a",
    },
    {
        "ID": 163,
        "Konu": "Hakikati Arama",
        "Öğüt": "Ömür boyunca hakikati aramak ve bulduğu yolda sebat etmek gerekir.",
        "Örnek ve Tatbikat": "İlmi ve imani eserleri derinlemesine incelemek.",
        "Eser ve Detaylı Kaynak": "Sözler",
    },
    {
        "ID": 164,
        "Konu": "Tevazu Esası",
        "Öğüt": "Başarılar ve güzellikler nefse mal edilmeyip Allah'tan bilinmelidir.",
        "Örnek ve Tatbikat": "Övüldüğünde şımarmayıp hamdetmek.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz",
    },
    {
        "ID": 165,
        "Konu": "Kardeş Yardımı",
        "Öğüt": "Mümin kardeşinin maddi ve manevi dar gününde yardımına koşulmalıdır.",
        "Örnek ve Tatbikat": "Borçlu bir dosta imkan ölçüsünde destek olmak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 166,
        "Konu": "Nefisle Mücadele",
        "Öğüt": "Cihadın en büyüğü olan nefsani arzularla mücadele asla bırakılmamalıdır.",
        "Örnek ve Tatbikat": "Kötü alışkanlıklara meyil olduğunda iradeyle karşı koymak.",
        "Eser ve Detaylı Kaynak": "Yirmi Dokuzuncu Mektup",
    },
    {
        "ID": 167,
        "Konu": "Hatalardan Ders",
        "Öğüt": "Geçmişteki hatalardan ders çıkarılarak geleceğe daha dikkatli bakılmalıdır.",
        "Örnek ve Tatbikat": "Aynı yanlışı ikinci kez yapmamak için tedbir almak.",
        "Eser ve Detaylı Kaynak": "Mesnevi-i Nuriye",
    },
    {
        "ID": 168,
        "Konu": "Selamlaşma",
        "Öğüt": "Aradaki muhabbeti artırmak için selam yaygınlaştırılmalıdır.",
        "Örnek ve Tatbikat": "Tanıdık tanımadık müminlere güler yüzle selam vermek.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 169,
        "Konu": "Zaman Yönetimi",
        "Öğüt": "Vakitler en kıymetli hazine gibi planlı ve verimli kullanılmalıdır.",
        "Örnek ve Tatbikat": "Günlük iş listesi yapıp vakti israf etmemek.",
        "Eser ve Detaylı Kaynak": "Birinci Söz",
    },
    {
        "ID": 170,
        "Konu": "İhlasın Korunması",
        "Öğüt": "Hizmetlerin zayi olmaması için ihlas sırrına sıkıca sarılmalıdır.",
        "Örnek ve Tatbikat": "Yaptığı iyilikleri başa kakmaktan kesinlikle sakınmak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz",
    },
    {
        "ID": 171,
        "Konu": "Manevi Huzur",
        "Öğüt": "Kalp huzuru ancak Allah'ı anmak ve Kur'an okumakla elde edilir.",
        "Örnek ve Tatbikat": "Sıkıntılı anlarda tesbihat ve zikirle kalbi ferahlatmak.",
        "Eser ve Detaylı Kaynak": "Ra'd Suresi Tefsiri / Lem'alar",
    },
    {
        "ID": 172,
        "Konu": "Hakka Bağlılık",
        "Öğüt": "Hiçbir makam veya menfaat hakikatin üstünde tutulmamalıdır.",
        "Örnek ve Tatbikat": "Çıkar çatışmalarında doğruluktan taviz vermemek.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 173,
        "Konu": "Şefkatli Eğitim",
        "Öğüt": "Çocuklara ve gençlere yaklaşırken şefkat ve sevgi temel alınmalıdır.",
        "Örnek ve Tatbikat": "Onları eğitirken kaba kuvvet yerine ikna ve sevgiyi seçmek.",
        "Eser ve Detaylı Kaynak": "Şualar",
    },
    {
        "ID": 174,
        "Konu": "Dost Vefası",
        "Öğüt": "Vefakar dostluklar hayatın en değerli manevi hazinelerindendir.",
        "Örnek ve Tatbikat": "Eski dostları unutmayıp zor günlerinde arayıp sormak.",
        "Eser ve Detaylı Kaynak": "Barla Lahikası",
    },
    {
        "ID": 175,
        "Konu": "Kötülüğe Karşı Durma",
        "Öğüt": "Haksızlıklar karşısında susup kalmayıp meşru dille tepki gösterilmelidir.",
        "Örnek ve Tatbikat": "Görülen bir haksızlığı ilgili makamlara veya usulünce uyarmak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 176,
        "Konu": "Rızık Şükrü",
        "Öğüt": "Yenilen her lokmaya şükredilerek israftan kaçınılmalıdır.",
        "Örnek ve Tatbikat": "Sofradaki nimetlerin kıymetini bilip çöpe atmamak.",
        "Eser ve Detaylı Kaynak": "Ondokuzuncu Lem'a",
    },
    {
        "ID": 177,
        "Konu": "Manevi Gözetim",
        "Öğüt": "İnsan kendi manevi dünyasını sürekli denetim altında tutmalıdır.",
        "Örnek ve Tatbikat": "Günlük eksileri artıları tartarak manevi kar-zarar hesabı yapmak.",
        "Eser ve Detaylı Kaynak": "Sözler",
    },
    {
        "ID": 178,
        "Konu": "İbadet Huşusu",
        "Öğüt": "Namaz ve diğer ibadetler huzur-u ilahide bilinciyle yapılmalıdır.",
        "Örnek ve Tatbikat": "Namazda başka şeyleri düşünmemeye gayret etmek.",
        "Eser ve Detaylı Kaynak": "Dokuzuncu Söz",
    },
    {
        "ID": 179,
        "Konu": "Cemaat Ruhu",
        "Öğüt": "Birlik ve beraberlik ruhu korunarak ortak maslahatlar gözetilmelidir.",
        "Örnek ve Tatbikat": "Ortak çalışmalarda bireysel egoları bir kenara bırakmak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz",
    },
    {
        "ID": 180,
        "Konu": "Sabır Sebatı",
        "Öğüt": "Hizmet yolunda karşılaşılan meşakkatler sabırla karşılanıp sebat edilmelidir.",
        "Örnek ve Tatbikat": "Yorulma emareleri gösterdiğinde gayreti tazelemek.",
        "Eser ve Detaylı Kaynak": "Kastamonu Lahikası",
    },
    {
        "ID": 181,
        "Konu": "Hakkaniyet",
        "Öğüt": "İnsanlar arasında hükmederken veya karar verirken tam adalet gözetilmelidir.",
        "Örnek ve Tatbikat": "Akraba dahi olsa haksızlık karşısında adaletten ayrılmamak.",
        "Eser ve Detaylı Kaynak": "Divan-ı Harb-i Örfî",
    },
    {
        "ID": 182,
        "Konu": "Tefekkür Derinliği",
        "Öğüt": "Kainattaki her bir zerre Allah'ın varlığına delil olarak tefekkür edilmelidir.",
        "Örnek ve Tatbikat": "Gökyüzüne bakıp yıldızların nizamını düşünmek.",
        "Eser ve Detaylı Kaynak": "Otuz Üçüncü Söz",
    },
    {
        "ID": 183,
        "Konu": "Nefis Terbiyesi",
        "Öğüt": "Nefsin arzularına her zaman boyun eğilmeyip zaman zaman muhalefet edilmelidir.",
        "Örnek ve Tatbikat": "Nefsin hoşuna gitmeyen ama hayırlı olan işlere öncelik vermek.",
        "Eser ve Detaylı Kaynak": "Mesnevi-i Nuriye",
    },
    {
        "ID": 184,
        "Konu": "Dürüst Yaşam",
        "Öğüt": "Özde ve sözde dürüstlük müminin en temel şiarı olmalıdır.",
        "Örnek ve Tatbikat": "Ne ise o görünmek, ikiyüzlü davranışlardan kaçınmak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 185,
        "Konu": "Gönül Kırmama",
        "Öğüt": "Gönül yıkmak Kabe yıkmak gibi büyük vebaldir, çok dikkat edilmelidir.",
        "Örnek ve Tatbikat": "Söz söylerken karşı tarafın kalbini kırıp kırmayacağını tartmak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 186,
        "Konu": "İlim ve Hikmet",
        "Öğüt": "İlim hikmetle harmanlanmalı, insana ve topluma faydalı kılınmalıdır.",
        "Örnek ve Tatbikat": "Öğrenilen bilgileri insanlığın hayrına kullanmak.",
        "Eser ve Detaylı Kaynak": "İşaratü'l-İ'caz",
    },
    {
        "ID": 187,
        "Konu": "Hizmet Şevki",
        "Öğüt": "Hizmet kervanında geride kalmamak için şevkle çalışmaya devam edilmelidir.",
        "Örnek ve Tatbikat": "Hizmetlere faal olarak aktif katılım sağlamak.",
        "Eser ve Detaylı Kaynak": "Barla Lahikası",
    },
    {
        "ID": 188,
        "Konu": "Manevi Temkin",
        "Öğüt": "Hallerde aşırılıktan kaçınılarak temkinli ve dengeli olunmalıdır.",
        "Örnek ve Tatbikat": "Aşırı neşe veya aşırı üzüntüde dahi ölçüyü kaçırmamak.",
        "Eser ve Detaylı Kaynak": "Mesnevi-i Nuriye",
    },
    {
        "ID": 189,
        "Konu": "Kardeş Hukuku",
        "Öğüt": "Mümin kardeşinin gıyabında onu korumak ve hakkını gözetmek esastır.",
        "Örnek ve Tatbikat": "Ortamda olmayan bir dostun arkasından atılan iftiraları önlemek.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Lem'a",
    },
    {
        "ID": 190,
        "Konu": "Hırsın Tedavisi",
        "Öğüt": "Hırs hastalığının tek ilacı kanaat ve iktisat düsturuna sarılmaktır.",
        "Örnek ve Tatbikat": "Sahip olduklarıyla yetinip fazlası için hırslanmamak.",
        "Eser ve Detaylı Kaynak": "Ondokuzuncu Lem'a",
    },
    {
        "ID": 191,
        "Konu": "Ahiret Bilinci",
        "Öğüt": "Dünyanın geçici, ahiretin ise ebedi olduğu bilinciyle hareket edilmelidir.",
        "Örnek ve Tatbikat": "Yatırım yaparken sadece dünyaya değil ahirete de yatırım yapmak.",
        "Eser ve Detaylı Kaynak": "Otuz İkinci Söz",
    },
    {
        "ID": 192,
        "Konu": "Güzel Ahlak",
        "Öğüt": "Müslüman güzel ahlakı ile etrafına örnek ve huzur kaynağı olmalıdır.",
        "Örnek ve Tatbikat": "Çevrede dürüstlüğü ve kibarlığı ile tanınmak.",
        "Eser ve Detaylı Kaynak": "Mektubat",
    },
    {
        "ID": 193,
        "Konu": "İhlas Sınavı",
        "Öğüt": "En zor anlarda dahi ihlastan taviz vermeden yola devam edilmelidir.",
        "Örnek ve Tatbikat": "Sıkıntılı dönemlerde menfaat gözetmeksizin hizmete sadık kalmak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz",
    },
    {
        "ID": 194,
        "Konu": "Dua Samimiyeti",
        "Öğüt": "Dualar kalpten gelen derin bir ihlas ve samimiyetle yapılmalıdır.",
        "Örnek ve Tatbikat": "Ezberden ziyade hissederek, kalben yakarışta bulunmak.",
        "Eser ve Detaylı Kaynak": "Yirmi Üçüncü Söz",
    },
    {
        "ID": 195,
        "Konu": "Şükrün Genişliği",
        "Öğüt": "Şükür sadece dille değil, azaların ve kalbin de şükrüyle tamamlanır.",
        "Örnek ve Tatbikat": "Gözü haramdan, eli kötülükten çekerek azalarla şükretmek.",
        "Eser ve Detaylı Kaynak": "Yirmi Sekizinci Söz",
    },
    {
        "ID": 196,
        "Konu": "Müspet Hareket Esası",
        "Öğüt": "Her şartta müsbet hareket edilip asayişe tam riayet edilmelidir.",
        "Örnek ve Tatbikat": "Olaylar ne kadar kışkırtıcı olursa olsun sükuneti korumak.",
        "Eser ve Detaylı Kaynak": "Emirdağ Lahikası",
    },
    {
        "ID": 197,
        "Konu": "Hizmet Sadakati",
        "Öğüt": "İman ve Kur'an hizmetinde son nefese kadar sadakatle sebat olunmalıdır.",
        "Örnek ve Tatbikat": "Yaş ilerlese dahi manevi gayretten geri durmamak.",
        "Eser ve Detaylı Kaynak": "Kastamonu Lahikası",
    },
    {
        "ID": 198,
        "Konu": "Nefis Terbiyesi",
        "Öğüt": "Nefsin desiselerine karşı uyanık olunup daima kurani düsturlarla hareket edilmelidir.",
        "Örnek ve Tatbikat": "Nefsin 'nasıl olsa bir şey olmaz' vesveselerine kulak asmamak.",
        "Eser ve Detaylı Kaynak": "Yirmi Dokuzuncu Mektup",
    },
    {
        "ID": 199,
        "Konu": "Kardeşlik Hukuku",
        "Öğüt": "Müminler arasındaki kardeşlik bağı tüm maddi bağların üstünde tutulmalıdır.",
        "Örnek ve Tatbikat": "Dostların sevincinde de kederinde de ortak olmak.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Lem'a",
    },
    {
        "ID": 200,
        "Konu": "Rıza-i İlahi",
        "Öğüt": "Hayattaki en nihai gaye yalnız ve yalnız Cenab-ı Hakk'ın rızasını kazanmaktır.",
        "Örnek ve Tatbikat": "Yapılan her hayırlı amelin arkasında sadece 'Ya Rabbi rızan için' diyebilmek.",
        "Eser ve Detaylı Kaynak": "Yirmi İkinci Söz (İhlas Risalesi)",
    },
]

# DataFrame Oluşturma
df = pd.DataFrame(veriler)

# --- ARAYÜZ BAŞLIĞI VE AÇIKLAMA ---
st.title("📖 Risale-i Nur Nasihat, Düstur ve Örnekler Rehberi (200 Madde Tam Liste)")
st.markdown(
    "Bediüzzaman Said Nursî’nin eserlerinden derlenen **200 adet eksiksiz** temel düsturu, "
    "ilgili örnekleri ve detaylı eser kaynaklarını sol menüden filtreleyerek inceleyebilirsiniz."
)

# --- SOL MENÜ (FİLTRELEME VE YASAL BİLGİ) ---
st.sidebar.header("🔍 Filtreleme Paneli")

# Konu Listesi
tum_konular = ["Tümü"] + sorted(df["Konu"].unique().tolist())
secilen_konu = st.sidebar.selectbox("Konu Seçin:", tum_konular)

# Eser veya Kaynak Filtresi
eser_filtresi = st.sidebar.text_input(
    "Eser / Kaynak Ara (Örn: İhlas, Lem'a, Sözler):", ""
)

st.sidebar.markdown("---")
with st.sidebar.expander("⚖️ Yasal Uyarı & Telif Hakları"):
    st.markdown(
        "Bu portaldaki tüm içerikler yalnızca **manevi gelişim ve bilgi amaçlıdır**.\n\n"
        "• **Kopyalanamaz ve Çoğaltılamaz.**\n"
        "• **Ticari amaçla kullanılamaz.**\n"
        "• Tüm hakları saklıdır."
    )

# --- FİLTRELEME MANTIĞI ---
filtrelenmis_df = df.copy()
if secilen_konu != "Tümü":
    filtrelenmis_df = filtrelenmis_df[
        filtrelenmis_df["Konu"] == secilen_konu
    ]

if eser_filtresi:
    filtrelenmis_df = filtrelenmis_df[
        filtrelenmis_df["Eser ve Detaylı Kaynak"]
        .str.lower()
        .str.contains(eser_filtresi.lower())
    ]

# --- SAĞ TARAF: SONUÇLAR VE KARTLAR ---
st.subheader(f"📋 Listelenen Düstur ve Örnek Sayısı: {len(filtrelenmis_df)}")
st.markdown("---")

# Tablo yerine her satırı dikeyde genişleyen, kaydırma çubuğu gerektirmeyen şık kartlar halinde listeleme
for index, row in filtrelenmis_df.iterrows():
    st.markdown(
        f"""
        <div class="nasihat-card">
            <div class="nasihat-header">#{row['ID']} - Konu: {row['Konu']}</div>
            <div class="nasihat-text"><b>Öğüt:</b> {row['Öğüt']}</div>
            <div class="nasihat-text"><b>Örnek ve Tatbikat:</b> {row['Örnek ve Tatbikat']}</div>
            <div class="nasihat-footer"><b>Kaynak:</b> {row['Eser ve Detaylı Kaynak']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- SAYFA ALT BİLGİSİ (FOOTER) ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>"
    "© 2026 Risale-i Nur Nasihat ve Düsturlar Veritabanı (200 Madde Tam Liste) | Sadece Manevi Gelişim ve Bilgi Amaçlıdır. "
    "İçerikler Kopyalanamaz ve Ticari Amaçla Kullanılamaz."
    "</div>",
    unsafe_allow_html=True,
)