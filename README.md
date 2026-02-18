# VisionPass
AI-powered biometric payment
# VisionPass: Otonom ve Temassız Biyometrik Ulaşım Ekosistemi

Ankara Üniversitesi Gıda Mühendisliği öğrencisi ve sistem mimarı adayı Zeynep Keskin tarafından, Turkcell "Yarının Teknoloji Liderleri" programı için geliştirilmiş bir vizyon projesidir. Bu proje, şehir içi mobilitede donanım bağımlılığını ortadan kaldırarak yolculara kesintisiz bir ulaşım deneyimi sunmayı hedefler.

### Çıkış Noktası ve Problem Tanımı
Mühendislik disiplininin temelinde yer alan proses optimizasyonunu, şehir içi ulaşım ağlarına entegre etmeyi hedefledim. Mevcut sistemlerdeki fiziksel turnikeler ve kart okutma zorunluluğu, özellikle yoğun saatlerde ciddi kapasite kayıplarına ve yüksek operasyonel maliyetlere yol açmaktadır. VisionPass, bu fiziksel bariyerleri tamamen dijitalleştirerek serbest akış prensibiyle çalışan sürdürülebilir bir altyapı sunar.

### Sistem Mimarisi ve İşleyiş
Sistem, istasyon giriş ve çıkışlarındaki mevcut kamera ağlarını uçta hesaplama teknolojisiyle akıllı hale getiren üç temel adımdan oluşur:

* **Algılama:** YOLOv8 modeli kullanılarak yüksek kalabalık ortamlarda milisaniyelik insan tespiti yapılır.
* **Doğrulama:** ArcFace algoritması ile kişilerin yüz biyometrisi anlık olarak dijital imza niteliğindeki matematiksel vektörlere dönüştürülür.
* **Otonom Tahsilat:** Yolcunun giriş ve çıkış yaptığı istasyonlar arasındaki mesafe hesaplanarak, ilgili ücret Paycell API üzerinden arka planda otomatik olarak tahsil edilir.

### Veri Mahremiyeti ve Güvenlik
Sistemin mimarisi Tasarımda Gizlilik ilkesi üzerine inşa edilmiştir. Kameralar tarafından algılanan ham görüntüler hiçbir sunucuda veya veritabanında saklanmaz. Yüz verisi anında geri döndürülemez şifreli hash kodlarına çevrilir. Ek olarak sistem, yalnızca Paycell uygulamasından açık rıza vermiş kullanıcılar için şifreli olarak çalışır.

### Teknoloji Yığını
* **Görüntü İşleme:** Python ve OpenCV
* **Yapay Zeka Modelleri:** YOLOv8 ve ArcFace
* **Nesne Takip Algoritmaları:** DeepSORT

### Kurulum (Installation)
Bu proje şu an Kavram Kanıtı (PoC) aşamasındadır. Simülasyon ortamındaki bağımlılıkları yüklemek için aşağıdaki komutu kullanabilirsiniz:

`pip install -r requirements.txt`

### Gelecek Vizyonu
Kısa vadeli hedefimiz, Paycell QR entegrasyonu ile hibrit bir geçiş modeli sunmaktır. Orta ve uzun vadede ise VisionPass protokolünü tüm toplu taşıma modlarında standart hale getirerek fiziksel turnike ve plastik kart bağımlılığını tamamen ortadan kaldırmayı hedefliyoruz.

### Yatırımcı Sunumu
VisionPass sisteminin finansal modelini, Turkcell ekosistemiyle olan sinerjisini, risk yönetimi senaryolarını ve gelecek yol haritasını detaylandırdığım sunum dosyasına, bu repoda yer alan **VisionPass_PitchDeck.pdf** belgesi üzerinden ulaşabilirsiniz.
