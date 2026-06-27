from robocorp.tasks import task
from robocorp import browser
from RPA.HTTP import HTTP
from RPA.PDF import PDF
from RPA.Tables import Tables


@task
def order_robots_from_RobotSpareBin():
    """
    Orders robots from RobotSpareBin Industries.
    Saves each order receipt as a PDF file.
    """
    browser.configure(slowmo=100)
    open_robot_order_website()
    orders = get_orders()
    for row in orders:
        close_annoying_modal()
        fill_the_form(row)
        preview_robot()
        submit_order()
        order_number = get_order_number()
        store_receipt_as_pdf(order_number)
        order_another_robot()


def open_robot_order_website():
    """Navigates to the RobotSpareBin Industries order portal."""
    browser.goto("https://robotsparebinindustries.com/#/robot-order")


def get_orders():
    """Downloads the orders CSV and returns it as a table."""
    http = HTTP()
    http.download(
        url="https://robotsparebinindustries.com/orders.csv",
        overwrite=True,
    )
    tables = Tables()
    return tables.read_table_from_csv("orders.csv", header=True)


def close_annoying_modal():
    """Dismisses the terms-and-conditions modal popup."""
    page = browser.page()
    page.click(".alert-buttons button.btn-dark")


def fill_the_form(row):
    """Fills the robot order form with data from one CSV row."""
    page = browser.page()
    page.select_option("#head", str(row["Head"]))
    page.click(f"#id-body-{row['Body']}")
    page.fill(
        "input[placeholder='Enter the part number for the legs']",
        str(row["Legs"]),
    )
    page.fill("#address", str(row["Address"]))


def preview_robot():
    """Clicks the Preview button to render the assembled robot image."""
    browser.page().click("#preview")


def submit_order():
    """Clicks the Order button to submit the current order."""
    browser.page().click("#order")


def get_order_number():
    """Reads the order confirmation number from the receipt badge."""
    element = browser.page().query_selector("#receipt p.badge-success")
    return element.inner_text() if element else "unknown"


def store_receipt_as_pdf(order_number):
    """Saves the HTML receipt for the current order as a PDF file."""
    receipt_html = browser.page().locator("#receipt").inner_html()
    pdf = PDF()
    pdf.html_to_pdf(receipt_html, f"output/receipts/{order_number}.pdf")


def order_another_robot():
    """Clicks 'Order another robot' to return to the order form."""
    browser.page().click("#order-another")
