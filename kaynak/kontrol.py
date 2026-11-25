# Eleman - yayından önce denetim (main'e itmeden önce çalıştır):  python3 kaynak/kontrol.py
#
# Üç sohbet (Asorti, Ölçü, Eleman) aynı depoya yazıyor. İki dosya elle değil, kaynağından üretilir:
#   Eleman/uygulama.html           <- kaynak/eleman/asorti_kabugu.html + kaynak/eleman/kabuk_yap.py
#   Eleman/olcu_tablosu_araci.html <- kaynak/olcu/src.html + kaynak/olcu/derle.py
# Üretilen dosya elle düzeltilirse, bir sonraki üretimde o düzeltme sessizce kaybolur (Kasım 2026'da iki kez oldu:
# Ölçü sekmesinin ışığı / "Gönderiliyor…" düzeltmesi yalnız uygulama.html'de, kaldırılan bir açıklama yalnız
# olcu_tablosu_araci.html'de kalmıştı). Bu betik ikisini yeniden üretip depodakiyle karşılaştırır, sürüm numaralarına
# ve sayfaların JavaScript'ine de bakar. Hiçbir dosyayı değiştirmez.
import json, os, re, shutil, subprocess, sys, tempfile

KOK = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
PROG = os.path.join(KOK, "Eleman") if os.path.isdir(os.path.join(KOK, "Eleman")) else os.path.join(KOK, "AsortiAraci")
hata = []


def uret(betik, args):
    r = subprocess.run([sys.executable, os.path.join(KOK, betik)] + args, cwd=KOK, capture_output=True, text=True)
    if r.returncode != 0:
        hata.append(betik + " çalışmadı:\n" + (r.stderr or r.stdout)[-800:])
        return False
    return True


def ayni(a, b, ad, nasil):
    if not os.path.exists(a):
        return
    if open(a, "rb").read() != open(b, "rb").read():
        hata.append(ad + " kaynağından üretilenle aynı değil. Üretilen dosya elle değiştirilmiş olabilir: değişikliği " + nasil
                    + " içine taşı, sonra yeniden üret (yoksa bir sonraki üretimde kaybolur).")


tmp = tempfile.mkdtemp(prefix="eleman_kontrol_")
try:
    # 1) kabuk
    k = os.path.join(tmp, "uygulama.html")
    if uret(os.path.join("kaynak", "eleman", "kabuk_yap.py"), [os.path.join("kaynak", "eleman", "asorti_kabugu.html"), k]):
        ayni(k, os.path.join(PROG, "uygulama.html"), "Eleman/uygulama.html", "kaynak/eleman/kabuk_yap.py ya da asorti_kabugu.html")
    # 2) Ölçü Tablosu (anahtarsız, şablonsuz: depodaki hali)
    o = os.path.join(tmp, "olcu_tablosu_araci.html")
    if uret(os.path.join("kaynak", "olcu", "derle.py"), ["--cikti", o]):
        ayni(o, os.path.join(PROG, "olcu_tablosu_araci.html"), "Eleman/olcu_tablosu_araci.html", "kaynak/olcu/src.html")
    # 3) sürüm: surum.json ile uygulamanın kendi sürümü aynı olmalı
    try:
        s = json.loads(open(os.path.join(PROG, "surum.json"), encoding="utf-8-sig").read())["surum"]
        p = open(os.path.join(PROG, "sistem", "uygulama", "Program.cs"), encoding="utf-8-sig").read()
        a = re.search(r'AssemblyVersion\("([0-9.]+)"\)', p).group(1)
        if a != s + ".0":
            hata.append("Sürüm uyuşmuyor: surum.json " + s + ", Program.cs AssemblyVersion " + a + " (ikisi birlikte artmalı).")
    except Exception as e:
        hata.append("Sürüm okunamadı: " + str(e))
    # 4) sayfaların JavaScript'i (node varsa): sözdizimi hatası olan sayfa iş bilgisayarında hiç açılmaz
    if shutil.which("node"):
        for ad in ("uygulama.html", "asorti_araci.html", "olcu_tablosu_araci.html"):
            js = "const s=require('fs').readFileSync(process.argv[1],'utf8');let n=0;for(const m of s.matchAll(/<script(?![^>]*src)[^>]*>([\\s\\S]*?)<\\/script>/g)){try{new Function(m[1])}catch(e){console.log(e.message);n++}}process.exit(n?1:0)"
            r = subprocess.run(["node", "-e", js, os.path.join(PROG, ad)], capture_output=True, text=True)
            if r.returncode != 0:
                hata.append(ad + " içinde JavaScript sözdizimi hatası: " + r.stdout.strip()[:300])
finally:
    shutil.rmtree(tmp, ignore_errors=True)

if hata:
    print("DENETİM GEÇMEDİ:\n- " + "\n- ".join(hata))
    sys.exit(1)
print("Denetim tamam: üretilen dosyalar kaynaklarıyla aynı, sürümler uyumlu, sayfalarda sözdizimi hatası yok.")
