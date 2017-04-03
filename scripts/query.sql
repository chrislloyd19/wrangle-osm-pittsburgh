SELECT value, count(*)
FROM ways_tags
JOIN (
  SELECT DISTINCT id
  FROM ways_tags
  WHERE value = 'Renfrew'
) w ON w.id = ways_tags.id
GROUP BY value
ORDER BY count(*) desc;
