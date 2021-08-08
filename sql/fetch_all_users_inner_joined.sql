select
    users.id,
    users.name,
    tickets.name from users
inner join tickets on tickets.user_id = users.id
where users.id = :id
