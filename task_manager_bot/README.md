# Task Manager Bot

Bu projede, bir Discord botu kullanarak basit bir görev yöneticisi uygulaması yapılmaktadır. 
Kullanıcı, bot aracılığıyla görevler ekleyebilir, silebilir, tamamlayabilir ve mevcut görevleri görüntüleyebilir.

## Özellikler

- !add_task <description>**: Yeni bir görev ekler.
- !delete_task <task_id>**: Verilen `task_id` ile bir görevi siler.
- !show_tasks: Tüm görevleri listeler.
- !complete_task <task_id>**: Verilen `task_id` ile bir görevi tamamlar.

## Gereksinimler

Bu projeyi çalıştırabilmek için aşağıdaki gereksinimlere sahip olmanız gerekiyor:

- Python yüklenilmesi gerek.
- Discord botu için `discord.py` kütüphanesi
- SQLite veritabanı için `sqlite3` modülü 

## Kurulum

1. Bu projeyi  bilgisayarınıza indirip herhangi bir kod derleyicisiinde çalıştırabilirsiniz:
    

2.Gerekli bağımlılıkları yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

## Kullanım

1. Discord Botunu Çalıştırma:
   - `bot.py` dosyasını çalıştırarak botu başlatın:
     ```bash
     python bot.py
     ```

2. Botu Sunucuya Eklemek:
   
Aşağıdaki adımları izleyerek bu projedeki Discord botunu kendi sunucunda çalıştırabilirsiniz:

### 1. Discord Developer Portal’a Gidin

 [https://discord.com/developers/applications](https://discord.com/developers/applications)

### 2. Yeni Bir Uygulama (Bot) Oluşturun

- "New Application" butonuna tıklayın.
- Bir isim verin.
- Sol menüden "Bot" sekmesine geçin.
- "Add Bot" butonuna tıkla ve oluşturun.

### 3. Bot Token’ını Al ve Koda Ekle

- Bot sekmesinde "Reset Token" butonuna tıklayarak bir token oluşturun.
- Bu token’ı kopyalayın.
- Projede `bot.run("TOKEN")` satırına size verdiğim token’i yapıştırın.



### 4. Botu Sunucuna Davet Edin

- Sol menüden OAuth2 > URL Generator sekmesine girin.
- Aşağıdaki ayarları yapın:

**Scopes:**
- `bot`

**Bot Permissions (İzinler):**
- `Send Messages`
- `Read Message History`
- `View Channels`

- Sayfanın en altında oluşan URL’yi kopyalayın.
- Bu URL’yi tarayıcıda aç ve botu kendi Discord sunucuna davet edin.

### 5. Botu Başlatın

Proje dizininde terminali aç ve aşağıdaki komutu çalıştır:

bash
python bot.py

3. Botunuz sunucuda aktif olacak ve komutlara yanıt verecektir.

## Testler

Projede, temel işlevlerin doğru çalışıp çalışmadığını test etmek için Pytest kullanılmaktadır. Testleri çalıştırmak için:

1. Testleri çalıştırın:
    ```bash
    python run_tests.py
    ```

2. Tüm testlerin geçtiğinden emin olun. Çıktıdaki `4 passed` ifadesi başarıyı gösterir.


