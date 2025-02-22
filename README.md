# Basit Yapay Zeka Sohbet Botu

Bu proje, Flask ve Transformers kütüphanelerini kullanarak basit bir yapay zeka sohbet botu oluşturur. Bot, kullanıcı sorularına yanıt verebilir, sohbet geçmişini saklayabilir ve kullanıcı tarafından eğitilebilir.

## Özellikler

- Kullanıcı sorularına temel cevaplar verebilir.
- Belirli anahtar kelimeleri tanıyıp ilgili cevapları verebilir.
- Kullanıcı ile sohbet geçmişini saklayabilir.
- Kullanıcının botun cevaplarını eğitebilmesi.
- Web tabanlı bir arayüz ile kullanıcı etkileşimi sağlar.
- Yazım hatalarını düzeltebilir ve benzer kelimeleri tanıyabilir.

## Gereksinimler

- Python 3.9+
- Flask
- Transformers
- FuzzyWuzzy
- python-Levenshtein

## Kurulum

1. Gerekli kütüphaneleri yükleyin:

   ```bash
   pip install Flask transformers fuzzywuzzy python-Levenshtein
   ```
