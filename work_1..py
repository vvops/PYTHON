from multiprocessing.pool import job_counter

if __name__ == '__main__':
    print(2000)
    print(350.5)

if __name__ == '__main__':
    print(2000 + 350.5)

if __name__ == '__main__':
    print(--2000)


#ПЕРЕМЕНЫЕ

if __name__ == '__main__':
    payment_amaunt = 3000
    payment_amaunt = 4000

    print(payment_amaunt * 0.1)
    print(payment_amaunt)

if __name__ == '__main__':
    payment_amaunt = 3000
    payment_amaunt = payment_amaunt + 4000

    print(payment_amaunt * 0.1)
    print(payment_amaunt)

# ТИП ДАННЫХ СТРОКИ

if __name__ == '__main__':
    name = "ВОВА"
    print(name)

if __name__ == '__main__':
    name = "ВОВА"
    job = "devops"
    who_am_i = name + " " + job
    email = "vvops@.gmail.com"
    who_am_i = "меня зовут {}, я {}, пишиnе {}".format(name, job, email)
    print(who_am_i)

if __name__ == '__main__':
    name = "ВОВА"
    job = "devops"
    who_am_i = name + " " + job
    email = "vvops@.gmail.com"
    who_am_i = f"меня зовут {name:>10}, я {job}, пишиnе {email}"
    print(who_am_i)