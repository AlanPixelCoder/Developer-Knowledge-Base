# 33. Tips Calculator

**Spanish version:** [33 - Calculadora de Propinas.md](./33%20-%20Calculadora%20de%20Propinas.md)

**Course:** C++
**Topic:** Chapter 6 Recap & Multiple Functions
**Tags:** `#cpp` `#recap` `#functions` `#calculator`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

## Chapter 6 Recap

- The "Don't Repeat Yourself" (DRY) methodology.
- We have been using built-in functions all along.
- How to **define** and **call** a `void` function — the two-step process.
- Inputs with **parameters** and **arguments**.
- Outputs with the `return` keyword.

## Project

Three functions, three responsibilities: one collects input, one computes, one reports.

```cpp
#include <iostream>

// 1. Ask the user for a tip percentage
double tips_menu() {
  double percentage;
  std::cout << "--- Leave a tip? ---\n";
  std::cout << "[ 15% ]  [ 20% ]  [ 25% ]\n\n";
  std::cout << "Enter your tip percentage (e.g., 20): ";
  std::cin >> percentage;
  return percentage;
}

// 2. Compute the tip amount
double tips_calculator(double subtotal, double tip_percentage) {
  return subtotal * (tip_percentage / 100.0);
}

// 3. Split the bill across the party
void shared_bills_calculator(double total_bill, int party_size) {
  if (party_size > 0) {
    double per_person = total_bill / party_size;
    std::cout << "\n--- Shared Bill ---\n";
    std::cout << "Party Size: " << party_size << "\n";
    std::cout << "Each person owes: $" << per_person << "\n";
  }
}

int main() {
  double meal_cost = 85.50;
  int party_size = 3;

  std::cout << "Subtotal: $" << meal_cost << "\n\n";

  double chosen_tip = tips_menu();
  double tip_amount = tips_calculator(meal_cost, chosen_tip);
  double final_total = meal_cost + tip_amount;

  std::cout << "\nTip Amount: $" << tip_amount << "\n";
  std::cout << "Total Bill: $" << final_total << "\n";

  shared_bills_calculator(final_total, party_size);
}
```

> [!NOTE]
> **The composition pattern**
> `main()` reads like a table of contents: gather, compute, report. Each function is small enough
> to test on its own. That is what DRY buys you once the program grows past a screen.

> [!WARNING]
> The `party_size > 0` guard prevents division by zero. Dividing a `double` by zero yields `inf`
> rather than crashing — which is arguably worse, because it propagates silently.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
