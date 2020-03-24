# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:35:09 2020

@author: Zachary Wozich
Assignment 3
Class - Info 2820

"""

from person import Person
#help(Person)

class Employee(Person):
    """ Defines information for a Employee """

    def __init__(self, name, address, phone, badge, salary):
        """Constructor creates a Student with the given """

        self.name = name
        self.address = address
        self.phone = phone
        self.badge = badge
        self.salary = salary

    def set_badge(self, badge):
        self.badge = badge

    def get_badge(self):
        return self.badge
    
    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def __str__(self):
        return "Name: " + self.name + \
               "\nAddress: " + self.address + \
               "\nPhone: " + self.phone + \
                "\nbadge: " + self.badge + \
               "\nsalary: " + self.salary
              

class Customer(Person):
    """ Defines information for a Customer """
    
    def __init__(self, name, address, phone, credit_score):
        """Constructor creates a Student with the given """

        self.name = name
        self.address = address
        self.phone = phone
        self.credit_score = credit_score

    def set_credit_score(self, credit_score):
        self.credit_score = credit_score

    def get_credit_score(self):
        return self.credit_score

    def __str__(self):
        return "Name: " + self.name + \
               "\nAddress: " + self.address + \
               "\nPhone: " + self.phone + \
               "\ncredit_score: " + self.credit_score

