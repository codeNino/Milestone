module database

    include("./models.jl")
    using MySQL, DBInterface
    using .models: User

    using Dates

    #create server connection
    conn =  DBInterface.connect(MySQL.Connection, "127.0.0.1", "root", "Oluwanino7")

    #create new DATABASE
    DBInterface.execute(conn, "CREATE DATABASE IF NOT EXISTS Milestone_Project")
    DBInterface.execute(conn, "USE Milestone_Project")


    #create new TABLE

    query =  "CREATE TABLE IF NOT EXISTS `Milestone_Users` (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL, username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE, contact TEXT NOT NULL,
         joining_date TEXT, password TEXT NOT NULL, account_balance INTEGER DEFAULT 0 );"

    DBInterface.execute(conn, query)
    DBInterface.close!(conn)

    function add_user(user)

        conn = DBInterface.connect(MySQL.Connection, "127.0.0.1", "root", "Oluwanino7", "Milestone_Project", 3306)

        query = "INSERT INTO `Milestone_Users` (name, username, email, password, contact, joining_date)  
            VALUES  ('$user.name',
                    '$user.username', '$user.email', '$user.password', '$user.contact', 
                    '$Dates.now(Dates.UTC)');"

        DBInterface.execute(conn, query)
        DBInterface.close!(conn)
    end

    function read_user(attribute, filter_by)

        conn = DBInterface.connect(MySQL.Connection, "127.0.0.1", "root", "Oluwanino7", "Milestone_Project")

        key = [i for i in keys(filter_by)][1]
        value = [i for i in values(filter_by)][1]

        query = "SELECT `$attribute` from `Milestone_Users` where `$key` = '$value'"
        return DBInterface.execute(conn, query)
        DBInterface.close!(conn)
    end

    function update_user(update, by)

        conn = DBInterface.connect(MySQL.Connection, "127.0.0.1", "root", "Oluwanino7", "Milestone_Project", 3306)
        by_key, by_value = [i for i in keys(by)][1],  [i for i in values(by)][1]
        update_key, update_value =  [i for i in keys(update)][1],  [i for i in values(update)][1]

        query = """Update Milestone_Users set `$update_key` = '$update_value' where `$by_key` = '$by_value'"""
        DBInterface.execute(conn, query)
        DBInterface.close!(conn)
    end


    export add_user, read_user, update_user


end