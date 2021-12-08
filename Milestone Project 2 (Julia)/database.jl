module database

    include("./models.jl")
    using SQLite
    using .models: User

    using Dates

    #create new DATABASE
    db = SQLite.DB("MILESTONE_DB")

    #create new TABLE

    query =  "CREATE TABLE IF NOT EXISTS `Milestone_Users` (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL, username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE, contact TEXT NOT NULL,
         joining_date TEXT, password TEXT NOT NULL, account_balance INTEGER DEFAULT 0 );"

    SQLite.execute(db, query)

    function add_user(user)

        query = "INSERT INTO `Milestone_Users` (name, username, email, password, contact, joining_date)  
            VALUES  ('$user.name',
                    '$user.username', '$user.email', '$user.password', '$user.contact', 
                    '$Dates.now(Dates.UTC)');"

        SQLite.execute(db, query)
    end

    function read_user(attribute, filter_by)

        key = [i for i in keys(filter_by)][1]
        value = [i for i in values(filter_by)][1]

        query = "SELECT `$attribute` from `Milestone_Users` where `$key` = '$value'"
        return DBInterface.execute(db, query)
    end

    function update_user(update, by)
        by_key, by_value = [i for i in keys(by)][1],  [i for i in values(by)][1]
        update_key, update_value =  [i for i in keys(update)][1],  [i for i in values(update)][1]

        query = """Update Milestone_Users set `$update_key` = '$update_value' where `$by_key` = '$by_value'"""
        DBInterface.execute(db, query)
    end


    export add_user, read_user


end