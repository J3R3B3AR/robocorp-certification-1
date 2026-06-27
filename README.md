# Sales Data Automation - Robocorp Level I Certification

![Demo](robocorp-cert-i-demo.gif)

An entry-level RPA bot built with Robocorp and Python that automates Maria's weekly sales data entry workflow at [RobotSpareBin Industries](https://robotsparebinindustries.com/). This is the **Automation Certification Level I** project.

## What It Does

1. **Opens the intranet:** navigates to the RobotSpareBin Industries intranet
2. **Logs in:** authenticates as the intranet admin (Maria)
3. **Downloads sales data:** fetches `SalesData.xlsx` directly from the site
4. **Processes each row:** for every sales representative in the spreadsheet:
   - Fills in first name, last name, sales target, and sales result
   - Submits the form
5. **Captures results:** takes a screenshot of the completed sales summary table
6. **Exports to PDF:** converts the results table to `output/sales_results.pdf`
7. **Logs out**

## Project Structure

```
robocorp-cert-i/
├── tasks.py      # Main automation logic
├── conda.yaml    # Python environment definition (managed by RCC)
├── robot.yaml    # Task and environment configuration
└── output/
    ├── sales_summary.png   # Screenshot of completed results table
    └── sales_results.pdf   # PDF export of the sales data
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
2. Click the Robocorp panel -> Run "Robot Spare Bin Python"

**Command line:**
```bash
rcc run
```

RCC reads `conda.yaml` and builds an isolated Python environment automatically. No manual `pip install` needed.

## Key Implementation Notes

- Uses `robocorp-browser` (Playwright) for browser control with `slowmo=100`
- `RPA.HTTP` downloads the Excel file at runtime; the bot is self-contained
- `RPA.Excel.Files` reads `SalesData.xlsx` without requiring Microsoft Excel
- `RPA.PDF` converts the final HTML results table to a single PDF
- Output files are saved to the `output/` directory

> **Note:** See the [Level II version](https://github.com/J3R3B3AR/robocorp-certification-2) for an enhanced implementation that adds retry logic, robot screenshots embedded into PDF receipts, and a final ZIP archive of all receipts.

## Author

**Jeremy Vargo**
- Email: jeremy.e.vargo@gmail.com
- LinkedIn: [linkedin.com/in/jeremyevargo](https://linkedin.com/in/jeremyevargo)
- GitHub: [github.com/J3R3B3AR](https://github.com/J3R3B3AR)
