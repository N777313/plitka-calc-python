надо использовать этот код за основу
import math

from dataclasses import dataclass

@dataclass
class Plita_title:
    name: str
    sizemm: str
    klassbetona: str
    amount_poddon_m2: float
    massa_poddona_kg: int
    price_grey_kzt: int
    price_color_kzt: int


    # ---- 1. Площадь одной плитки ----
    def calc_area_m2(self):
        length_mm, width_mm, *_ = self.sizemm.split("*")
        return (float(length_mm) / 1000) * (float(width_mm) / 1000)

    # ---- 2. Количество плиток на поддон ----
    def calc_quantity_on_pallet(self):
        return self.amount_poddon_m2 / self.calc_area_m2()

    # ---- 3. Цена за 1 плитку ----
    def calc_price_per_tile(self, color="grey"):
        area_one = self.calc_area_m2()
        if color == "grey":
            return area_one * self.price_grey_kzt
        return area_one * self.price_color_kzt

    # ---- 4. Вес одной плитки ----
    def calc_weight_per_tile(self):
        return self.massa_poddona_kg / self.calc_quantity_on_pallet()

    # ---- 5. Стоимость поддона ----
    def calc_pallet_price(self, color="grey"):
        if color == "grey":
            return self.amount_poddon_m2 * self.price_grey_kzt
        return self.amount_poddon_m2 * self.price_color_kzt

    # ---- 6. Расчёт по запросу клиента (главный новый метод) ----
    def calc_order(self, need_m2, color="grey"):
        area_one = self.calc_area_m2()
        price_m2 = self.price_grey_kzt if color == "grey" else self.price_color_kzt

        # сколько штук нужно (округляем вверх)
        tiles_needed = math.ceil(need_m2 / area_one)

        # стоимость
        total_price = need_m2 * price_m2

        # вес
        weight_one = self.calc_weight_per_tile()
        total_weight = tiles_needed * weight_one

        # сколько м2 даёт точно такое число плит
        real_m2 = tiles_needed * area_one

        return {
            "m2_requested": need_m2,
            "m2_real": real_m2,
            "tiles_needed": tiles_needed,
            "total_price": total_price,
            "total_weight": total_weight,
            "color": color,
            "tile_name": self.name
        }

    # ---- 7. Красивый вывод заказа ----
    def print_order(self, order_dict):
        print(f"📦 Заказ плитки: {order_dict['tile_name']} ({order_dict['color']})")
        print(f"Запрошено м²: {order_dict['m2_requested']:.2f}")
        print(f"Реальные м² с округлением: {order_dict['m2_real']:.2f}")
        print(f"Количество плиток: {order_dict['tiles_needed']} шт")
        print(f"Общий вес: {order_dict['total_weight']:.2f} кг")
        print(f"Стоимость заказа: {order_dict['total_price']:.0f} ₸")
        print("-" * 40)



# -------------         Main            ----------------------------

Ptitle = [
    Plita_title("Арена", "90*75*60", "B22,5(M 300)", 7.2, 900, 7500, 9500),
    Plita_title("Артсити",  "477*167*60", "B22(M 300)",   10.92, 1446, 6000, 8500),
    Plita_title("Артсити",  "357*167*60", "B22(M 300)",   10.92, 1446, 6000, 8500),
    Plita_title("Артсити",  "197*167*60", "B22(M 300)",   10.92, 1446, 6000, 8500),
    Plita_title("Артсити",  "157*167*60", "B22(M 300)",   10.92, 1446, 6000, 8500),
    Plita_title("Артсити",  "437*207*60", "B22(M 300)",   10.92, 1446, 6000, 8500),
    Plita_title("Артсити",  "317*207*60", "B22(M 300)",   10.92, 1446, 6000, 8500),
    Plita_title("Артсити",  "237*207*60", "B22(M 300)",   10.92, 1446, 6000, 8500),
    Plita_title("Артсити",  "197*207*60", "B22(M 300)",   10.92, 1446, 6000, 8500)
]

 
и надо создать сайт на flask api или fast api на python

при запуске должен выйти сайт для рассчета
входные данные это
1) Сколько квадратуры нужны для клиента
2) нужен цвет серый или цветной

должна быть кноп рассчитать
и на выходе должны вот пример
📦 Заказ плитки: Арена (grey)
Запрошено м²: 20.00
Реальные м² с округлением: 20.00
Количество плиток: 2963 шт
Общий вес: 2500.03 кг
Стоимость заказа: 150000 ₸



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# answer:
Ниже даю **полный готовый рабочий пример** сайта на **Flask**, который:

* использует **твои классы и данные** без изменений;
* даёт веб-страницу с формой:
  ✔ ввод м²
  ✔ выбор цвета (серый / цветной)
  ✔ выбор модели плитки
  ✔ кнопка «Рассчитать»
* выводит результат в том же красивом формате.

---

# ✅ **Готовый проект на Flask**

## 📁 Структура проекта

```
project/
│ app.py
│ plitka.py
│ templates/
│      index.html
```

---

# 📌 **1. plitka.py**

(твои данные + класс как есть, ничего менять не нужно)

```python
import math
from dataclasses import dataclass

@dataclass
class Plita_title:
    name: str
    sizemm: str
    klassbetona: str
    amount_poddon_m2: float
    massa_poddona_kg: int
    price_grey_kzt: int
    price_color_kzt: int

    def calc_area_m2(self):
        length_mm, width_mm, *_ = self.sizemm.split("*")
        return (float(length_mm) / 1000) * (float(width_mm) / 1000)

    def calc_quantity_on_pallet(self):
        return self.amount_poddon_m2 / self.calc_area_m2()

    def calc_price_per_tile(self, color="grey"):
        area_one = self.calc_area_m2()
        if color == "grey":
            return area_one * self.price_grey_kzt
        return area_one * self.price_color_kzt

    def calc_weight_per_tile(self):
        return self.massa_poddona_kg / self.calc_quantity_on_pallet()

    def calc_pallet_price(self, color="grey"):
        if color == "grey":
            return self.amount_poddon_m2 * self.price_grey_kzt
        return self.amount_poddon_m2 * self.price_color_kzt

    def calc_order(self, need_m2, color="grey"):
        area_one = self.calc_area_m2()
        price_m2 = self.price_grey_kzt if color == "grey" else self.price_color_kzt

        tiles_needed = math.ceil(need_m2 / area_one)
        total_price = need_m2 * price_m2
        weight_one = self.calc_weight_per_tile()
        total_weight = tiles_needed * weight_one
        real_m2 = tiles_needed * area_one

        return {
            "m2_requested": need_m2,
            "m2_real": real_m2,
            "tiles_needed": tiles_needed,
            "total_weight": total_weight,
            "total_price": total_price,
            "color": color,
            "tile_name": self.name
        }


Ptitle = [
    Plita_title("Арена", "90*75*60", "B22,5(M 300)", 7.2, 900, 7500, 9500),
    Plita_title("Артсити",  "477*167*60", "B22(M 300)", 10.92, 1446, 6000, 8500),
    Plita_title("Артсити",  "357*167*60", "B22(M 300)", 10.92, 1446, 6000, 8500),
    Plita_title("Артсити",  "197*167*60", "B22(M 300)", 10.92, 1446, 6000, 8500),
    Plita_title("Артсити",  "157*167*60", "B22(M 300)", 10.92, 1446, 6000, 8500),
    Plita_title("Артсити",  "437*207*60", "B22(M 300)", 10.92, 1446, 6000, 8500),
    Plita_title("Артсити",  "317*207*60", "B22(M 300)", 10.92, 1446, 6000, 8500),
    Plita_title("Артсити",  "237*207*60", "B22(M 300)", 10.92, 1446, 6000, 8500),
    Plita_title("Артсити",  "197*207*60", "B22(M 300)", 10.92, 1446, 6000, 8500)
]
```

---

# 📌 **2. app.py — Flask сайт**

```python
from flask import Flask, render_template, request
from plitka import Ptitle

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        need_m2 = float(request.form["need_m2"])
        color = request.form["color"]
        tile_index = int(request.form["tile_index"])

        tile = Ptitle[tile_index]
        result = tile.calc_order(need_m2, color)

    return render_template("index.html", Ptitle=Ptitle, result=result)


if __name__ == "__main__":
    app.run(debug=True)
```

---

# 📌 **3. templates/index.html**

Создай папку **templates** и файл `index.html`.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Калькулятор плитки</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        .card { background: #f0f0f0; padding: 20px; width: 400px; }
        .result { margin-top: 20px; padding: 20px; background: #e8ffe8; }
    </style>
</head>
<body>

<h2>Калькулятор плитки</h2>

<div class="card">
<form method="post">

    <label>Модель плитки:</label><br>
    <select name="tile_index">
        {% for t in Ptitle %}
            <option value="{{ loop.index0 }}">{{ t.name }} ({{ t.sizemm }})</option>
        {% endfor %}
    </select><br><br>

    <label>Нужная квадратура (м²):</label><br>
    <input type="number" step="0.01" name="need_m2" required><br><br>

    <label>Цвет:</label><br>
    <select name="color">
        <option value="grey">Серый</option>
        <option value="color">Цветной</option>
    </select><br><br>

    <button type="submit">Рассчитать</button>
</form>
</div>

{% if result %}
<div class="result">
    <pre>
📦 Заказ плитки: {{ result.tile_name }} ({{ result.color }})
Запрошено м²: {{ "%.2f"|format(result.m2_requested) }}
Реальные м² с округлением: {{ "%.2f"|format(result.m2_real) }}
Количество плиток: {{ result.tiles_needed }} шт
Общий вес: {{ "%.2f"|format(result.total_weight) }} кг
Стоимость заказа: {{ "%.0f"|format(result.total_price) }} ₸
    </pre>
</div>
{% endif %}

</body>
</html>
```

---

# 🚀 **Запуск**

В терминале:

```bash
pip install flask
python app.py
```

Открыть в браузере:

```
http://127.0.0.1:5000
```

---

# 🎉 Готово!

Если хочешь — могу сделать:

✅ FastAPI версию
✅ Добавить Bootstrap (красивый UI)
✅ Автоматический выбор модели
✅ API без интерфейса
✅ Docker контейнер

Хочешь улучшенную версию?

