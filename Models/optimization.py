"""
Optimization Model
-------------------------------------------------
Suggests optimal parking allocation 
based on vehicle type, size, and slot usage.
"""

import random
import logging

logging.basicConfig(level=logging.INFO)

class OptimizationModel:
    def __init__(self):
        self.parking_layout = {
            "small": list(range(1, 51)),
            "medium": list(range(51, 81)),
            "large": list(range(81, 101))
        }
        self.allocated_slots = {}
        logging.info("[INIT] Optimization model initialized with parking layout.")

    def check_availability(self, vehicle_type: str) -> bool:
        """
        Check if there is a free slot for the vehicle type.
        """
        available = len(self.parking_layout.get(vehicle_type, [])) > 0
        logging.debug(f"[CHECK] Availability for {vehicle_type}: {available}")
        return available

    def allocate_slot(self, vehicle_type: str) -> str:
        """
        Allocate a slot for the given vehicle type.
        """
        if not self.check_availability(vehicle_type):
            return "No available slot for this vehicle type."

        slot = self.parking_layout[vehicle_type].pop(0)
        self.allocated_slots[slot] = vehicle_type
        logging.info(f"[ALLOCATE] Vehicle={vehicle_type}, Slot={slot}")
        return f"Allocated Slot: {vehicle_type.upper()}-{slot}"

    def release_slot(self, slot_id: int):
        """
        Free up a previously allocated slot.
        """
        if slot_id not in self.allocated_slots:
            return f"Slot {slot_id} not found in allocation."

        vehicle_type = self.allocated_slots.pop(slot_id)
        self.parking_layout[vehicle_type].append(slot_id)
        logging.info(f"[RELEASE] Slot {slot_id} released.")
        return f"Slot {slot_id} released."

    def suggest_best_slot(self, vehicle_type: str) -> str:
        """
        Suggest a slot near entrance (fake heuristic).
        """
        if not self.check_availability(vehicle_type):
            return "No slots available."

        best_slot = min(self.parking_layout[vehicle_type])
        return f"Suggested Slot: {vehicle_type.upper()}-{best_slot}"

# Example usage
if __name__ == "__main__":
    optimizer = OptimizationModel()
    print(optimizer.allocate_slot("medium"))
    print(optimizer.suggest_best_slot("small"))
    print(optimizer.release_slot(52))
