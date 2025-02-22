from flask import Flask, request, jsonify, render_template
from transformers import pipeline
from fuzzywuzzy import fuzz, process

app = Flask(__name__)

# Sohbet geçmişini saklamak için bir liste
sohbet_gecmisi = []

# Güncellenmiş cevapları saklamak için bir sözlük
guncellenmis_cevaplar = {}

# Türkçe dil modeli ile transformers pipeline oluştur
nlp = pipeline("fill-mask", model="dbmdz/bert-base-turkish-cased")

# Basit bir cevap fonksiyonu
def cevap_ver(soru):
    soru_lower = soru.lower()

    # Güncellenmiş cevapları kontrol et
    en_yakin_soru = process.extractOne(soru_lower, guncellenmis_cevaplar.keys(), scorer=fuzz.ratio)
    if en_yakin_soru:
        yakin_soru, yakinlik = en_yakin_soru
        if yakinlik > 80:  # %80 benzerlik eşiği
            return guncellenmis_cevaplar[yakin_soru]

    if "merhaba" in soru_lower:
        return "Merhaba! Size nasıl yardımcı olabilirim?"
    elif "nasılsın" in soru_lower:
        return "Ben bir yapay zeka botuyum, duygularım yok ama size yardımcı olabilirim!"
    elif "görüşürüz" in soru_lower:
        return "Görüşürüz! İyi günler!"
    elif "hava" in soru_lower:
        return "Hava durumu hakkında bilgi veremiyorum, ama dışarıya bakabilirsiniz!"
    elif "saat" in soru_lower:
        return "Şu anki saati öğrenmek için cihazınızın saatine bakabilirsiniz."
    elif "adın ne" in soru_lower:
        return "Ben bir yapay zeka sohbet botuyum."
    else:
        return "Üzgünüm, bu soruya cevap veremiyorum."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sor", methods=["POST"])
def sor():
    veri = request.get_json()
    soru = veri.get("soru")
    cevap = cevap_ver(soru)

    # Sohbet geçmişine ekle
    sohbet_gecmisi.append({"soru": soru, "cevap": cevap})

    return jsonify({"cevap": cevap})

@app.route("/gecmis", methods=["GET"])
def gecmis():
    return jsonify(sohbet_gecmisi)

@app.route("/egit", methods=["POST"])
def egit():
    veri = request.get_json()
    soru = veri.get("soru")
    cevap = veri.get("cevap")

    # Güncellenmiş cevapları sakla
    guncellenmis_cevaplar[soru.lower()] = cevap

    # Yeni soru-cevap çiftini sohbet geçmişine ekle
    sohbet_gecmisi.append({"soru": soru, "cevap": cevap})

    return jsonify({"mesaj": "Cevap başarıyla güncellendi!"})

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8000)