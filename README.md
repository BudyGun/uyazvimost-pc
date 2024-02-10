# Домашнее задание к занятию «Уязвимости и атаки на информационные системы» Константин Чумаков

### Инструкция по выполнению домашнего задания

1. Сделайте fork [репозитория c шаблоном решения](https://github.com/netology-code/sys-pattern-homework) к себе в Github и переименуйте его по названию или номеру занятия, например, https://github.com/имя-вашего-репозитория/gitlab-hw или https://github.com/имя-вашего-репозитория/8-03-hw).
2. Выполните клонирование этого репозитория к себе на ПК с помощью команды `git clone`.
3. Выполните домашнее задание и заполните у себя локально этот файл README.md:
   - впишите вверху название занятия и ваши фамилию и имя;
   - в каждом задании добавьте решение в требуемом виде: текст/код/скриншоты/ссылка;
   - для корректного добавления скриншотов воспользуйтесь инструкцией [«Как вставить скриншот в шаблон с решением»](https://github.com/netology-code/sys-pattern-homework/blob/main/screen-instruction.md);
   - при оформлении используйте возможности языка разметки md. Коротко об этом можно посмотреть в [инструкции по MarkDown](https://github.com/netology-code/sys-pattern-homework/blob/main/md-instruction.md).
4. После завершения работы над домашним заданием сделайте коммит (`git commit -m "comment"`) и отправьте его на Github (`git push origin`).
5. Для проверки домашнего задания преподавателем в личном кабинете прикрепите и отправьте ссылку на решение в виде md-файла в вашем Github.
6. Любые вопросы задавайте в чате учебной группы и/или в разделе «Вопросы по заданию» в личном кабинете.

Желаем успехов в выполнении домашнего задания.

------

### Задание 1

Скачайте и установите виртуальную машину Metasploitable: https://sourceforge.net/projects/metasploitable/.

Это типовая ОС для экспериментов в области информационной безопасности, с которой следует начать при анализе уязвимостей.

Просканируйте эту виртуальную машину, используя **nmap**.

Попробуйте найти уязвимости, которым подвержена эта виртуальная машина.

Сами уязвимости можно поискать на сайте https://www.exploit-db.com/.

Для этого нужно в поиске ввести название сетевой службы, обнаруженной на атакуемой машине, и выбрать подходящие по версии уязвимости.

Ответьте на следующие вопросы:

- Какие сетевые службы в ней разрешены?
- Какие уязвимости были вами обнаружены? (список со ссылками: достаточно трёх уязвимостей)
  
*Приведите ответ в свободной форме.*     

### Решение 1   
При сканировании утилитой nmap были обнаружены сервисы:   
ftp, ssh, telnet, smtp, domain, http, rpcbind, netbios-ssn, microsoft-ds, exec, login, shell, rmiregistry, ingreslock, nfs, ccproxy-ftp, mysql, postgresql,vnc, x11, irc, ajp13   
Более подробно здесь с названиями сервисов:   
```
nmap -sV 192.168.107.130
```

![alt text](https://github.com/BudyGun/uyazvimost-pc/blob/main/images/sec3.png)

1) Спомощью брутфорс из базы скриптов ssh обнаружена правильная пара для доступа по ssh:  user:user      
```
 nmap -sV -p 22 192.168.107.130 --script ssh*     
```
![alt text](https://github.com/BudyGun/uyazvimost-pc/blob/main/images/sec10.png)   

Зашел на ВМ, посмотрел файлы:   
![alt text](https://github.com/BudyGun/uyazvimost-pc/blob/main/images/sec11.png)    

2) Такая же уязвимость по ftp, обнаружена пара user:user с помощью команды:   
```
 nmap -sV -p 21 192.168.107.130 --script ftp*     
```
![alt text](https://github.com/BudyGun/uyazvimost-pc/blob/main/images/sec12.png)    

3) обнаружены куки на сервере
```
nmap -sV -p 80 192.168.107.130 --script http-c*
```
![alt text](https://github.com/BudyGun/uyazvimost-pc/blob/main/images/sec30.png)   

### Задание 2

Проведите сканирование Metasploitable в режимах SYN, FIN, Xmas, UDP.

Запишите сеансы сканирования в Wireshark.

Ответьте на следующие вопросы:

- Чем отличаются эти режимы сканирования с точки зрения сетевого трафика?
- Как отвечает сервер?

*Приведите ответ в свободной форме.*




