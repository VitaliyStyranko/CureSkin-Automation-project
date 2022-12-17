# Created by Vitaliy at 12/15/2022
Feature: User can access the product page from the Collection page


  Scenario: User can access the product page from the Collection page
    Given Open Collections page
    When Click on a Body collection link
    Then Verify the user is taken to the products page