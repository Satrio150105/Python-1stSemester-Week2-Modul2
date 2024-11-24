students =  {
    'Shafira': {'Kalkulus 1': 85, 'Metode Statistika': 75},
    'Amanda': {'Kalkulus 1': 80, 'Metode Statistika': 90},
    'Aditya': {'Kalkulus 1': 75, 'Metode Statistika': 80},
    'Nedia': {'Kalkulus 1': 85, 'Metode Statistika': 80},
    'Widya': {'Kalkulus 1': 80, 'Metode Statistika': 85},
    'Hanif': {'Kalkulus 1': 75, 'Metode Statistika': 90},
    'Andi': {'Kalkulus 1': 80, 'Metode Statistika': 85},
    'Dhanar': {'Kalkulus 1': 80, 'Metode Statistika': 75},
    'Hikma': {'Kalkulus 1': 80, 'Metode Statistika': 75},
}

# 1. Shafira's average score across both subjects
shafira_avg = sum(students['Shafira'].values()) / 2
print(f"Rata-rata nilai Shafira pada kedua mata kuliah: {shafira_avg}")
# 2. Total score for Hanif and Andi across all subjects
hanif_total = sum(students['Hanif'].values())
andi_total = sum(students['Andi'].values())
hanif_andi_total = hanif_total + andi_total
print(f"Jumlah nilai Hanif dan Andi untuk semua mata kuliah: {hanif_andi_total}")
# 3. Average score for Widya, Dhanar, Hikma, and Nedia in each subject
students_group = ['Widya', 'Dhanar', 'Hikma', 'Nedia']
kalkulus_total = sum(students[student]['Kalkulus 1'] for student in students_group)
statistika_total = sum(students[student]['Metode Statistika'] for student in students_group)
kalkulus_avg = kalkulus_total / len(students_group)
statistika_avg = statistika_total / len(students_group)
print(f"Rata-rata nilai untuk Widya, Dhanar, Hikma, dan Nedia pada Kalkulus 1: {kalkulus_avg}")
print(f"Rata-rata nilai untuk Widya, Dhanar, Hikma, dan Nedia pada Metode Statistika: {statistika_avg}")
# 4. Average score in Kalkulus 1 for all students
kalkulus_avg_all = sum(students[student]['Kalkulus 1'] for student in students) / len(students)
print(f"Rata-rata nilai mata kuliah Kalkulus 1 untuk semua mahasiswa: {kalkulus_avg_all}")
# 5. Average score in Metode Statistika for all students
statistika_avg_all = sum(students[student]['Metode Statistika'] for student in students) / len(students)
print(f"Rata-rata nilai mata kuliah Metode Statistika untuk semua mahasiswa: {statistika_avg_all}")