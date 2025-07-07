document.addEventListener('DOMContentLoaded', () => {
  loadSlots();
});

document.getElementById('bookingForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const name = document.getElementById('name').value;
  const carNumber = document.getElementById('carNumber').value;
  const inTime = document.getElementById('inTime').value;
  const outTime = document.getElementById('outTime').value;

  const response = await fetch('/book-slot', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name, carNumber, inTime, outTime })
  });

  const result = await response.json();

  alert(result.message);
  loadSlots();
});

async function loadSlots() {
  const response = await fetch('/slots');
  const data = await response.json();

  const slotContainer = document.getElementById('slots');
  slotContainer.innerHTML = '';

  for (let i = 1; i <= 5; i++) {
    const slot = document.createElement('div');
    slot.classList.add('slot');

    const isBooked = data.some(d => d.slot === i);
    slot.classList.add(isBooked ? 'booked' : 'available');
    slot.innerHTML = `<strong>Slot ${i}</strong><br>${isBooked ? 'Booked' : 'Available'}`;

    slotContainer.appendChild(slot);
  }
}
