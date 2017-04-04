SELECT n.value, count(*) as number_cafes
FROM nodes_tags
JOIN (SELECT id, value
FROM nodes_tags
WHERE key = 'postcode') n
ON nodes_tags.id = n.id
WHERE nodes_tags.key = 'amenity'
AND nodes_tags.value = 'cafe'
GROUP BY n.value
ORDER BY count(*) desc
LIMIT 25;
