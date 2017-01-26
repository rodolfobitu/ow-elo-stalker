select
  DATE_TRUNC('hour', r.timestamp) + DATE_PART('minute', r.timestamp)::int / 10 * interval '10 minute' as time
  , max(r.elo)
from
  ow.users_ranked r
WHERE
  user_id = {}
  AND r.timestamp > NOW() - INTERVAL '{} day'
GROUP BY
  DATE_TRUNC('hour', r.timestamp) + DATE_PART('minute', r.timestamp)::int / 10 * interval '10 minute'
ORDER BY
  time DESC;