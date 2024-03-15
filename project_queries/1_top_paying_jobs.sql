/*
Question: What are the top 10 highest-paying Data Analyst roles that are available remotely?
- Why? Highlight the top-paying opportunities for Data Analysts, offering insights into employment options and location flexibility.
*/
SELECT
    job_title,
    job_schedule_type,
    job_posted_date::DATE,
    salary_year_avg
FROM
    job_postings_fact
LEFT JOIN company_dim
    ON job_postings_fact.company_id = company_dim.company_id
WHERE
    job_title_short = 'Data Analyst'
    AND job_work_from_home = TRUE
    AND salary_year_avg IS NOT NULL 
ORDER BY
    salary_year_avg DESC
LIMIT 10;