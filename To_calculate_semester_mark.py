#to calculate semester mark

first_sem=int(input("Enter your first semester mark that you obtained:"))
total_in_sem1=int(input("Enter your first semester maximum mark:"))

second_sem=int(input("Enter your second semester mark that you obtained:"))
total_in_sem2=int(input("Enter your second semester maximum mark:"))

third_sem=int(input("Enter your third semester mark that you obtained:"))
total_in_sem3=int(input("Enter your third semester maximum mark:"))

fourth_sem=int(input("Enter your fourth semester mark that you obtained:"))
total_in_sem4=int(input("Enter your fourth semester maximum mark:"))

fifth_sem=int(input("Enter your fifth semester mark that you obtained:"))
total_in_sem5=int(input("Enter your fifth semester maximum mark:"))

sixth_sem=int(input("Enter your sixth semester mark that you obtained:"))
total_in_sem6=int(input("Enter your sixth semester maximum mark:"))

total_sem_marks=first_sem+second_sem+third_sem+fourth_sem+fifth_sem+sixth_sem
total_max_mark=total_in_sem1+total_in_sem2+total_in_sem3+total_in_sem4+total_in_sem5+total_in_sem6

og_total_sem_mark=total_max_mark//100

print(f"your total mark obtained:{total_sem_marks}")

total_percentage=total_sem_marks/og_total_sem_mark
print(f"your overall percentage:{total_percentage}%")

tamil=int(input("Enter your tamil that you obatained:"))
total_tamil_mark=int(input("Enter your tamil maximum mark:"))
english=int(input("Enter your english that you obatained:"))
total_english_mark=int(input("Enter your english maximum mark:"))

total_mark_in_tam_eng=tamil+english

total_tam_eng_max_mark=total_english_mark+total_tamil_mark

print(f"your mark in tamil & english:{total_mark_in_tam_eng}")

total_mark_obtain_without_t_e =total_sem_marks-total_mark_in_tam_eng
total_without_t_e_marks=total_max_mark-total_tam_eng_max_mark

total_t_e=total_without_t_e_marks//100
total_percentage_without_lang=total_mark_obtain_without_t_e/total_t_e

print(f"your semester percentage without tamil and english:{total_percentage_without_lang}%")

