# Created by Vitaliy at 12/12/2022
Feature: Cart test cases

  Scenario:Cart has correct product information
    Given Open Product Details cureskin-cleansing-gel page
    When Click to add product to cart
    And Verify added to your cart confirmation is shown
    Then Open cart page
    And Verify CureSkin Cleansing Gel is in the cart
