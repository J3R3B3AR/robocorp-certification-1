# Robot Order Automation - Robocorp Level I Certification

![Demo](robocorp-cert-i-demo.gif)

An entry-level RPA bot built with Robocorp and Python that automates the robot ordering workflow on [RobotSpareBin Industries](https://robotsparebinindustries.com/#/robot-order). This is the **Automation Certification Level I** project.

## What It Does

1. **Opens the order portal:** navigates to RobotSpareBin Industries and dismisses the modal
2. **Downloads order data:** fetches `orders.csv` directly from the site (no manual download)
3. **Processes each order:** for every row in the CSV:
- Selects the head, body, and leg parts
- Enters the shipping address
- Clicks Preview to render the assembled robot
- Clicks Order to submit
- Saves the HTML receipt as a PDF
- Returns to the form for the next order

## Project Structure

```
robocorp-cert-i/
├── tasks.py      # Main automation logic
├── conda.yaml    # Python environment definition (managed by RCC)
├── robot.yaml    # Task and environment configuration
└── output/
    └── receipts/ # PDF receipts generated at runtime
```

## Tech Stack

| Tool | Version |
|------|---------|
| Python | 3.12.8 |
| robocorp | 3.0.0 |
| robocorp-browser (Playwright) | 2.3.5 |
| rpaframework | 30.0.2 |
| RCC | via conda.yaml |

## Running the Bot

**VS Code (Robocorp extension):**
1. Open the project folder
2. Click the Robocorp panel → Run "Order robots"

**Command line:**
```bash
rcc run
```

RCC reads `conda.yaml` and builds an isolated Python environment automatically. No manual `pip install` needed.

## Key Implementation Notes

- Uses `robocorp-browser` (Playwright) for browser control with `slowmo=100`
- `RPA.HTTP` downloads the orders CSV at runtime; the bot is self-contained
- `RPA.PDF` converts the receipt HTML to PDF for each order
- Each PDF is saved to `output/receipts/<order_number>.pdf`

> **Note:** See the [Level II version](https://github.com/J3R3B3AR/robocorp-certification-2) for an enhanced implementation that adds retry logic, robot screenshots embedded into PDF receipts, and a final ZIP archive of all receipts.

## Author

**Jeremy Vargo**
- Email: jeremy.e.vargo@gmail.com
- LinkedIn: [linkedin.com/in/jeremyevargo](https://linkedin.com/in/jeremyevargo)
- GitHub: [github.com/J3R3B3AR](https://github.com/J3R3B3AR)
