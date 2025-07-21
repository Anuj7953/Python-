marks = {"Anuj":90, "Pawan":66}
# keys = names like Anuj, Pawan
# values = marks like 90, 66
print(marks.keys ())
print(marks.values())

marks.update({"Anuj": 67})
print(marks)

marks.get("Anuj")  # returns value for key "Anuj"
marks.pop("Pawan")  # removes key "Pawan" and its value