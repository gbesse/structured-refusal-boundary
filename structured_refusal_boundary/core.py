import json,math
from .common import number,integer,identifier,unique_ids
def run(d):
 fields=d['fields'];events=d['events']
 if not isinstance(fields,dict)or not 1<=len(fields)<=50 or len(events)>1000:raise ValueError('shape')
 for k,values in fields.items():
  identifier(k)
  if not isinstance(values,list)or not values or any(not isinstance(v,str)for v in values):raise ValueError('choices')
 refusals=[i for i,e in enumerate(events)if e.get('kind')=='refusal'];terminals=[e for e in events if e.get('kind')in ['completed','incomplete','failed']];chunks=[e.get('text','')for e in events if e.get('kind')=='text']
 if any(not isinstance(c,str)for c in chunks)or sum(len(c)for c in chunks)>100000:raise ValueError('text')
 reason='refused'if refusals else 'terminal_ambiguous'if len(terminals)!=1 else 'not_completed'if terminals[0]['kind']!='completed'else None;payload=None
 if reason is None:
  def unique(pairs):
   out={}
   for k,v in pairs:
    if k in out:raise ValueError('duplicate')
    out[k]=v
   return out
  try:
   payload=json.loads(''.join(chunks),object_pairs_hook=unique)
   if not isinstance(payload,dict)or set(payload)!=set(fields)or any(type(payload[k])is not str or payload[k]not in values for k,values in fields.items()):reason='schema_mismatch';payload=None
  except (ValueError,TypeError):reason='invalid_json';payload=None
 return dict(accepted=reason is None,reason=reason,payload=payload,refusal_event_indices=refusals)
