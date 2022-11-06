Feature: Health_care

  Background: :User should be able to purchase a product in Pharmeasy application through healthcare module
    Given User is able to launch browsers
    When User is able to click on health_care module
    Then User is  able to click on Covid essentials
    And User is able to click on Covid Test Kits
    And User is able to click on popularity
    Then User is able to select a product according its popularity
    Then User is able to filter the product according to its brand
    And User should be able to select and choose price range
    Then User should be able to select product
    And User should be able add the product to cart
    And User should be able to select Qty of items to be added to cart
    Then User should be to click on view cart
  Scenario Outline:
    Then User is able to add the delivery address
    When User enter valid phone "<number>" in phone number text field
    Then User should be able to click on send otp
    And User should be able to click on submit otp
    And close browser

    Examples:
      |number|
      |7396424409|
      |123456789 |
      |87654321 |


