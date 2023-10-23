import pygal

line = pygal.Bar()

line.title = "Aholi statistika"

line.x_labels = ["Yanvar", "Iyun", "Noyabr"]

line.add("Vatikan", [1000, 990, 950])
line.add("Mali", [1500, 1490, 1550])
line.add("Peru", [2000, 2190, 2250])

line.render_in_browser()
