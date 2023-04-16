import os

base = "django_car_selector/media/car_images"

obj = os.scandir(base)

dir_list = []
for entry in obj:
    if entry.is_file():
        if int(entry.name) >= 27:
            dir_list.append(
                [os.path.join(base, entry.name), os.path.join(base, str(int(entry.name) - 1)), int(entry.name)])

dir_list = sorted(dir_list, key=lambda student: student[2])

for _dir in dir_list:
    os.rename(_dir[0], _dir[1])
obj.close()


import os
base = "media/car_images"
for car in cars:
    try:
        obj = os.scandir(base+f"/{car.id}")
        for entry in obj:
                if entry.is_file():
                        CarImage.objects.create(image=os.path.join(f"car_images/{car.id}/", entry.name), car=car)
    except:
        pass