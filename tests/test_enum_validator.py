import unittest
from district42 import json_schema as schema
from validator_testcase import ValidatorTestCase


class TestEnumValidator(ValidatorTestCase):
  
  def test_it_validates_enumerators(self):
    self.assertValidationPasses('banana', schema.enum('banana', 'cucumber'))
    self.assertValidationPasses(None,     schema.enum(None, False, 0, ''))

    self.assertValidationFails('carrot', schema.enum('banana', 'cucumber'))
    self.assertValidationFails(0,        schema.enum(*range(1, 10)))
    self.assertValidationFails(False,    schema.enum(0, 1))

  def test_it_validates_nullable(self):
    self.assertValidationPasses(None, schema.enum('banana', 'cucumber').nullable)
    self.assertValidationPasses(None, schema.enum(None, False, 0, '').nullable)

    self.assertValidationFails(False, schema.enum('true', 'false').nullable)
    self.assertValidationFails(0,     schema.enum('true', 'false').nullable)
    self.assertValidationFails('',    schema.enum('true', 'false').nullable)
    self.assertValidationFails([],    schema.enum('true', 'false').nullable)
    self.assertValidationFails({},    schema.enum('true', 'false').nullable)


if __name__ == '__main__':
  unittest.main()
