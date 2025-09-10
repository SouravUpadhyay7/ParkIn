"""
Dynamic Pricing Model
-------------------------------------------------
Adjusts parking charges dynamically 
based on demand, time, and traffic.
"""

import datetime
import random
import logging

logging.basicConfig(level=logging.INFO)

class DynamicPricingModel:
    def __init__(self, base_rate: float = 20.0):
        self.base_rate = base_rate
        self.logs = []
        logging.info(f"[INIT] Dynamic pricing initialized, base rate={base_rate}")

    def get_time_multiplier(self) -> float:
        """
        Different time slots have different multipliers.
        """
        hour = datetime.datetime.now().hour
        if 8 <= hour <= 20:  # Daytime
            return 1.5
        elif 20 < hour <= 23:  # Evening
            return 1.2
        else:  # Night
            return 0.8

    def get_demand_factor(self) -> float:
        """
        Fake demand factor between 0.5 to 2.0
        """
        return round(random.uniform(0.5, 2.0), 2)

    def calculate_price(self, duration_hours: int) -> float:
        """
        Compute dynamic price for given duration.
        """
        time_mult = self.get_time_multiplier()
        demand = self.get_demand_factor()
        final_price = round(self.base_rate * duration_hours * time_mult * demand, 2)

        log_entry = {
            "time": datetime.datetime.now(),
            "duration": duration_hours,
            "demand": demand,
            "price": final_price
        }
        self.logs.append(log_entry)
        logging.info(f"[PRICE] Calculated={final_price}, Demand={demand}, TimeMult={time_mult}")
        return final_price

    def get_logs(self):
        return self.logs

# Example usage
if __name__ == "__main__":
    pricing = DynamicPricingModel()
    for hrs in [1, 2, 5]:
        print("Price for", hrs, "hours:", pricing.calculate_price(hrs))
    print(pricing.get_logs())
