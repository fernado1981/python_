class locators_flightsearch:
    locators = {
        "xpath_from": "//select[@name='fromPort']/option[text()='{}']",
        "xpath_to": "//select[@name='toPort']/option[text()='{}']",
        "xpath_submit": "//input[@type='submit']",
        "xpath_count_flights": "//table/tbody/tr"
    }