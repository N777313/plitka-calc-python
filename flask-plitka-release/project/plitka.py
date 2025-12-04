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
        skolko_paddonov =  total_weight / self.massa_poddona_kg
        paddon_p1 =  (math.floor(skolko_paddonov)+1)*self.massa_poddona_kg			# paddon + 1
        paddon_m1 =  (math.floor(skolko_paddonov)-1)*self.massa_poddona_kg                  # paddon - 1

        return {
            "m2_requested": need_m2,
            "m2_real": real_m2,
            "tiles_needed": tiles_needed,
            "total_weight": total_weight,
            "total_price": total_price,
            "kolichestvo_paddonov_nado": skolko_paddonov,
            "paddon_p1": paddon_p1,
            "paddon_m1": paddon_m1,
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
