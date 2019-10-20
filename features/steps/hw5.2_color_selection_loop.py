from behave import when, given, then
from selenium.webdriver.common.by import By
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, 'div#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, 'div#variation_color_name span.selection')


@then("Verify user can select through colors of jeans")
def verify_colors(context):
    expected_colors = ['Medium Wash', 'Dark Wash', 'Rinse']

    color_webelements = context.driver.find_elements(*COLOR_OPTIONS)
    print('There are: ', color_webelements, 'color webelements.')

    """
    for x in range(len(color_webelements)):
        color_webelements[x].click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text

        print('The actual color is: ', actual_color, '.')
        assert actual_color == expected_colors[x], f'Expected {expected_colors[x]}, but got [expected_color]'
    """
    for color in color_webelements:
        color.click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text
        print('The actual color is: ', actual_color, '.')
        assert actual_color == expected_colors[color_webelements.index(color)]
