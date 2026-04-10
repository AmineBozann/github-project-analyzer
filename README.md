# 🚀 GitHub Akıllı Proje Keşif ve Analiz Sistemi

## 📌 Proje Tanımı

Bu proje, GitHub üzerindeki milyonlarca açık kaynak proje arasından **en kaliteli ve en uygun projeleri bulmak** amacıyla geliştirilmiş akıllı bir analiz sistemidir.

Standart GitHub araması yalnızca yıldız sayısına odaklanırken, bu sistem çok kriterli analiz ve makine öğrenmesi kullanarak daha doğru sonuçlar sunar.

---

## 🎯 Projenin Amacı

- Yazılımcıların doğru projeyi daha hızlı bulmasını sağlamak
- Sadece popüler değil, **kaliteli projeleri önermek**
- GitHub projelerini analiz ederek akıllı sıralama yapmak

---

## ⚙️ Kullanılan Teknolojiler

- Python
- Flask
- Pandas
- Scikit-learn
- Matplotlib
- SQLite
- GitHub API

---

## 🧠 Makine Öğrenmesi

Projede **KMeans algoritması** kullanılmıştır.

Projeler 3 sınıfa ayrılır:

- 🟢 Yüksek kaliteli
- 🟡 Orta seviye
- 🔴 Düşük kalite

---

## 📊 Skorlama Sistemi

Projeler aşağıdaki kriterlere göre değerlendirilir:

- ⭐ Yıldız sayısı
- 🍴 Fork sayısı
- 📝 README varlığı
- 🔄 Güncellik
- 💬 Açıklama kalitesi
- 🔥 Aktivite (commit, issue, PR)

---

## 📌 Filtreleme Kuralları

- 0 < yıldız < 1000
- Son 1-2 yıl içinde güncellenmiş
- README bulunmalı
- Aktif commit geçmişi olmalı
- Issue/PR aktivitesi olmalı

---

## 🌐 Özellikler

- 🔍 Anahtar kelime ile proje arama
- 📊 Skor tablosu
- 📈 Grafiksel analiz
- 🔗 GitHub proje linkine yönlendirme
- 🤖 Makine öğrenmesi ile sınıflandırma

---

## 🛠️ Kurulum

```bash
git clone https://github.com/USERNAME/github-project-analyzer.git
cd github-project-analyzer
pip install -r requirements.txt
python app.py