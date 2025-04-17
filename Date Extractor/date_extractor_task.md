## Task 2: "Date Extractor"
📅 **Description**: The user enters a string containing a date in the format `"DD.MM.YYYY"`.

Your task:

- Extract and print the **day**, **month**, and **year** separately (as substrings).
- Swap the day and month to display the date in the format: `"MM.DD.YYYY"`.
- Print only the **last two digits** of the year.

📌 Use only **slicing** — no `split()`!

### What to validate in the date:
- The string must be **exactly 10 characters** long.
- The **3rd and 6th characters** must be dots (`.`).
- Day, month, and year must be **numbers**.
- Day must be **from 1 to 31**, month — **from 1 to 12**, and year must have **4 digits**.
