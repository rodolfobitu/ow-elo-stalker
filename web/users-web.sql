select
  u.id
  , regexp_replace(u.battletag, '-.*', '') as battletag
from
  ow.users u;