SELECT 
    table_with_individuals.display_name AS 'Contact display name',
    table_with_employer.display_name AS 'Employer organization name,',
    incident_numbers AS 'Number (count) of cases'
FROM
    (SELECT 
        cc.display_name,
            count(*) AS 'incident_numbers',
            cc.employer_id
    FROM
        civicrm_case_contact AS ccc
    INNER JOIN civicrm_contact AS cc
    WHERE
        ccc.contact_id = cc.id
            AND cc.contact_type = 'Individual'
    GROUP BY ccc.contact_id) AS table_with_individuals
        LEFT OUTER JOIN
    civicrm_contact table_with_employer ON table_with_individuals.employer_id = table_with_employer.id;

