import unittest
from structured_refusal_boundary.core import run
class DomainTests(unittest.TestCase):
 def fixture(self):return {'fields':{'r':['ok']},'events':[dict(kind='text',text='{"r":"ok"}'),dict(kind='completed')]}
 def test_success(self):self.assertTrue(run(self.fixture())['accepted'])
 def test_refusal_overrides_valid_json(self):
  d=self.fixture();d['events'].append(dict(kind='refusal'));self.assertEqual(run(d)['reason'],'refused')
 def test_incomplete(self):
  d=self.fixture();d['events'][-1]['kind']='incomplete';self.assertFalse(run(d)['accepted'])
 def test_duplicates(self):
  d=self.fixture();d['events'][0]['text']='{"r":"bad","r":"ok"}';self.assertEqual(run(d)['reason'],'invalid_json')
