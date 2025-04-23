import discord #Discord API ile etkileşim kurmak için discord.py kütüphanesini ekler.
from discord.ext import commands #Bot komutlarını yönetmek için commands modülünü projeye dahil eder.
import sqlite3 #SQLite veritabanı ile etkileşim için sqlite3 modülünü ekler.

# Intents oluşturmazsak hata alıyoruz
intents = discord.Intents.default()  # Varsayılan intents'i oluşturur, yani botun en temel işlevselliği için gerekli izinler sağlanır.
intents.message_content = True  # Mesaj içeriğine erişim sağlamak için gerekli


# Botu intents ile başlatıyoruz
bot = commands.Bot(command_prefix="!", intents=intents)#Bu satır, botu başlatır ve botun komutlarını kullanarak etkileşime geçmek için ! komut öneki belirler.

# Veritabanı bağlantısı yapalım
def create_connection():
    conn = sqlite3.connect('tasks.db')
    return conn


# Komut: !add_task <description> "Bota görev ekleme komutu"
@bot.command(name='add_task')
async def add_task(ctx, *, description: str):
    conn = create_connection()
    cursor = conn.cursor()

    # Görevi veritabanına ekliyoruz
    cursor.execute("INSERT INTO tasks (description, is_completed) VALUES (?, ?)", (description, 0))
    conn.commit()
    conn.close()

    await ctx.send(f"Task added: {description}")


# Komut: !delete_task <task_id> "Bota görev ekleme komutu"
@bot.command(name='delete_task')
async def delete_task(ctx, task_id: int):
    conn = create_connection()
    cursor = conn.cursor()

    # Görevi veritabanından siliyoruz
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

    await ctx.send(f"Task with ID {task_id} has been deleted.")


# Komut: !show_tasks "Bota görev ekleme komutu"
@bot.command(name='show_tasks')
async def show_tasks(ctx):
    conn = create_connection()
    cursor = conn.cursor()

    # Tüm görevleri seçiyoruz
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    if tasks:
        tasks_list = "\n".join(
            [f"ID: {task[0]}, Description: {task[1]}, Completed: {'Yes' if task[2] == 1 else 'No'}" for task in tasks])
        await ctx.send(f"Tasks:\n{tasks_list}")
    else:
        await ctx.send("No tasks found.")


# Komut: !complete_task <task_id> Görevleri yapıldı olarak işaretleme komutu
@bot.command(name='complete_task')
async def complete_task(ctx, task_id: int):
    conn = create_connection()
    cursor = conn.cursor()

    # Görevi tamamlanmış olarak işaretliyoruz.
    cursor.execute("UPDATE tasks SET is_completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

    await ctx.send(f"Task with ID {task_id} has been marked as completed.")


# Aşağıdaki random gözüken şey botu çalıştırmak için gerekli token :))
bot.run('Size verdiğim token buraya yapıştırılacak.')