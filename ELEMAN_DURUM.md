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
3. Ölçü: birden çok sekme açıkken ortak hafıza eşitlemesini tek sekme yapsın.
4. ⚙ menüsünde Ölçü'nün ayarları (şimdilik düğme Ölçü'nün kendi ayar penceresini açıyor).
5. ✓ 9 Kasım 2026: kullanıcı "programı tamamen Eleman'a çevirelim" dedi; 3.2.0 main'e geçti, iş bilgisayarı güncellemeyle Eleman'a geçer.
6. El yazısı okuma modeli (Eleman'ın ilk sürümünde olacak).
