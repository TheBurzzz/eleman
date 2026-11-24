# Eleman — ortak durum notu

Bu dosya üç sohbetin (Asorti Aracı, Ölçü Tablosu Aracı, Eleman) ortak defteridir.
Her sohbet işe başlamadan önce bunu okur, iş bitince "Son durum" bölümünü günceller.

## Dallar (branch)

| Dal | Ne | Kural |
|---|---|---|
| `main` | Yayındaki **Eleman** (9 Kasım 2026'dan beri, 3.2.0; öncesinde Asorti Aracı 2.x). Kurulu programlar (iş bilgisayarı) güncellemeyi buradan alır. | Yalnız `eleman`'da hazır olan girer, ileri sararak: `git push origin eleman:main`. main'de ayrı iş yapılmaz. Her yayında `surum.json` sürümü artar (Releases'a kendiliğinden eklenir). |
| `eleman` | **Geliştirme dalı**: üç sohbet de burada çalışır. Evdeki deneme kurulumu bu daldan güncellenir. | Asorti, Ölçü ve Eleman düzeltmeleri buraya; hazır olunca main'e. |
| ~~`exe-deneme`~~ | **Kaldırıldı** (9 Kasım 2026): Asorti Aracı artık yalnız Eleman'ın içinde. | Asorti düzeltmesi `eleman`'da (aşağıda "Asorti ya da Ölçü değişince"). |
| ~~`surum-vX.Y.Z`, `arsiv`~~ | **Kaldırıldı** (7 Kasım 2026, kullanıcının isteği): eski sürümler artık GitHub **Releases**'ta (etiket `v1.0.0`…`v2.0.4`, `ilk-deneme`). | Yeni sürüm dalı açılmaz. |

## Değişmeyecekler (çalışan hiçbir şey bozulmasın diye)

- **Depo adı `eleman` OLDU** (kullanıcı 7 Kasım 2026 gece değiştirdi: "hepsi tek yerde, Eleman adı altında, düzenli dursun";
  eski adı `asorti-araci`). Varsayılan dal `eleman`, açıklama "Eleman · Asorti Aracı ve Ölçü Tablosu bir arada".
  Yerel klonlar: `git remote set-url origin https://github.com/TheBurzzz/eleman`. GitHub eski adresleri (git, raw.githubusercontent, codeload, API) yeni
  ada yönlendirir; iş bilgisayarındaki v2.0.4 bu yönlendirmeyle güncellenir. Eleman 3.1.0+ ikisini sırayla dener
  (`ElemanDepolari`: önce `TheBurzzz/eleman`, 404'te `TheBurzzz/asorti-araci`); kurulum `eleman-<dal>` ve `asorti-araci-<dal>`
  klasör adlarını tanır. Varsayılan dal `eleman` yapılır (depo sayfası ve Download ZIP Eleman'ı verir; güncelleyiciler dalı
  açıkça yazdığı için etkilenmez). **Eski adla yeni bir depo açılmaz** (yönlendirme bozulur). Sohbetler depoyu yeni adla
  (`TheBurzzz/eleman`) eklemeli. Ortak hafıza ayrı gizli depo olarak kalır (`eleman-hafiza`; anahtarlar yalnız ona erişir).
- **Program klasörü depoda `Eleman/`** (9 Kasım 2026'dan beri; önce `AsortiAraci/`). 3.2.0+ güncelleyici (Guncelleme.cs,
  sunucu.ps1) ve kurulum (Kurulum.ps1) iki adı da tanır (önce Eleman); derle.py, kabuk_yap.py ve surum.yml de. v2.x ve
  Eleman ≤3.1.0 yalnız `AsortiAraci/`'yi bildiği için artık güncellenemez (kullanıcı kabul etti: evdeki eski kurulum gerekirse
  GitHub'dan indirilip Kurulum.bat ile yeniden kurulur, ayarlar korunur). **Aşağıdaki eski notlarda geçen `AsortiAraci/...`
  depo yolları artık `Eleman/...`.**
- Kurulum klasörü `C:\AsortiAraci` aynı kalır (OTOPASTAL bağlantısı, WebView2 profili, çalışma sayfaları bu yolda).
- `AsortiAraci.exe` dosya adı şimdilik aynı; görünen ad (pencere, görev yöneticisi, bildirim, uyarılar) **Eleman**.
- Sunucu adresi `localhost:8642` aynı (sayfaların yerel kaydı bu adrese bağlı).

## Herkese açık depoya asla girmeyenler

- Okur-yazar ortak hafıza anahtarı (`github_pat_…`, `anahtar.txt`): yalnız kullanıcının bilgisayarlarında. Salt-okur anahtar
  yalnız karışık yazılmış hâliyle girer (aşağıda "Anahtarlar").
- Müşteri şablonları (`sablonlar.json`: müşteri adları, logolar), müşteri kağıtları/taramaları, KESİM RAPORLARI,
  deneme verileri (`base.json`). Bunlar gizli `eleman-hafiza` deposunda ya da Eleman sohbetinin çalışma alanında durur.
- Kök `.gitignore`: `anahtar.txt`, `guncelleme_anahtari.txt`, `sablonlar.json`, `olcu_sablonlar.json` yanlışlıkla eklenmesin.

## Anahtarlar (kullanıcının kararı, 6 Kasım 2026 gece)

Kullanıcı: "uygulamayı indirdiğim an kendinden anahtarlı olsun; müşteri bilgileri çok gizli değil." Önce gizli depo
düşünüldü; kullanıcı istemedi (başka bilgisayarda adını yazıp programı gösterebilmek, hesabına girmeden indirebilmek
istiyor). **Program deposu herkese açık kalır.** Karar:
- **Güncel karar (6 Kasım 2026, 22:58):** "her pc hem öğrensin hem öğretsin; 1 yıl sonra başka bir bilgisayara geçtiğimde
  sana 'bu benim bilgisayarım' demek zorunda kalmayayım." Asıl kullanım iş bilgisayarı, ev deneme. Bu yüzden **programın
  içindeki anahtar** (`SunucuOlcu.cs` → `OKUMA`, ters + "eleman-okuma" ile XOR + base64; GitHub'daki adı `eleman-okuma`,
  yalnız `eleman-hafiza`) her kurulumda kullanılır ve kullanıcı onu GitHub'da **Contents: Read and write** yapar
  (✓ 9 Kasım 2026'da iş bilgisayarından denendi: okuyor, yazabiliyor; deneme yanlış sha ile yapıldı, hiçbir şey değişmedi).
  Düz yazılmaz çünkü GitHub herkese açık depoda gördüğü anahtarı iptal eder; gizleme değildir, kurcalayan çözebilir
  (kullanıcı kabul etti: müşteriler gizli değil, başkası kullanmıyor). Başkası da kullanırsa öğrendikleri ortak olur.
- Sunucu `salt` hep false. Ölçü Tablosu yazmayı dener; GitHub 403 derse (anahtar yalnız okuyorsa) kendiliğinden yalnız
  okumaya geçer (`SYNC.salt`, "Ortak hafıza (okuma)"), bir sonraki açılışta yine dener.
- Koruma: ortak hafıza silinir ya da bilgisayarın bildiğinin yarısından azı kalırsa (`saves`, en az 20) o bilgisayardaki
  kopya geri yüklenir. Müşterilerden yarısı ya da fazlası (en az 2) birden kaybolursa yeniden gönderilir; tek tük kaybolan
  başka bilgisayarda silinmiştir, burada da silinir (yeni gönderilen 2 dk sayılmaz). GitHub her sürümü saklar.
- `anahtar.txt` (ayrı okur-yazar anahtar) artık şart değil; evde var, kalabilir (programdaki anahtar iptal edilse de o
  bilgisayar yazmaya devam eder). İş bilgisayarına konması gerekmiyor.
- Güncellemeler herkese açık yoldan, eskisi gibi. 3.0.2'deki `guncelleme_anahtari.txt` desteği boşta bekler (dosya yoksa
  hiçbir şey yapmaz); depo bir gün gizli yapılırsa işe yarar.

## Tasarım kararları (6 Kasım 2026, kullanıcı)

- **Eleman**: sarı tema. Simge: sarı kare üstünde siyah çizgili, kasketli yardımcı eleman (`sistem/eleman.svg`).
- **Asorti Aracı**: mavi, **aynen kalır**.
- **Ölçü Tablosu Aracı**: yeşil tema; simge Excel'i / tabloyu andıran yeşil tablo (`sistem/olcu.svg`). Cetvel/metre simgesi kaldırıldı.
  Kullanımı Asorti gibi: üst çubukta sekmeler ("Sayfa 1", "+ Yeni sayfa").
- Açık/koyu görünüm yalnız **⚙ Ayarlar → Görünüm** içinde (Açık / Koyu / Otomatik + Gece ışığı). Üst çubukta ayrı tema düğmesi yok.
- Ana sayfa Apple tasarımından örnek alır; üç uygulama aynı tasarım dilinde (Inter, cam kartlar, yumuşak gölgeler).
- "Created by Şamil Yeşil" imzası her yerde kalır.
- Eleman'ın ilk sürümünde **el yazısı okuma modeli** bulunacak (unutulmayacak).

## Ölçü Tablosu kaynağı

- Kaynak: `kaynak/olcu/src.html` + `kaynak/olcu/veri/` (ölçü sözlüğü vb.). Eleman içindeki hali:
  `python kaynak/olcu/derle.py` → `Eleman/olcu_tablosu_araci.html` (anahtarsız, şablonsuz).
- Masaüstündeki tek başına hali depo dışına derlenir: `derle.py --sablonlar <gizli> --anahtar <gizli> --cikti <depo dışı>`.
- Sunucu tarafı: `Eleman/sistem/uygulama/SunucuOlcu.cs` (yalnız `/olcu/...` adresleri), kitaplıklar `Eleman/sistem/olcu/`.

## Asorti ya da Ölçü değişince (9 Kasım 2026'dan beri)

- **Asorti düzeltmesi** (Asorti sohbeti): `eleman` dalında `Eleman/asorti_araci.html` düzeltilir (exe-deneme yok).
  Asorti'nin sekmeli penceresi (sekmeler, Gerber durumu, güncelleme) değişecekse kaynağı `kaynak/eleman/asorti_kabugu.html`
  (Asorti 2.0.4'ün `uygulama.html`'i) düzeltilir ve kabuk yeniden üretilir:
  `python3 kaynak/eleman/kabuk_yap.py kaynak/eleman/asorti_kabugu.html Eleman/uygulama.html` (`uygulama.html` elle düzeltilmez).
- **Ölçü Tablosu düzeltmesi** (Ölçü sohbeti): `kaynak/olcu/src.html` eleman dalında düzeltilir, `python3 kaynak/olcu/derle.py`
  çalıştırılır (Eleman/olcu_tablosu_araci.html yenilenir). Masaüstündeki tek başına hali gerekirse depo dışına derlenir.
- **Yayın** (iş bilgisayarına gitsin): `Eleman/surum.json` (sürüm, tarih, kullanıcının göreceği Türkçe notlar) ve
  `Program.cs` AssemblyVersion artar, `eleman`'a itilir, sonra `git push origin eleman:main`. Releases'a `surum.yml` ekler.
- **Bakım**: dal silme ve sürüm başlığı `.github/workflows/bakim.yml` ile (workflow_dispatch; API:
  `POST repos/TheBurzzz/eleman/actions/workflows/bakim.yml/dispatches`). Git vekili dal silmeye ve depo ayarına izin vermiyor;
  varsayılan dalı yalnız kullanıcı değiştirebilir (şimdilik `eleman`).
- C# değişikliğinden sonra derleme denemesi (Linux, mono, Windows'taki csc.exe gibi C# 5): `KopruIcte.cs` yerine küçük bir taslak
  sınıfla `mcs -langversion:5` (Eleman sohbetinde `/home/claude/is/derle/derle.sh`).

## Son durum

- 2026-11-06 (Eleman sohbeti, öğleden sonra):
  - `eleman` dalı açıldı (main = v2.0.4'ten). main'e dokunulmadı.
  - Simgeler ve açılış ekranı Eleman; pencere, uyarı, bildirim, görev yöneticisi adı "Eleman". Ölçü sunucu bölümü (`/olcu/...`) eklendi.
  - Eleman kabuğu (`uygulama.html`): Apple tarzı ana sayfa (selam, iki uygulama kartı, canlı durum), üst çubukta
    Asorti Aracı / Ölçü Tablosu düğmeleri, Ölçü için Asorti'ninkiyle aynı sekmeler, ⚙ menüsünde açık uygulamanın bölümü,
    Ölçü'nün ortak hafıza durumu üst çubukta. Açılışta ana sayfa gelir.
  - Ölçü Tablosu: yeşil tema, tablo simgesi, tema düğmesi kaldırıldı, Eleman içinde başlıksız, sekme başına ayrı taslak,
    müşteri şablonları `/olcu/sablonlar`'dan (kurulumdaki gizli `olcu_sablonlar.json`).
  - Önizleme kullanıcının bilgisayarında: `Masaüstü\Ölçü Tablosu Aracı\exe-hazirlik\eleman_onizleme\Eleman.html`
    (sadece görünüş; sunucu yok, yazılanlar gerçek programlara karışmaz).
  - İş bilgisayarının kopyası Eleman sohbetinin çalışma alanında: `/home/claude/eleman-arsiv`
    (`is_pc_C` = C:\AsortiAraci ayarlar/kayıtlar/sayfalar, `is_pc_masaustu` = KESİM RAPORLARI + Ölçü Tablosu Aracı klasörü,
    `is_pc_ornekler` = son ölçü tabloları, müşteri logoları, bir tarama örneği). Gizli: GitHub'a konmaz.

- 2026-11-06 akşam: **Eleman 3.0.0** (yalnız `eleman` dalında). Kurulum sihirbazı Eleman adıyla; GitHub ZIP klasör adından
  (`asorti-araci-eleman`) güncelleme dalı `eleman` yazılır, böylece evdeki deneme kurulumu `eleman` dalındaki düzeltmeleri alır.
  Kullanıcıya evde denemesi için `Eleman_kurulum.zip` verildi (içinde anahtar.txt; GitHub'da yok).
  Linux'ta uçtan uca denendi: gerçek C# sunucusu (mono) + kabuk + Ölçü: şablonlar gizli depodan indi, PDF okundu (10 sn),
  Excel'e kaydedildi, Asorti sayfası açıldı. Tek 404: `kopru/alanlar.json` (Gerber'siz kurulumda zaten yok, eskiden de böyle).
  Deneme araçları (Eleman sohbeti): `/home/claude/is/e2e/e2e.py`, `/home/claude/is/derle/derle.sh`, `/home/claude/is/parse.ps1` (pwsh 7.4).

- 2026-11-06 gece: **Eleman 3.0.1** (yalnız `eleman` dalı; kullanıcının evdeki kurulumu bu daldan güncellenir).
  Kullanıcının kısaltmaları: **AA** = Asorti Aracı, **ÖT** = Ölçü Tablosu.
  - Simge: kurulumdaki derleme (sistem/ortak.ps1) de eleman.ico kullanır; kısayollar (Kisayol.cs) eleman.ico'ya bağlanır,
    güncellenen kurulumlarda masaüstü / Başlat'taki "Asorti Araci.lnk" adı "Eleman.lnk" olur (görev çubuğuna sabitlenmişe dokunulmaz).
  - Açılış (X / Twitter iOS gibi): yerel açılış ekranı (Acilis.cs) düz zemin + ortada 104 px simge (sistem/acilis/orta_*.png
    yalnız simge). Sayfa da aynı görüntüyle açılır (#acilis); yerel ekran kalkınca Eleman sayfaya {t:"acilis"} yollar, simge
    küçülüp büyür, içi pencere olur ve uygulama görünür (tuval, ~0,9 sn). Aynı oturumda yenilemede oynamaz (sessionStorage).
  - Üst çubuk: AA / ÖT düğmeleri kalktı; sol üstteki Eleman simgesi menü açar (Ana sayfa, AA, ÖT). Etiket: "Eleman › Asorti Aracı".
  - Sayfa kendiliğinden açılmaz; boşken AA / ÖT boş ekranı (Yeni sayfa düğmesi). Ana sayfada sürüm yazmaz (yalnız ⚙).
  - Hız: sayfalar ilk açılınca yüklenir; AA'da en çok 4, ÖT'de 3 sayfa canlı, gerisi uyur (AA: yalnız boş ya da tablosu
    kaydedilmiş sayfa uyur; Gerber işi süren uyumaz. ÖT: okuma / kayıt sürerken uyumaz, uyumadan önce taslakYaz(true)).
    Sekme adları kalıcı (S.ad / SO.ad).
  - ÖT: müşteri döşemeleri (şablondaki logo + ad; sıra Sorgenfri, Lykka, Deerberg, Heiter, sonra alfabetik), başlıkta
    "＋ Müşteri ekle" ve "Sıfırla" (AA'daki gibi; Kaydet'teki "Yeni tablo" kalktı), Tara'da bağlı tarayıcının adı ya da
    "Tarayıcı bağlı değil", "Kağıdı yanda aç": taranan kağıt solda, seçili satırın kağıttaki yeri işaretli (satırlarda yer:{pg,a,b}),
    "✓ Onayla" düğmesi. Eleman sekmesinde tablo kaydedilse de sekmede durur, program açılınca sessizce geri gelir.

- 2026-11-06 gece: **Eleman 3.0.2** (yalnız `eleman`): anahtarlı güncelleme (yukarıdaki "Gizli depo" 1. aşama),
  güncelleme yedeğine `olcu_tablosu_araci.html` de girdi, kök `.gitignore`. Linux'ta mono ile denendi: anahtarla surum.json,
  zipball (302 → codeload, 10 MB, `TheBurzzz-asorti-araci-<sha>/AsortiAraci/...`). (Gizli depo planı sonra iptal edildi.)
- 2026-11-06 gece: **Eleman 3.0.3** (yalnız `eleman`): salt-okur hafıza (yukarıda "Anahtarlar"). Kullanıcının `eleman-okuma`
  anahtarı `OKUMA`'da karışık yazılı (düz hâli yalnız Eleman sohbetinin çalışma alanında, depoda yok). Okuma izni
  raw.githubusercontent ile doğrulandı (sahte anahtar 404, bu anahtar 200); yazma izni yokluğu token sayfasının ekran görüntüsüyle
  doğrulandı: yalnız `TheBurzzz/eleman-hafiza`, Contents Read-only, Metadata Read-only, süresiz. (Buradan api.github.com /
  github.com denemesi olmaz: vekil kendi kimliğini koyuyor.) Anahtar değişecekse: önce yeni salt-okur token → `OKUMA`
  yeniden karışık yazılır → yeni sürüm yayınlanır → kurulumlar güncellenince eskisi silinir (önce silinirse yeni kurulumlar müşterisiz kalır). mono + Playwright (GitHub taklit) ile denendi:
  okuma anahtarıyla yalnız GET (hafiza.json, sablonlar), PUT/DELETE hiç yok; yerel öğrenilen, eklenen ve silinen
  müşteri yerelde kalıyor; `anahtar.txt` varken `salt:false`, okur-yazar anahtar.

- 2026-11-06 gece: **Eleman 3.0.4** (yalnız `eleman`), Ölçü Tablosu (kullanıcı Eleman sohbetinden istedi):
  - Logo: şablonlarda müşteri logosu F7:I10 kutusundan taşıyor (Lykka üst/alt, Strikkeby ve Story of Mine yanlar; Excel'de
    gölgeli beyaz kart olarak görünüyor). `buildXlsx` → `logoSigdir`: merkezi boş bir birleşik hücreye düşen resim o kutuya
    oranı korunarak, ortalanarak, %9 payla sığdırılır (oneCellAnchor). Şirket logosu (D2) ve nokta şekli dokunulmaz.
    Önizleme sütun pikselleri Excel'deki gibi (`xlPx`: (256w+18)/256*7; eskiden w*7+5). LibreOffice ve önizlemeyle 7 müşteri denendi.
  - Beden dizisi: `SZ={list,sample,base,elle}`; "Beden dizisi" menüsü (şablondaki, hazır harf/numara dizileri, son elle
    yazılanlar `ota_beden_son`, elle yaz). Dizideki bir bedene basınca kağıttan araya giren beden geri alınır. Müşteri
    değişince / boş tabloda şablondakine döner; taramadan sonra elle seçilen dizi kalır. Az bedenli dizide yazdırma alanı
    şablonun genişliğinde kalır (Development başlığı kesilmesin).

- 2026-11-06 gece: **Eleman 3.0.5** (yalnız `eleman`): her kurulum ortak hafızaya yazar (yukarıda "Anahtarlar"), 403'te
  yalnız okumaya geçer, silinen / bozulan hafıza ve müşteriler geri yüklenir. Playwright + GitHub taklidiyle 6 durum denendi
  (yazabilen, 403, hafıza 404, hafıza küçülmüş, 3 müşteriden 2'si kayıp, 1'i silinmiş).

- 2026-11-06 gece: **Eleman 3.0.6** (yalnız `eleman`):
  - Açılış (kullanıcı: "daha efektli, logonun içine giriliyormuş gibi, ekrana çarpıyormuş gibi, saçma efekt yok"): simge
    vektör çizilir (`ADAM` = eleman.svg'deki çizgiler, kabuk_yap.py çıkarır). 300 ms geri çekilme (0,82), 640 ms dalış
    (üstel büyüme, yakınlaşma merkezi simge ortasından yüze kayar: FX,FY=32,28.6; yüzün içi ekranı p≈0,74'te kaplar),
    sarı dağılırken üst çubuk ve ana sayfa "çarpar" (1,18 → 0,982 → 1,004 → 1, 620 ms). Toplam ≈1,3 sn. Kareler denendi.
  - Ölçü Tablosu `logoIsle`: müşteri logosunun zemini kırpılır (saydam ya da düz renk; düz renk zemin yumuşak kenarla
    saydam yapılır), PNG olur (`xl/media/eleman_logoN.png`, eski resim kullanılmıyorsa silinir), gölgesi kaldırılır, kutuya
    %5 payla sığar. Desenli zemine (Deerberg) dokunulmaz. Müşteri döşemelerinde de kırpılmış logo. JSZip'e
    `createFolders:false` (çıktıda klasör girdisi kalmasın). LibreOffice ile 7 müşteri denendi.

- 2026-11-06 gece: **Eleman 3.0.7** (yalnız `eleman`): açık görünüm "Liquid Glass" (kullanıcı: "gece modu çok güzel, açık
  tema da hayran bıraksın"). Tek dosya: `AsortiAraci/sistem/eleman_cam.css`, yalnız `html:not([data-theme=dark])`:
  kabuk (`[data-uyg]`, kabuk_yap.py `</style></head>`'e <link> ekler), Asorti sayfaları (kabuk iframe'e `camEkle(f)` ile
  <link> ekler ve `data-eleman="asorti"` yapar; **asorti_araci.html değişmedi**), Ölçü (src.html `data-eleman="olcu"` + <link>).
  Değişkenler (--bg #e2e7f0, --glass daha saydam, --gb/--hi parlak kenar, --sh ince çizgi + derinlik, --btn cam kapsül,
  --bl1..5 canlı lekeler); bileşen kuralları `:where()` ile (sayfanın temel kuralı kadar özgül; .btn.pri, .btn.duz,
  button.exb gibi özellere dokunmaz). Kartlarda backdrop-filter yalnız saturate (blur yok: zemin yumuşak, kaydırmada pahalı).
  Yerel açılış zemini (Acilis.cs) açıkta 226,231,240 (yeni --bg ile aynı, geçişte renk atlamasın). Koyu görünüm piksel
  piksel aynı kaldı (karşılaştırıldı). **Asorti sohbeti:** açık temada renk değişkenlerini değiştirirse eleman_cam.css'e de bakmalı.

- 2026-11-07 gece: **Eleman 3.0.8** (yalnız `eleman`): ⚙'deki Asorti ayarlarının hiçbir düğmesi çalışmıyordu. Sebep:
  3.0.1'de boş ekran için eklenen `.bos{position:absolute;inset:0;z-index:3}` kuralı, Asorti'nin Excel klasörü yazısındaki
  `.yol.bos` (klasör seçilmemiş) ile çakıştı; yazı bütün menünün üstünü kapattı. Sınıf `.bosEkran` oldu.
  **Kural:** kabuk_yap.py'de main'in kullandığı sınıf adları (bos, ok, on, ad, x, ik, t, is, bekle, bad, tab ...) kapsamsız
  kullanılmaz; yeni sınıflara Eleman'a özgü ad verilir. Playwright ile ⚙'deki her düğmenin üstte olduğu ve çalıştığı denendi.

- 2026-11-07 gece: **Eleman 3.0.9** (yalnız `eleman`): sol üstteki uygulama değiştirici yeniden (kullanıcı: "fena değil ama çok
  daha güzel bir şey istiyorum"). `#uMenu`: Eleman simgesinden yayılan cam panel (468 px), üç büyük kutu `.uApp[data-u]`
  (58 px simge, ad, durum: `#mDH` selam, `#mDA`, `#mDO`; açık sayfası olanın simgesi altında nokta `.acik .uNokta`;
  seçili olan kendi renginde `--r`), kutular sırayla gelir, ok tuşlarıyla gezilir. Panel açılışta `body`'ye taşınır:
  `#bar`'ın backdrop-filter'ı içindeki elemanın arkayı bulanıklaştırmasını engelliyor (backdrop root). Bu yüzden ⚙ menüsünün
  açık temadaki `--pop`'u .92 (neredeyse opak). Kısayol: Ctrl+1/2/3 (`kisayol`, `kisayolBagla`: Asorti ve Ölçü iframe'lerinin
  belgesine de bağlanır). Playwright: ok tuşları + Enter, Ölçü ve Asorti içindeyken Ctrl+2/3/1 denendi.

- 2026-11-07 gece: **Eleman 3.1.0** (yalnız `eleman`): depo adı `eleman`'a hazırlık (yukarıda "Değişmeyecekler"): güncelleyici
  iki adı dener (mono'da denendi: eski adlı ayar, ayarsız, başka depo), eski PowerShell sunucusu da; kurulum yeni klasör adını
  tanır; README Eleman'ın vitrin sayfası oldu (simge, iki uygulama, kurulum, klasörler, dallar).

- 2026-11-07 gece: **README'de tanıtım videosu** (yalnız README, program ve sürüm aynı): 4:23 sesli tanıtım, demo verisiyle
  (gerçek müşteri belgesi yok). Video depoda değil, GitHub eki: `https://github.com/user-attachments/assets/767b67ba-…`
  (ücretsiz planda 10 MB sınırı: 720p, 24 fps; ilk 1,5 sn giriş kartı, oynatıcı siyah kare göstermesin). README düzenlenirken
  bu adres tek başına bir satırda, üstü altı boş kalmalı; `<video>` etiketine çevrilmemeli (giriş yapmış kullanıcıda oynamıyor).
  mp4 depoya konmamalı: güncelleyici dalın zip'ini indiriyor, her güncelleme büyür. Oynatıcı sessiz başlıyor, üstünde not var.

- 2026-11-09 sabah: **Eleman 3.2.0 main'e geçti, iş bilgisayarı Eleman oldu** (kullanıcı iş bilgisayarından: "programı tamamen
  elemana çevirelim … yeni güncelleme iş yerindeki pc'me güncelleme olarak gelsin").
  - 3.2.0: güncelleyici ve kurulum `Eleman/` ve `AsortiAraci/` klasör adlarını tanır; sürüm notları 2.0.4 kullanıcısına göre.
  - Önce iş bilgisayarının yedeği: `C:\AsortiAraci\yedek_asorti_2.0.4_eleman_oncesi` (program dosyaları, ayarlar, yerel kayıtlar,
    WebView2 Local Storage; 78 dosya, 3,3 MB). Güncelleyicinin kendi yedeği `C:\AsortiAraci\yedek`.
  - `git push origin eleman:main` (ileri sarma). Releases: **Eleman v3.2.0** (surum.yml, Latest); v2.0.4'ün başlığından
    "(iş bilgisayarındaki sürüm)" kalktı. `exe-deneme` silindi (bakim.yml). Dallar: `main`, `eleman`. Varsayılan dal `eleman`
    (vekil depo ayarına izin vermiyor; main yapmak isterse kullanıcı Settings'ten değiştirir).
  - İş bilgisayarı (KALIP1) kayıtları: 08:46:03 "guncellendi: 2.0.4 -> 3.2.0", 08:46:07 Windows csc ile derlendi, pencere
    yeniden açıldı, "kisayollar uygulamaya baglandi (6 kisayol)", kurulum klasöründeki `Asorti Araci.lnk` → `Eleman.lnk`.
    Asorti sayfaları (yerel_kayit.json) yerinde. Ölçü şablonları (olcu_sablonlar.json) Ölçü Tablosu ilk açılınca iner.
  - Aynı sabah kullanıcının onayıyla ("hemen değiştir") depodaki program klasörü `Eleman/` oldu (sürüm aynı, 3.2.0;
    iş bilgisayarı yeni yoldan sürümü görüyor). Evdeki eski kurulum artık güncellenemez, gerekirse yeniden kurulur.

- 2026-11-09 öğle (Asorti sohbeti): **Eleman 3.2.1**, çizgili üründe **Kol birimi ayrı** seçeneği (kullanıcı: "beden birimini
  ayrı, kol birimini ayrı şekilde yapabilme seçeneği olsun"; o sabah bir çizgili sayfada kol birimini aynı bedenlere ikinci grup
  olarak yazmıştı).
  - `asorti_araci.html`: kol grupları `bgk`, seçenek `bkOn` (grup işlevleri `bgAdd/bgDel/bgSet/bgTog(k, …)`, k=0 beden, 1 kol).
    Sayfa ve Excel kaydında `bgk` (kapalıyken null; eski kayıtlarda yok → seçenek kapalı açılır).
  - Excel / yazdırma: BEDEN BİRİMLERİ'nin altında (2 boş satır) aynı biçimde sarı KOL BİRİMLERİ. Kapalıyken çıktı eskisiyle aynı.
  - Seçenek açılınca kol tablosu boşsa: beden tablosunda aynı bedene ikinci kez yazılmış gruplar kola taşınır, yoksa beden
    grupları birimsiz kopyalanır ("Beden gruplarını kopyala" düğmesi de var). Çizgili tablo aynı bedenlerle yeniden
    hazırlanınca birimler kalır (önceden siliniyordu).
  - Playwright (kabuk içinden, açık ve koyu): seçenek, taşıma, kopyalama, kolda farklı gruplama, uyarılar, Excel (LibreOffice
    ile bakıldı), yazdırma, sayfa kaydı ve yeniden açılış, eski kayıt, çizgisiz iş. Sayfa hatası yok.

- 2026-11-09 öğleden sonra (Asorti sohbeti): **Eleman 3.2.2**, köprü düzeltmesi. Kullanıcı bir ek tabloyu (kontrast cep, tek
  pastal, OTOPASTAL'sız) Gerber'e gönderince "Durdu: Pastal olusmadi" çıktı, ama pastal oluşmuştu.
  - Sebep (`kopru.ps1` `PastalAdim`): `-not ($st | Where-Object …)`. Tek pastallı işte durum '' iken (engine.que'de henüz yok)
    filtre tek bir '' döndürür, PowerShell onu yanlış sayar → "hazır" → pastal kaydı yok → hata. v2.0.4'ün 6 sn önbelleğinden beri
    ilk bakış hep amsubmit'ten önce okunan metne düşüyor, yani tek pastallı işler (ek tablolar) her seferinde düşebilirdi;
    çok pastallı işte de ['ok',''] erken "hazır" sayılıyordu. 6 Kasım'daki tek pastallı iş v2.0.3'teydi (önbellek yok), sorun yoktu.
    Aynı '' Batch kapatılırken "bitmiş" sayıldığı için köprü Batch'i pastal yazılırken kapatmaya başlamıştı
    (pastal 13:00:19'da yazıldı, Batch 13:00:20'de zorla kapatıldı; pastal dosyası tam).
  - Düzeltme: sayıyla bakılır (`@(...).Count`). Batch "tamamlandı" deyip pastal kaydı henüz görünmüyorsa, Batch hata demediyse
    60 sn beklenir. Batch kapatılırken '' de bitmemiş sayılır (iş bittikten sonra en fazla 15 sn beklenir).
  - pwsh benzetimi (gerçek işlevler, sahte engine.que ve .ctl), eski ve yeni karşılaştırmalı: tek pastal Batch yazmadan /
    yazarken / "tamamlandı" ama kayıt yok / kayıt geldi; Batch başarısız; 60 sn'de gelmedi; çok pastallı; Batch'i kapatma.

- 2026-11-09 öğleden sonra (Asorti sohbeti): **Eleman 3.2.3**, Gerber adları 20 harf (kullanıcı: "gerberin harf sınırı var … ben
  urt-c yerine u-c veya ur-c yazıyordum … program izin vermezse sen de benim yaptığım gibi yap").
  - Sınır, iş bilgisayarındaki 166 Gerber klasörünün .ctl kayıtlarından: en uzun ad 20 harf (4343 pastal tam 20). Kullanıcının
    elle kısaltmaları da oradan görüldü: `…-UR1-2`, `…-UR-H`, `…-U1-E`, `…-U-H2`, `…-U4-TOF` (URT → UR → U, gerisi aynen).
  - `asorti_araci.html`: `gAd(model, no, harf)` URT → UR → U, U ile de sığmazsa model adının sonu kısalır; üretim pastalları,
    diğer kumaşlar, ek tablolar (`xAd`) ve Gerber'den boy / verim okuma hep bunu kullanır. Denemeler `gAsAd` (MODEL-AS01,
    sığmazsa model kısalır); köprü eski denemeleri silerken aynı kısaltmayla da arar. Kısaltınca iki ad aynı olursa gönderilmez,
    uyarı çıkar. Adı 20'ye sığanlar eskisiyle aynı (önceki işlerin adları değişmez).

- 2026-11-09 öğleden sonra (Asorti sohbeti, kullanıcının isteğiyle ÖT'de): **Eleman 3.2.4**, ÖT imzası AA gibi ("öt daki imzam
  aa gibi değil. aa gibi olsun"). `kaynak/olcu/src.html`: imza `<main>`'in içinden çıktı, `</main>`'den sonra `<footer class="imza">`
  (AA'daki gibi); `.gomulu body{display:flow-root}`, `.gomulu main{min-height:calc(100vh - 94px);margin-bottom:22px}`; yan yana
  görünümde imza da içerikle aynı sol boşluğu alır. `derle.py` ile yeniden üretildi (değişiklikten önce derleme, depodakiyle
  bayt bayt aynıydı). Kabuk içinde ölçüldü: iki uygulamada da imza pencerenin dibinden 20,8 px yukarıda (1920×1048 ve
  1366×700); ÖT'nin boş sayfadaki 14 px kaydırması kalktı; uzun sayfada imza içeriğin hemen altında.

- 2026-11-11 sabah (Eleman sohbeti): **Eleman 3.2.5**, genel tarama (kullanıcı: "uygulamayı güzelce tara, oluşabilecek hataları önle,
  ÖT'nin ortak hafızası için geliştirme düşün"). İş bilgisayarı kayıtlarında (9–11 Kasım) program hatası yok; Ölçü Tablosu iş
  bilgisayarındaki Eleman'da henüz hiç kullanılmamış (`olcu_klasorler` yok, ortak hafıza 3 Kasım'dan beri 4 kayıtta).
  - **Ortak hafıza eşitlemesi (`kaynak/olcu/src.html`, `syncNow`) yeniden**: birden çok Ölçü sekmesi aynı sırayı (`ota_bekleyen`)
    aynı anda gönderiyordu → kayıtlar iki-üç kez sayılıyordu (3 sekmede 9 kayıt uzakta 19 yerine 22–27 `saves`), sıradan
    `slice(q.length)` ile düşüldüğü için yeni kayıt kaybolabiliyordu. Şimdi: her deltanın `id`'si var; ortak hafıza son 400
    uygulananı `uyg`'da tutar (aynı delta bir kez işlenir: çift gönderim, cevabı kaybolan PUT); sıradan kimlikle düşülür
    (`siradanDus`); sekmeler `navigator.locks` ("ota-esitle", şablonlar "ota-sablon") ile sırayla eşitler; başka sekme son 20 sn'de
    eşitlediyse ve sıra boşsa GitHub'a gidilmez (`ota_son_esit` = {t,d}); `storage` olayıyla öbür sekmelerin hafızası ve göstergesi
    yenilenir. Eski sürümler (≤3.2.4) `uyg`'u bozmadan geri yazar. **"Sıradaki işler 3" bitti.**
  - `ghGet`: 1 MB'ı geçen dosyada GitHub `content`'i boş verir → eskiden boş hafıza sanılırdı; şimdi `git/blobs/<sha>`'dan okunur,
    bozuk JSON'da eşitleme durur (üstüne yazılmaz). Dosya hiç yoksa (404) ve bu bilgisayar bir şey biliyorsa geri yükler
    (eskiden yalnız 20+ kayıtta; azsa yerel hafıza da siliniyordu).
  - `learn`: ölçü aralığı (`typ`) yalnız bilinen aralığın 0,5–2 katı içindeki değerle genişler (virgülsüz 525 gibi bir değer
    bütün bilgisayarlarda "tuhaf değer" uyarısını kalıcı kapatıyordu). `sablonEsitle` başta `CUSTOM`'ı IndexedDB'den tazeler.
  - Kapatılan Ölçü sekmesinin taslağı sayfa kapanırken yeniden yazılıyordu (taranan kağıt görüntüleriyle IndexedDB'de kalıyordu):
    `sekmeKapandi()` (iframe `data-sil`) ile yazılmaz; kabuk açılışta sekmesi olmayan `taslak-*` kayıtlarını siler.
  - `Sunucu.cs` `Isle`: `Origin` başlığı varsa ve `http://localhost:<port>` değilse 403 (tarayıcıdaki başka bir site
    `/excel/kaydet`, `/kopru/gelen` gibi adreslere POST gönderemesin). Programın sayfası kendi adresini, betikler (hizli_ac.vbs,
    Program.cs) hiç göndermez. **Yeni bir sayfa / iframe eklenirse `sandbox` ya da `data:` adresi kullanılmamalı** (Origin `null` olur).
  - Ölçü ayarları: "Son eşitleme" satırı; Hakkında'da Eleman'ın sürümü.
  - Denemeler (Eleman sohbeti, `/home/claude/is/tarama`: gerçek C# sunucusu mono'da + Chrome + sha denetimli sahte GitHub):
    `t_yaris.py` (3 sekme yarışı, düzeltmeden önce 3/3 hatalı, sonra 4/4), `t_hafiza.py` (1 MB üstü, silinen dosya, kaybolan cevap,
    403, internetsiz, eski sıra, iki bilgisayar: 8/8), `t_sekme.py` (uyuma, kapatma, yeniden açılış, sahipsiz taslak: 5/5),
    `t_genel.py` (kağıt oku → kaydet → öğren), `t_asorti.py` (sipariş → hesap → Excel), `t_typ.py`. ESLint `no-undef`: temiz.
  - **Öneriler (yapılmadı, kullanıcıya sunuldu):** öğrenilenleri görme / silme ekranı (silme `sil` deltasıyla herkese yayılır);
    paylaşılan klasördeki elle yapılmış tablolardan toplu öğrenme (yalnız okuma); el yazısı modeli hâlâ yok (0 örnek toplandı);
    main'e çıkmadan önce deneme kanalı; ⚙'de Ölçü ayarları; ana sayfada son işler.

- 2026-11-11 akşam (Eleman sohbeti): **Eleman 3.3.0**, ortak hafıza için dört özellik (kullanıcı: "sırasıyla 1'den 4'e kadar yap").
  Hepsi `kaynak/olcu/src.html` + `SunucuOlcu.cs`; Ölçü ayarları → Ortak hafıza bölümünde.
  1. **Geçmiş tablolardan öğrenme** (yalnız Eleman'da). Klasör `kullanici.json` → `olcu_havuz` (öneri: masaüstündeki
     "Ortak Ölçü Tabloları", kullanıcı bir kez onaylar). Sunucu: `/olcu/havuz`, `/olcu/havuz-sec`, `/olcu/havuz-liste`,
     `/olcu/havuz-dosya` — **yalnız okur, o klasöre hiçbir şey yazmaz** (kural aynen geçerli). Sayfa: `havuzOku` (şablon düzeni:
     D sütununda MEASUREMENT başlığı; D=İngilizce, E=Türkçe, B:C birleşik=grup, F..L beden değerleri; başka düzen atlanır),
     sayımlar bu bilgisayarda IndexedDB `havuz_ist`; `havuzTuret`: sözlükte olmayan ad ≥2 tabloda → `extra`, Türkçesi boş olana
     ≥3 tabloda aynı Türkçe → `tr`, ≥3 tabloda geçen ölçünün %5–%95 aralığı → `typ`. Okunan dosyaların kısa özetleri ortak hafızada
     `hv` (başka bilgisayar yeniden saymaz), sayısı `havuz`. Açılıştan 15 sn sonra, 12 saatte bir, dosya başına 30 ms arayla.
     Not: programla gelen sözlük (`veri/dict.json`) zaten Kasım başındaki ~1200 tablodan çıkarılmıştı; bu özelliğin kazancı
     sonradan (elle, başka bilgisayarda) yapılan tabloların da sürekli katılması. Klasörde 2299 xlsx var (11 Kasım).
  2. **Öğrenilenleri gör / sil**: `ogrModal`; silme `sil:{alan:[anahtar]}` deltasıyla gider (`applyDelta` siler), herkesten kalkar.
  3. **Eski bir güne dön**: `geriModal`; GitHub commit listesi (`commits?path=`), seçilen hal `ghGet(ref)` ile okunur, yeni commit
     olarak yazılır, `donem` artar: öbür bilgisayarların "geri yükleme" koruması (yarıdan az kayıt) bu durumda çalışmaz, hale uyar.
     Gerçek GitHub'da buradan denenemedi (vekil); anahtarın Contents iznine commit listesi dahildir.
  4. **Kimin öğrettiği**: `/olcu/durum` → `pc` (bilgisayar adı); her delta `pc`, `t` taşır; hafızada `kay["tür:anahtar"]=[pc,t]`
     (n ad, t Türkçe, q kumaş, x yeni ölçü, y aralık) ve `kim[pc]={n,h,t}`; commit iletisi "hafıza güncellendi (N) · PC".
  - Denemeler: `/home/claude/is/tarama/t_yeni.py` (iş bilgisayarından kopyalanan 22 gerçek tabloyla; klasörün değişmediği özetle
    doğrulandı) 9/9; önceki denemeler yeniden: yarış 3/3, hafıza 8/8, sekme 5/5, genel akış.

- 2026-11-19 (Ölçü sohbeti): **Eleman 3.3.2**, kağıdın yönü. Kullanıcı ilk kez Eleman'dan taradı; kağıt camda ters duruyordu,
  hiçbir satır okunamadı (kullanıcı: "kağıdı tarayıcıya nasıl koyduğum fark etmesin … iki yönlü de koyabileyim").
  - `kaynak/olcu/src.html` → `yonBul`: sayfanın 1000 px'lik temizlenmiş kopyasının orta bandı (%25–75) 0°, 180°, 90°, 270° sırayla
    hızlıca okunur; güveni ≥55 olan sözlük kelimeleri sayılır (VOCAB + sözlükteki Türkçe kelimeler + başlık kelimeleri). Puanı ≥8 olan
    ilk yön seçilir (0° dışındaki yön 0°'ın 2 katı+2'yi de geçmeli); bantta yazı azsa (kısa tablo, boş sayfa) bütün sayfaya bakılır.
    Sonra eskisi gibi deskew → temizle → oku; "Kağıdı yanda aç" ve satırların kağıttaki yeri çevrilmiş sayfaya göre.
    Mesaj: "Kağıt ters/yan taranmıştı, düz çevrilip okundu."
  - `cevir`: tam sayılı `setTransform` (pikseller birebir taşınır; `rotate` + yarım piksel kayması görüntüyü bulanıklaştırıyordu).
  - Ölçek kısa kenara göre (tarama 2480, fotoğraf en az 2000, PDF `pdfCiz(...,true)`): yan duran sayfa küçülmesin; dik sayfada eskisiyle aynı.
  - Denemeler (Ölçü sohbeti, Playwright, gerçek tarama örnekleri): düz kağıtta 3.3.1 ile birebir aynı sonuç (FJONNA ve JELDRA PDF,
    tarayıcı JPEG'i, 2 telefon fotoğrafı); aynı kağıt 0°/90°/180°/270° → satırlar, değerler ve kağıttaki yerler birebir aynı (kayıpsız PNG);
    yanlış yönde puan 0–1, doğru yönde 27–102. Süre: düz kağıtta +~1,2 sn, ters kağıtta +~3 sn. Müşteri seçili akışta ters tarama
    `handleFile` ile: 25 satır, model ve beden doğru, sayfa hatası yok.

- 2026-11-19 öğlen (Ölçü sohbeti): **Eleman 3.3.3**, kullanıcının dört isteği (`kaynak/olcu/src.html` + `Eleman/uygulama.html`).
  - **Sekme ışığı / kapatma hatası** (kullanıcı: Excel'e kaydedip çıktı aldı, ışık yanıp sönüyor, sekmeyi kapatırken "şu an kağıt
    okuyor ya da kaydediyor" diyor). Neden: kaydet düğmesi `durumBildir()`'i `KAYDEDIYOR` hâlâ true iken çağırıyor, `finally`'de
    false olunca haber vermiyordu → kabuk `busy:true`'da kalıyordu (3.0'dan beri). Şimdi `finally`'de de `durumBildir()`.
    Yeni durum: `KAYDEDILDI` (Excel'e kaydedildi, sonra değişmedi) → mesajda `bitti`; kabukta Ölçü sekmesi `ik ok` (sabit yeşil,
    başlık "Excel'e kaydedildi"), `degisti()` / yeni kağıt / boş tablo / sıfırla sıfırlar; taslakta `kaydedildi` (uyuyan sekme
    açılınca yine yeşil). Asorti sekmelerine dokunulmadı.
  - **hood grubu**: `GROUPS0` + `GROUP_WORD.hood` (`\bHOOD\b|KAPUZE`). Taranan kağıtta `kapsonGrubu` HOOD geçen grupsuz satırları
    hood yapar (öğrenilen hafızada HOOD WIDTH/LENGTH grubu "" olduğu için sözlükten değil burada). Elle "—" yapılan satır `grpEl`:
    `autoGroup` onu gruba geri çekmez (pocket vb. için de geçerli; önceden tek satır gruptan çıkarılamıyordu).
  - **Onayla**: ölçü kutusuna yazınca (`mTyped`) satırın adı şüpheli (`chk`) değilse Onayla düğmesi hemen kalkar. Onayla zaten
    yazılan değeri bırakır (okunan değere dönmez); kullanıcı sordu: "7'yi silip 21 yazıp onaylarsam hangisini doğru sayar" → 21.
  - **El yazısı defterine sayı örnekleri**: taranan her satırda `mOku` (okunan değer) ve `mImg` (`sayiCrop`: M sütunu hücresi,
    sağa el yazısı payı, ~2–7 KB JPEG). Kayıtta elle yazılıp okunandan farklı olan değer → örnek `{tur:"sayi",img,m,oku,satir,en,tr,
    musteri,model}`; aynı satır yeniden değişirse aynı `satir` kimliğiyle yeniden gider (sonuncusu geçerli). `eleman-hafiza`
    `olcu-tablosu/el_yazisi/YYYY-MM/`. 19 Kasım öğlen defterde toplam 2 örnek vardı (ikisi de o sabah, Lykka INKGE, basılı satır).
  - Denemeler (Ölçü sohbeti, `scratchpad/e2e`: Eleman klasörü http'de + Playwright): gerçek kabukta sekme 3.3.2'de kaydettikten sonra
    `ik is` + kapatma uyarısı (hata yeniden üretildi), 3.3.3'te `ik ok`, değişince normal, kapatma sorunsuz. 3.3.2 ile 3.3.3 aynı
    kağıtları birebir aynı okuyor (Fjonna, Jeldra, 2 fotoğraf, ters Fjonna, yapay kapşonlu kağıt); tek fark HOOD satırlarının grubu.
    Onayla, defter örnekleri (düzeltilmeyen gitmez, ikinci kayıtta tekrar gitmez), hood boşaltma; Asorti sekmesi açılıyor; ESLint
    `no-undef` yalnız eski iki tanıdık (`showDirectoryPicker`, `asortiPencere`).

- 2026-11-19 öğleden sonra (Ölçü sohbeti): **Eleman 3.3.4**, yaka açıklığı kuralı (kullanıcı: "yaka açıklığı varsayılan olarak içten
  içe gelsin; ölçü tablosunda dikişten dikişe yazıyorsa varsayılan yapma, bir şey yazmıyorsa varsayılanı kullan").
  - `lookup(raw, trKagit)` → `yakaKurali`: sonuç düz `NECK WIDTH` ya da şablondaki iki hali (`(INSIDE)`, `(SEAM TO SEAM)`) ise
    kağıttaki satır yazısına (İngilizce + varsa Türkçe) bakılır: SEAM / SIEM / DİKİŞ / NAHT / SØM TIL SØM geçiyor ve INSIDE / İÇTEN /
    INNEN geçmiyorsa `NECK WIDTH (SEAM TO SEAM)`, yoksa `NECK WIDTH (INSIDE)`; ad ve Türkçe sözlükten (şablon yazımı).
    Öğrenilen hafıza "dikişten dikişe" dese bile kağıtta yazmıyorsa içten içe. "NECK WIDTH SEAM TO SEAM" (parantezsiz, sözlükte),
    "EDGE TO EDGE", "NECK WIDTH 1" gibi başka bir şey yazanlara dokunulmaz. NECK DROP'a dokunulmadı.
  - Elle yazılan düz NECK WIDTH (Türkçesi elle yazılmamışsa) da içten içe; satırdaki seçimden "—" seçilirse düz kalır.
  - Denemeler: 15 tek tek eşleştirme; yapay iki kağıt (düz → içten içe, seam to seam → aynen); Fjonna, Jeldra, wa1 (seam to seam)
    3.3.3 ile birebir aynı, wa0 (düz neck width) artık içten içe; başka fark yok. Yedi müşteri şablonunun hepsinde iki satır var:
    NECK WIDTH (INSIDE) ve NECK WIDTH (SEAM TO SEAM).

- 2026-11-19 öğleden sonra (Ölçü sohbeti): **Eleman 3.3.5**, Almanca ve yanlış yazılmış İngilizce. Kullanıcı: "müşterilerin çoğu
  Alman; bazen İngilizceyi yanlış yazıyorlar, bazen ölçü adlarını Almanca yazıyorlar (nadir). Her şeyi İngilizce düşünme."
  **Bundan sonra her yeni kural (anahtar kelime, eşleştirme) Almancayı da düşünmeli.**
  - `DE_PARCA` (Almanca parça → İngilizce: WEITE/BREITE→WIDTH, LÄNGE→LENGTH, HÖHE→HEIGHT, BRUST, TAILLE, HÜFTE, SAUM→BOTTOM, ÄRMEL,
    ARMLOCH, AUSSCHNITT→NECK, KAPUZE, TASCHE, BUND→WAISTBAND, VORNE/HINTEN, HM→CB, VM→CF, NAHT→SEAM …). `deBol`: bileşik kelimeyi
    parçalara böler (bağlayıcı S/N/EN/ES; AM, ZU gibi kısalar yalnız tek başına); `deBol(s,true)`: bileşikte bir parçanın bir harfi
    yanlış okunmuş olabilir (KAPUZENHTHE = KAPUZE+N+HÖHE). `almancaCevir`: kelime kelime çeviri; NECK DEPTH→NECK DROP,
    SHOULDER WIDTH→SHOULDER TO SHOULDER, TOTAL/FRONT LENGTH→FRONT LENGTH FROM HPS.
  - `lookup0`: öğrenilen → SYN → sözlük → **katlanmış eşleşme** (`katliBul`: Ä=A, Ö=O, Ü=U, ß=SS; kağıtta BANDLÄNGE, öğrenilen
    BANDLANGE) → **Almanca**: çeviri bilinen ölçüyse o (status `chk`, `orig` Almanca ad; benzerlikle eşleşme yalnız skor ≥ 0,9) →
    benzerlik → yeni (Almanca ad kalır, `ipucu` = İngilizcesi; Türkçe önerisi `glossHint(r.ipucu||r.en)`).
  - `fixTokens`: yer değiştirme de düzeltilir (WIDHT, LENTGH, HEGIHT, POISTION). Sözlükte hiç olmayan kelime: bir harf farkı ya da
    yer değiştirme; eski tablolarda da yanlış yazılmış kelime (WIDHT 7 kez): yalnız yer değiştirme ve doğrusu ≥ 50 ve ≥ 20 kat
    yaygınsa (CENTRE/CENTER kalır). Almanca kelimeye dokunulmaz (HOHE → HOLE olmasın).
  - Yön bulma: `yonKanon` (büyük harf, şapkasız: width → WIDTH, LÄNGE → LANGE, Türkçe harfler de) + Almanca kelimeler.
    Başlık: Messpunkt / Bezeichnung / Maße satırı beden etiketi; Artikel, Qualität/Material, Farbe, Lieferant, Größe etiketleri
    (yalnız İngilizcesi yoksa). Gruplar: TASCHE, KRAGEN, ABNÄHER, GÜRTEL, KAPUZE.
  - Denemeler (`scratchpad/e2e/t_almanca*.py`): 65 tek tek ad; sözlüğün 6168 yazılışı (her ad, küçük harfli, " I" ekli, harf
    yer değiştirmiş, harf eksik) 3.3.4 ile: sözlükteki hiçbir ad ve küçük harfli yazılış değişmedi, bulunan hiçbir şey kaybolmadı,
    farklar yalnız yanlış yazılışlarda (çoğu doğru ada bağlandı). 20 gerçek sayfa (Fjonna, Jeldra, 8 WhatsApp fotoğrafı, 2 PDF,
    çevrilmiş halleri) 3.3.4 ile birebir aynı, yönler aynı (doğru yönde puan biraz arttı, yanlış yönde 0–2). Yapay Almanca kağıt:
    3.3.4'te ters/yan konunca hiç okunmuyordu, şimdi 0/90/180'de aynı 16 satır, model, kumaş, beden 38.

- 2026-11-19 öğleden sonra (Ölçü sohbeti): **Eleman 3.3.6**, "Gönderiliyor…" takılması (kullanıcı: "benden ne bekliyor, bir
  butona mı basmamı istiyor? kendi otomatik yapsın"). Gönderme zaten kendiliğindendi ama takılıyordu: `learn()` örnek gönderimini
  (`syncSamples`) ve hafıza eşitlemesini (`syncNow`) aynı anda başlatıyordu; iki commit GitHub'da çakışınca (409) `syncSamples`
  duruyor, kalan örnekler 5 dakikalık eşitlemeye ya da pencere değişene kadar bekliyordu (eleman-hafiza'da görüldü: 13:56'daki
  kaydın örnekleri 13:59'da gitti). Sahte GitHub'la 3.3.5'te aynısı üretildi (1 örnek gitti, 10'u kaldı).
  - `syncSamples` artık `syncNow` ile aynı kilitte (`ota-esitle`): sekmeler ve iki iş sırayla yazar, çakışmaz.
  - **Defter dosyası biçimi değişti:** bir gönderimdeki örnekler tek dosyada `{ornekler:[...]}` (yol
    `el_yazisi/YYYY-MM/<t>_<id>_<adet>.json`, ~700 KB'a kadar). 3.3.6'dan önceki dosyalar tek örnek (doğrudan nesne). Defteri
    okuyacak araç ikisini de okumalı.
  - 409 / 5xx / internet: 4 kez artan beklemeyle yeniden dener, olmazsa 30 sn sonra yine. Sıra (IndexedDB `hw_kuyruk`) ekleme ve
    çıkarmada kilitli (`ota-hw-sira`): gönderim sürerken gelen yeni kaydın örnekleri silinmez (önceden silinebiliyordu).
  - `learn()`: önce öğrenilenler (`syncNow`), sonra örnekler (`addSamples(smp,true)` + `syncNow().finally(syncSamples)`).
  - Kabuk: Ölçü sekmesi kapanınca (`kapatO`) açık bir Ölçü sekmesine `{t:"esitle"}` gider, yarım kalan gönderimi o bitirir;
    hiç Ölçü sekmesi kalmadıysa gösterge "Gönderiliyor…"da kalmaz (sırada kalan Ölçü bir sonraki açılışta gider).
  - Göstergenin ipucu: "Öğrenilenler ortak hafızaya kendiliğinden gönderiliyor, birkaç saniye sürer. Senin bir şey yapmana gerek yok".
  - Denemeler (`scratchpad/e2e/t_gonder*.py`, `t_sekme2.py`, sahte GitHub: aynı anda iki yazma 409): kayıttan ~3 sn sonra
    "Ortak hafıza", 11 örnek tek dosyada, çakışma 0; iki anlık hata (500, bağlantı) + gönderim sürerken ikinci kayıt: 20 örneğin
    hepsi gitti; kaydedip sekmeyi 250 ms'de kapatınca: iki sekmede öteki bitirdi, tek sekmede gösterge takılmadı. Sekme ışığı,
    Asorti sekmesi, ESLint aynı.

- 2026-11-20 sabah (Ölçü sohbeti): **Eleman 3.3.7**, en üst satır atlanıyordu (kullanıcı: "son 3-4 tabloda en üst satırı okumuyor,
  elle satır açıyorum"; Lykka designsheet, Inskai). Neden: ilk satırın sayısının hemen sağına tik atılmış ("61-|"); OCR "A1"
  okuyor, sayı sayılmadığı için `analyse` M sütununun başını (`topY`) ikinci sayıdan hesaplıyor, ilk satır tablonun dışında
  kalıyordu (kullanıcının ekran görüntüsündeki kağıtla birebir üretildi; 3.3.6'da 16, 3.3.7'de 17 satır).
  - `analyse`: başlık (M sütunundaki beden etiketi ya da MEASUREMENTS / MESSPUNKT / DESCRIPTION) ile ilk okunan sayı arasında
    2,5 satır yüksekliğinden büyük boşluk varsa oraya, başlık yoksa bir satır aralığı yukarısına bakılır (`ekUst`); bu ek bölgedeki
    satır yalnız adı bilinen bir ölçüyse (`lookup0` ok) alınır, harfli okunan sayısı boşaltılır (`refineNums` hücreyi yalnız
    rakamla yeniden okur). Başlık ile ilk sayı arası olağansa hiçbir şey değişmez.
  - `BASLIK` / `basliksiz`: başlık kelimesiyle başlayan satır (ilk satırla tek satır okunmuş olabilir) başlıktan sonrası bilinen
    ölçüyse atılmaz.
  - `cleanNum`: sayının sağına yapışık tik "61-1" / "61~|" → 61 (emin değil, sarı).
  - Denemeler: 27 sayfa (gerçek + yapay + Almanca, çevrilmiş halleri) 3.3.6 ile birebir aynı; sahte kelimelerle `analyse`
    (tikli ilk sayı: 3.3.6 satırı atıyor, 3.3.7 alıyor; olağan tablo aynı).

- 2026-11-20 sabah (Asorti sohbeti): **Eleman 3.4.0**, kullanıcının iki isteği: (1) "alt-üst takım / çizgili gibi panolu işler
  için de bir seçenek … 1 panodan kaç beden, kaç kol çıkıyor yazacağım alan … asorti yapılmıyor ama ek asorti tabloları kalsın …
  seçenekler uygulamanın temasına uygun olsun"; (2) "astar ve kontrast cep … gerbere gönderip oto pastala gönderme seçeneği de
  olsun ama kendim yapma seçeneği de olsun".
  - Sipariş kartı: iki onay kutusu yerine "İş türü" tek seçim (Normal · Alt-üst takım · Çizgili ürün · Panolu iş), simgeli
    kartlar (`turUI`, `turSec`; `tkTog` / `cizTog` ona yönlenir). Yeni bayrak `ord.panolu`.
  - Asortisiz işler için `info.asz` (= çizgili || panolu): "asorti yok" anlamında `info.cizgili`'ye bakan her yer (ek tablolar
    sipariş adetlerinden, ana Gerber gönderimi kapalı, fazla kesim yok…) artık `info.asz`'a bakar; çizgiliye özgü birim
    tabloları `info.cizgili`'de kaldı.
  - Panolu iş: kart `#stp` (2. adım), gruplar `pnr` [{s:[beden], b:'1,5', k:'2'}], varsayılan tek grup bütün bedenler, kolda
    "= 4 kol" ipucu. Excel / yazdırma: sarı PANO BİRİMLERİ; BEDEN PANO BİRİMİ ve KOL PANO BİRİMİ ikişer sütun birleşik, değer
    "1 PANODAN 1,5 İŞ" (kullanıcının elle yaptığı tablolardaki gibi; iş bilgisayarındaki KESİM RAPORLARI'nda 2 örnek vardı).
    Kayıtta `pnr`; aynı bedenlerle yeniden hazırlayınca gruplar kalır.
  - Ek tablolar (yalnız astar ve kontrast cep, OTOPASTAL kuruluysa): "OTOPASTAL yerleştirsin / Kendim yerleştireceğim" (tür
    başına son seçim `localStorage asorti-xoto`). OTOPASTAL seçiliyse sipariş dosyasına `# kuyruksuz` yazılmaz, köprü ana
    pastallar gibi kuyruğa ekler (köprüde değişiklik yok). Bitince boy, BİRİM ve verim tabloya yazılır, bildirim çıkar;
    sürerken Durdur var. Kayıtta `xt[].oto`.
  - Çizgili / panolu işte Excel'deki sipariş tablosunun TOPLAM sütunu (n+2) artık genişlik alıyor (eskiden dar kalıyordu).
  - Denendi (Playwright, kabuk içinden, açık ve koyu): iş türü seçimi; panolu kart, Excel (LibreOffice ile bakıldı), yazdırma,
    sayfa kaydı, yeniden hazırlama, türler arası geçiş, eski kayıt; kontrast cep OTOPASTAL (sahte köprü sonucuyla: yerleşim,
    bitti, yerleşemedi, bildirim), astar kendim. Eski ve yeni sürümle aynı normal iş: Excel bayt bayt aynı; çizgili işte yalnız
    TOPLAM sütun genişliği farklı. Çizgili ve Gerber ad denemeleri yeniden geçti.

- 2026-11-20 öğlen (Asorti sohbeti): **Eleman 3.4.1**, panolu iş düzeltmeleri (kullanıcı: "1 panodan değil de mesela 2 panodan
  1 iş olacak … sadece 1 pano üzerinden düşünme"; "bedenin ayrı olsun kolun ayrı olsun, yan yana olunca kafa karıştırıyor …
  ön arka 1 adet kol şeklinde birim vericem … biraz özgür olmalı"; "alt üst takım hariç … tek satırla başlaması lazım").
  - Panolu iş artık çizgilideki "kol birimi ayrı" gibi: iki kutu (BEDEN PANO BİRİMİ, KOL PANO BİRİMİ), her birinin kendi beden
    grupları `pnB` / `pnK` [{s:[beden], b:'serbest yazı'}], varsayılan birer grup bütün bedenler. Birim serbest yazı; yalnız sayı
    yazılırsa "1 PANODAN … İŞ" olur (yanında önizleme), kolda "N PANODAN M İŞ" ise "= 2M kol" ipucu. Kol boşsa kol tablosu
    yazılmaz (uyarı yok); bedende birim yoksa uyarı.
  - Excel / yazdırma: 3.4.0'daki yan yana tek tablo kalktı; çizgilinin `birim` tablosu kullanılıyor (`metin:true` yazıyı olduğu
    gibi yazar, `gen:3` birimi 3 sütun birleşik yazar): sarı BEDEN PANO BİRİMİ | BİRİM, altında KOL PANO BİRİMİ | BİRİM.
    Çizgili çıktısı aynı (gen 1).
  - 3.4.0 kaydı (`pnr`, b/k ve bp/kp) açılınca pnB/pnK'ye çevrilir.
  - İş türü: takım dışındaki türe geçince boş satırlar silinir (yazılı satır kalır), tek satır kalır.
  - Denendi (Playwright, açık ve koyu): iki bölüm, serbest yazı, ipuçları, uyarılar, Excel (LibreOffice ile bakıldı), yazdırma,
    sayfa kaydı, yeniden hazırlama, 3.4.0 kaydı; satır sayısı her tür geçişinde. Eski / yeni normal iş Excel'i bayt bayt aynı,
    çizgili yalnız TOPLAM sütunu (3.4.0'dan beri); çizgili denemeleri yeniden geçti.

- 2026-11-20 öğleden sonra (Asorti sohbeti): **Eleman 3.4.2**, alt-üst takımda ÜST'ün asorti tablosu üstte, ALT'ınki altta
  (kullanıcı yazdırma görüntüsünü gönderdi: "üstün asorti tablosu üstte olsun, altınki de altta olsun").
  - Yalnız görünen sıra: `mainSira()` (takımda mainBlocks'un tersi) Excel (`outBlocks`), yazdırma ve ekrandaki sonuç tablosu
    (`show0`) için. `mainBlocks()` sırası (k: 0 ALT, 1 ÜST) aynı kaldı: Gerber kumaş eni (gW / gW2), model adları ve kayıtlı
    sayfalar ona bağlı. Yazdırmada FAZLA KESİM son ana tablodan (artık ALT) sonra; etiketler "ÜST = ALT", "ÜST ve ALT aynı asorti".
  - Denendi: takım işinde ekran, yazdırma, Excel sırası ÜST → ALT; normal iş Excel'i eskisiyle bayt bayt aynı.

- 2026-11-23 sabah (Asorti sohbeti): **Eleman 3.4.3**, sonuçtaki fazla kesim yüzdesi göze çarpan küçük özet şeridinde
  (kullanıcı: aceleyle çalışırken "siparişin %…" yazısını göremiyor, geçenlerde %5'i geçen asortiyi üretime vermiş; önce %5'te
  kırmızı istedi, sonra "%5'te değil, benim yazdığım sınırı geçince uyarsın" dedi).
  - `fkOz(s)`: show0 kutusunun başında Seçenek · Pastal · Fazla kesim (+N adet) · Siparişe oranı (büyük yüzde, sınır çizgisi
    olan küçük çubuk, "✓ %Y sınırı içinde" / "! %Y sınırını aşıyor" etiketi). Sınır = Ayarlar'daki Y ("Toplam fazla kesim en
    fazla %"); aşınca kutu kırmızı (3 kez yumuşak nabız, reduced-motion'da yok). Takım / süre doldu notları şeridin sağında.
  - Hesap Y'yi zaten aşmaz; aşım elle asorti değişikliğinde ya da hesaptan sonra Y düşürülünce olur. Y değişince `fkTazele()`
    şeridi, kontrol kutusunu ve uyarıyı hemen yeniler.
  - `actBtn()`: aşımda Yazdır / Excel düğmelerinin üstünde kırmızı bildirim (`#fkuy`, `bildir` görünümü). chk satırı
    "%X — %Y sınırını aşıyor" (eski "’ünü" eki her sayıya uymuyordu). Aşım 1 haneye yuvarlanınca sınıra eşit görünürse 2 hane.
  - Ek asorti tabloları, Excel ve yazdırma değişmedi.
  - Denendi (Playwright, açık ve koyu, geniş ve dar): sınır içinde, Y düşürülünce aşım, elle değişiklikle aşım, Y geri alınınca
    yeşile dönme, takım + süre doldu notları, ek tablo hesabı, yuvarlama.

- 2026-11-23 öğle (Asorti sohbeti): **Eleman 3.4.4**, özet şeridinde Pastal kutusu yerine "Sıradaki çözüm" düğmesi
  (kullanıcı: "pastal sayısını göstermesi gereksiz olmuş, onun yerine sıradaki çözüm butonu oraya gelebilir").
  - `fkOz`: Seçenek · [Sıradaki çözüm ›] · Fazla kesim · Siparişe oranı. `fkSira()` (hesap sürerken ya da tek çözümde bir şey
    yapmaz; tek çözümde düğme kapalı, "Bu ayarlarla başka çözüm bulunmadı"). Alttaki aynı düğme kaldırıldı; altta Baştan hesapla
    ve Katları yeniden hesapla kaldı. Düğme şeritte sabit yerde: art arda basınca oran yanında değişir.
  - Denendi (Playwright, açık ve koyu): iki tık 1/15 → 3/15, şerit güncel; tek çözümde kapalı; konsol hatası yok.
  - Not: kullanıcı tamamen Türkçe konuşulmasını istedi (3.4.3 sonrası bir yanıt yanlışlıkla İngilizce gitmişti).

- 2026-11-23 öğle (Asorti sohbeti): **Eleman 3.4.5**, sonuç tablosunun altındaki "Fazla — RENK: XS 0 · S 0 …" satırları küçük
  tabloya döndü (kullanıcı: temaya uygun, az yer kaplasın, abartılı olmasın ama bedenlerdeki fazlalıklar dikkat çeksin).
  - `fzTab(R,T,id)`: başlık satırı "Fazla kesim | bedenler", her renk bir satır; 0 soluk, artı mavi etiket (`.fzp`), Max + (T)
    sınırını aşan ya da eksik (−) kırmızı etiket (`.fzr`, title açıklamalı). Kart `.fzk` (inbg, ince kenar, 14px köşe,
    `width:fit-content`), beden sütunları eşit (46px), sayılar tabular.
  - `fzOz(s)` ana sonuç için (renk sırası mainSira: takımda ÜST üstte); ek asorti tablolarında da aynı tablo (T = tablonun
    Max +'sı; tek asortide bitir / ana asortinin katı modunda sınırsız). "Max +" (T) ve Y değişince `fkTazele()` tabloyu da yeniler.
  - chk satırı "+T’i aşıyor" yerine "bir bedende fazla kesim +T sınırını aşıyor" (ek her sayıya uymuyordu).
  - Denendi (Playwright, açık ve koyu): normal, T düşürülünce kırmızı, elle azaltınca eksik (−), takım (ÜST üstte), hızar ek
    tablosu; konsol hatası yok.

- 2026-11-23 öğle (Asorti sohbeti): **Eleman 3.4.6**, Gerber bölümündeki "Kumaş: ☑ K  H → ek asorti tablosundan  ☐ S" satırı
  sade etiketlere döndü (kullanıcı: "burayı da düzelt, abartılı olmasın, diğer istediklerim geçerli").
  - `gFabUI`: `.fbr` satırı, "Kumaş" etiketi; her kumaş tipi bir `.fb` hap: onay kutusu + harf + adı (`fbAd`, FABN'den: K ana kumaş,
    H hızar, S işaret kalıbı…; adı bilinmeyen harf yalnız harf). Seçili hap mavi tonlu (`:has(input:checked)`), ek asorti
    tablosundan gidenler (FABX) kesik çizgili, tıklanmaz: "H hızar → ek asorti tablosundan". Seçim mantığı, en kutusu aynı.
  - Denendi (Playwright, açık ve koyu): K kaldır/işaretle (info.gFab), S işaretleyince en kutusu, bilinmeyen harf.

- 2026-11-23 öğle (Asorti sohbeti): **Eleman 3.4.7**, kumaş satırı yalnız bilgi (kullanıcı: "işaret kalıbı için en yazmana gerek
  yok, onu ben kendim yapacağım; sadece model dosyasında hangi parçaların olduğunu oradan öğrenmek istiyorum").
  - `gFabUI`: "Modelde" + etiketler: K ana kumaş (mavi, "bu siparişle Gerber'e gider"), FABX harfleri kesik çizgili
    "→ ek asorti tablosundan", ötekiler (S işaret kalıbı, bilinmeyen harf) düz, "Gerber'e gönderilmez". Onay kutusu, en kutusu yok.
  - `gBuild`: ana kumaş her zaman gider; modeldeki öteki harfler için sipariş yazılmaz (eski kayıttaki `gFab` seçimi, ör. K kapalı
    ya da S açık, artık etkisiz; `gFab` kayıtta duruyor, okunmuyor). `gXfor` kalktı.
  - Denendi (Playwright, açık ve koyu): satır, kutu yok; eski seçim {K:false,S:true} ile gBuild yalnız K siparişleri, uyarı yok.

- 2026-11-23 öğleden sonra (Asorti sohbeti): **Eleman 3.5.0**, "En verimli asortiyi bul" yenilendi (kullanıcı: bazen 15 dk bekleyip
  6-7 metrelik pastal çıkıyor; metre sınırı olsun ama katı olmasın, toleransı ben belirlemeyeyim; asorti sayısı vermeden çalışsın,
  bazen verebilirim). Kullanıcının cevapları: önemli olan masa değil bir pastalın en fazla boyu; 3 m'nin toleransı yüksek, 5 m'nin
  düşük olsun; 5 m az yapılıyor ama yapılıyor; 6,5 ve 7 m asla. Bekleme ~10 dk (takımda iki katı). Düğme Ayarlar'da, Hesapla'nın yanında.
  - Ayarlar: "Pastal boyu en fazla (m)" (`#L`, işle saklanır `set.L`, son kullanılan `localStorage asorti-boy`), "🔎 En verimli asortiyi
    bul" (`#araB`) ve panel (`#araP`): kumaş eni / yön (takımda iki model) ve müşteri klasörü (`aW`, `aW2`, `aY`, `aY2`, `aAr`, info'ya
    yazılır, `araEs` sonuçtaki Gerber kutularını da günceller), Başlat / Vazgeç, süre tahmini; iş sürerken gStHtml durumu, bitince Kapat.
    Gerber bölümündeki eski düğme kalktı. Hesapla eskisi gibi asorti sayısı ister.
  - Tolerans `araTol(L)`: oran %13 − (L−3)·%4, %3–%17 arası, 15–40 cm; 3 m → 3,39 · 3,5 → 3,89 · 4 → 4,36 · 5 → 5,25 m; `ARA_SERT` 6 m asla.
  - Akış: (1) ölçüm işi `_olc_` (MODEL-AS00, gereken her bedenden 1 adet, takımda iki model) → bir adedin boyu: ölçek s, beden başına
    büyüme %4 (`araR`); önbellek `gdb.models[m].olc` (anahtar: en # yön # kumaş # beden dizisi) ya da tablodaki PASTAL BOYU varsa atlanır;
    üretim pastalları ve denemeler bitince de öğrenilir (`araOgren`). (2) `araDeneme`: beden başına tahmini boy w, P = en çok
    min(6, (L+tol)/en kısa adet, Ayarlar'daki asorti sayısı); çözücüye `lw:{w,max}` (tahmini boyu L+tol'u aşan asorti hiç üretilmez),
    plus:1; `araAday`: en iyi çözüm + her adımda en az yeni asorti isteyen çözüm, en çok `ARA_BUT`=8 yeni asorti (ölçülmüş bedava);
    deneme işi `_ara_` (AS01…). (3) `gAraBitir`: R0 (ölçüm) + deneme sonuçları; toleransı aşan pastalı seçenek elenir; L'yi geçen
    pastal için verimden 1,5·(aşım/tolerans) puan düşülür (en çok 4); mesajda en uzun pastal, elenen sayısı, bir adedin boyu.
  - Kopya (deneme pastalı üretime) için kumaş harfi gBuild'dekiyle aynı (`araFab`); AS00 de MODEL-ASnn temizliğine giriyor (köprü değişmedi).
  - `show()` sonuç yokken bir şey çizmez (en verimli hesaplamadan başlayabildiği için). Sayfa yeniden açılınca süren iş panelde görünür.
  - Denendi (Playwright + sahte köprü, açık ve koyu): 2,5 m (ölçüm + 7 deneme, en uzun 2,43), önbellekle ölçümsüz, asorti sayısı 3,
    1,2 m (tolerans içi 1,27 seçildi), 6,5 yazınca 6 m, takım (2 ölçüm + 12 deneme), durdurma, Kapat / yeniden aç, Hesapla, Excel,
    kopya satırı (URT1=AS05…), önceki şerit ve fazla tablosu testleri.

- 2026-11-23 akşam (Asorti sohbeti): **Eleman 3.5.1**, "Pastal boyu en fazla (m)" yeni işte boş (kullanıcı: "varsayılan olarak 5 geldi,
  boş olmasını istiyorum"). 3.5.0'daki son kullanılan değeri hatırlama (`localStorage asorti-boy`) kalktı, anahtar açılışta silinir;
  kayıtlı iş açılınca o işin `set.L` değeri gelir. Denendi: yeni iş boş, kayıtlı iş 4,5, yeni sayfada anahtar yok.

- 2026-11-23 akşam (Asorti sohbeti): **Eleman 3.5.2**, `#L` kutusundaki "ör. 3,5" placeholder'ı kalktı (kullanıcı: "ör. 3 yazıyor, o da
  yazmasın, asorti sayısı gibi boş olsun"; dar kutuda "ör. 3" diye kesik görünüyordu).

- 2026-11-23 akşam (Asorti sohbeti): **Eleman 3.6.0**, müşteriye bölünen renk tıklamayla (kullanıcı: "RENK - MÜŞTERİ" yazmak yerine
  tıklayayım, kendisi toplasın, kesim raporunda eskisi gibi görünsün; her renk kendi içinde: mavi1 mavi2, yeşil1 yeşil2…).
  - Veri değişmedi: `ord.rows` düz kalır (RENK - MÜŞTERİ … RENK TOPLAM), Excel / kayıt / parse aynı. Form `grpla(R)` ile parse()'daki
    kuralla gruplar (TOPLAM satırından önceki, adı RENK ile başlayan satırlar), `grpSira()` satırları form sırasına getirir (dizinler
    rd() sonrasıyla aynı). `ngSatir()`: normal satır (× · + müşteri), renk başlığı `tr.gh` (ad `.gad`, TOPLAM etiketi, toplamlar `.gt`
    salt okunur, × grubu siler (onay), + müşteri ekler), müşteri satırı `tr.gc` (↳, ad; numara ise kutu boş, yer tutucu "müşteri n",
    `data-n`). `mBol` satırı gruba çevirir (adetler 1. müşteriye, 2. boş, imleç 2.'de), `mEkle`, `mSil` (tek müşteri kalırsa renk tek
    satıra döner), `gSil`. `rd()` grupları düzleştirir (boş ad → ilk boş numara), takımda kısım renk satırında, müşteriler aynı kısımda.
    `tt()` müşteri adedi yazılırken renk toplamını da günceller. Alttaki uzun açıklama kısaldı.
  - Denendi (Playwright, açık ve koyu): böl, 3. müşteri, sil → tek satır, grup sil, renk adı değişince müşteri adları, eski düz kayıt
    (araya başka renk girmiş) gruplu görünüm, takım, Tabloyu hazırla (renk toplamı ve parts), yazdırma, Excel satırları ve TOPLAM formülleri.

- 2026-11-24 (Asorti sohbeti): **Eleman 3.6.1**, bölünen renk kullanıcının gerçek kesim raporu düzeninde (kullanıcı: "bazen böyle de
  gelebiliyor ama senin yaptığın tablo buna uygun olmuyor"; elle hazırladığı raporda: RENK, RENK MÜŞTERİ (müşteri kırmızı), TOPLAM).
  - İç biçim aynı (`ord.rows`: X = ana sipariş, "X - EK" = diğer müşteri, "X TOPLAM"); Excel'e yazarken `raporDuzen(R)`: grup önü/arkası
    boş satır (24.75), üye satırı `setR` ile zengin metin (X + kırmızı EK, şablon yazı tipinden `rPr`), toplam satırı yalnız "TOPLAM"
    (kırmızı, ortalı, altı çizili `redC`). 9 satıra sığıyor ama son satır TOPLAM ise H=19 (ASORTİ ile arada boşluk kalsın).
  - Gruplama tek yerde: `grupBul(N,gevsek)` (boş satır grubu keser; "TOPLAM" tek başına ise üstündeki ortak önekli satırlar üye).
    parse(), loadForeign() (elle yapılmış rapor) ve form `grpla()` bunu kullanır; openSaved eski/yeni düzeni ayırt edip adetleri karşılaştırır.
  - Renk sayfasında A8 artık TOPLAM satırına bağlı formül değil rengin adı (gerçek dosyadaki gibi), adetler toplam satırından.
  - Form: + müşteri → 1. satır "ana sipariş" (boş ad), 2. satır müşteri adı; boş ad = ana sipariş, sonraki boşlar numara alır.
  - Denendi: form + Excel (LibreOffice çizimi), kullanıcının elle yaptığı rapor gruplu açılıyor (toplamlar doğru), kaydedilen dosya
    yanlış uyarısız açılıyor, adet değişince uyarıyor, normal sipariş çıktısı 3.6.0 ile parça parça aynı, t19/t20 eski senaryolar.

## Sıradaki işler
0. **Sürüm arşivi = GitHub Releases.** 32 sürüm (ilk-deneme, v1.0.0–v1.1.22, v2.0.0–v2.0.4) bir kerelik GitHub Actions işiyle
   taşındı, `surum-v*`, `arsiv`, `surum-test` dalları silindi (dallar: eleman, main, exe-deneme). Bu oturumlardan etiket ve
   Release oluşturulamıyor (git vekili etiket itmeye 403, API Release yazmaya izin vermiyor); işi Actions yapar:
   `.github/workflows/surum.yml` main'de `Eleman/surum.json` değişince `v<sürüm>` Release'ini kendisi ekler
   (9 Kasım 2026'dan beri çalışıyor: Eleman v3.2.0).
   Kurulum, Releases zip'inin klasör adındaki sürüm numarasını (eleman-1.1.22) dal sanmaz.
0. ✓ 9 Kasım 2026: depoda program klasörü `Eleman/` (3.2.0 güncelleyici ve kurulum iki adı da tanır). Kullanıcı
   "her şey tamamen Eleman olsun" dedi; bilgisayardaki kurulum klasörü `C:\AsortiAraci` ve `AsortiAraci.exe` adı yine aynı
   (Gerber bağlantısı, WebView2 profili; yukarıda "Değişmeyecekler"), görünen her yer Eleman.

1. ✓ Müşteri şablonları gizli `eleman-hafiza` deposunda: `olcu-tablosu/veri/sablonlar.json` (2026-11-06, 7 müşteri).
   Eleman ilk açılışta `anahtar.txt` ile oradan indirip `olcu_sablonlar.json` olarak saklar, 6 saatte bir arka planda tazeler
   (SunucuOlcu.cs: OlcuSablonIndir). Bu klasör çalışan Ölçü Tablosu'nun okuduğu `olcu-tablosu/sablonlar/` değildir, ona karışmaz.
   Claude'un GitHub uygulaması artık `eleman-hafiza`'ya da erişebiliyor.
2. ✓ Masaüstü kısayolunun adı ve simgesi "Eleman" (kurulum ve güncelleme).
3. ✓ (3.2.5) Ölçü: birden çok sekme açıkken eşitleme sırayla, kayıtlar kimlikli (çift sayım yok).
4. ⚙ menüsünde Ölçü'nün ayarları (şimdilik düğme Ölçü'nün kendi ayar penceresini açıyor).
5. ✓ 9 Kasım 2026: kullanıcı "programı tamamen Eleman'a çevirelim" dedi; 3.2.0 main'e geçti, iş bilgisayarı güncellemeyle Eleman'a geçer.
6. El yazısı okuma modeli (Eleman'ın ilk sürümünde olacak). Hâlâ yok: öğreneceği örnek yok. 19 Kasım 2026'da defterde 2 örnek;
   3.3.3'ten beri düzeltilen sayılar da giriyor. Kullanıcıya söylenen: ~300 örnek birikince ilk okuyucu kurulur (Tesseract'ı
   defterdeki satır/hücre görüntüleriyle ince ayar ya da rakam için küçük model; sözlük ve tipik ölçü aralığıyla birlikte),
   sonra örnek arttıkça iyileşir. Sayıyı `eleman-hafiza` → `olcu-tablosu/el_yazisi/` altından say.
