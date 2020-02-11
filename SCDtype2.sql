--postgreSQL

SELECT
	t1.post_id,
    t1."views",
    t1.likes,
    t1.shares,
    MIN(t1.dttm) effective_from,
    COALESCE(t2.dttm, TO_TIMESTAMP('9999-12-31 23:59:59', 'yyyy-mm-dd HH24:MI:SS')) effective_to

FROM posts_stats t1
LEFT JOIN posts_stats t2
    ON  t2.post_id = t1.post_id
    and t2.dttm > t1.dttm
    and (t2.likes <> t1.likes
      or t2."views" <> t1."views"
      or t2.shares <> t1.shares)
    AND NOT EXISTS (
        SELECT 1 FROM posts_stats t3
        WHERE
				t3.post_id = t1.post_id
                and (t3.likes <> t1.likes
                or t3."views" <> t1."views"
                or t3.shares <> t1.shares)

            AND t3.dttm > t1.dttm
            AND t3.dttm < t2.dttm
    )
GROUP BY
	t1.post_id,
    t1."views",
    t1.likes,
    t1.shares,
    t2.dttm
ORDER BY
    post_id, effective_from