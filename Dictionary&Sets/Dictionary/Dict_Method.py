marks={
    "Yousuf":90,
    "Imu":80,
    "Kabila":70,
    0:"Liran"
}
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Yousuf":100, "Shimu":80})
print(marks)
print(marks.get("Kabila"))
print(marks.get(0))