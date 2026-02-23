# vending_machine
# Digital Vending Machine Simulation

This project presents a **digital vending machine** designed and simulated using **Logisim-Evolution**. It models a real-world vending machine that:

- Accepts coins (5, 10, and 25 cents)
- Dispenses products when sufficient balance is reached (75 cents)
- Returns change for excess amount
- Tracks product inventory and sold-out status
- Implements reset and control logic for reliable operation

## Features
- Modular design with subcircuits for Bank, Activator, Dispenser, and Product management
- Coin accumulation using registers and adders
- Product selection and enable logic using comparators and multiplexers
- Stock management with counters and BCD display
- Automatic reset after each transaction

## Tools
- **Software:** Logisim-Evolution
- **Components:** Logic gates, adders, registers, counters, multiplexers, decoders, output pins

## How to Use
1. Open the project in Logisim-Evolution.
2. Insert coins using input buttons.
3. Select a product once the balance reaches 75 cents.
4. Product will dispense, and any extra amount will be returned as change.
5. Restock products using the Restock buttons if required.

## Files
- `MainCircuit.circ` – Main vending machine circuit
- `BankSubcircuit.circ` – Coin accumulation logic
- `ActivatorSubcircuit.circ` – Checks balance and computes change
- `DispenserSubcircuit.circ` – Handles product dispensing
- `ProductSubcircuits.circ` – Product stock management
- `README.md` – Project description and instructions

## Author
**Saira Zaman** – Project developed as part of Digital Logic Simulation coursework.

